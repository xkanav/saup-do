import sys
from pathlib import Path
import json, mimetypes
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

import shutil

# Add the prototype directory to Python path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app import App, Rejected

# Use /tmp for writable data on Vercel
DATA_DIR = Path('/tmp/data')

if not DATA_DIR.exists():
    try:
        shutil.copytree(ROOT / 'data', DATA_DIR)
    except Exception as e:
        print(f"Failed to copy data: {e}")
        DATA_DIR.mkdir(parents=True, exist_ok=True)

app_instance = App(DATA_DIR, ROOT)

class handler(BaseHTTPRequestHandler):
    def log_message(self, *args): pass
    
    def send(self, status, body, kind='application/json; charset=utf-8', extra=None):
        if not isinstance(body, bytes): 
            body = json.dumps(body, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', kind)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; media-src 'self' blob:; connect-src 'self'; frame-ancestors 'none'")
        if extra:
            for k, v in extra.items(): 
                self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)
        
    def trusted(self):
        # Allow all requests on Vercel
        return True
        
    def route(self):
        parsed = urlparse(self.path)
        return parsed.path, {k: v[0] for k, v in parse_qs(parsed.query).items()}
        
    def do_GET(self):
        if not self.trusted(): 
            return self.send(403, {'error':'Local demo only.'})
        
        path, q = self.route()
        try:
            if path in ('/', '/index.html'): 
                return self.send(200, (ROOT / 'static/index.html').read_bytes(), 'text/html; charset=utf-8')
            if path in ('/app.js', '/style.css'):
                return self.send(200, (ROOT / 'static' / path[1:]).read_bytes(), 'text/javascript; charset=utf-8' if path.endswith('.js') else 'text/css; charset=utf-8')
            if path == '/api/session': 
                return self.send(200, {'tokens': app_instance.tokens, 'identity_note': 'Demo role controls, not production authentication.'})
            if path == '/api/state': 
                return self.send(200, app_instance.view(q.get('run')))
            if path == '/api/audio':
                with app_instance.store.lock: 
                    asset = app_instance.store.db.execute('SELECT * FROM assets WHERE id=?', (q.get('id'),)).fetchone()
                if not asset: 
                    raise Rejected('UNKNOWN_AUDIO', 'Recording not found.')
                p = app_instance.data / asset['path']
                return self.send(200, p.read_bytes(), 'audio/mp4' if p.suffix == '.m4a' else (mimetypes.guess_type(p.name)[0] or 'application/octet-stream'))
            if path == '/api/artifact':
                rid = q.get('run')
                app_instance.store.row(rid)
                base = (app_instance.data / 'runs' / rid).resolve()
                requested = (base / q.get('path', '')).resolve()
                if not requested.is_relative_to(base) or not requested.is_file() or requested.name.endswith('.tmp'): 
                    raise Rejected('UNKNOWN_ARTIFACT', 'Artifact not found.')
                return self.send(200, requested.read_bytes(), 'application/json; charset=utf-8' if requested.suffix == '.json' else 'text/plain; charset=utf-8')
            if path == '/api/export': 
                return self.send(200, app_instance.export_zip(q['run']), 'application/zip', {'Content-Disposition': 'attachment; filename="saunpdo-run-evidence.zip"'})
            self.send(404, {'error': 'Not found'})
        except (ValueError, KeyError): 
            self.send(404, {'error': 'The requested run or file was not found.'})
            
    def do_POST(self):
        if not self.trusted(): 
            return self.send(403, {'error':'Local demo only.'})
            
        path, q = self.route()
        role = next((r for r, t in app_instance.tokens.items() if self.headers.get('X-SaunpDo-Session') == t), None)
        if not role: 
            return self.send(403, {'error': 'Open a demo role session first.'})
            
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length < 29 * 1024 * 1024: 
                raise Rejected('REQUEST_SIZE', 'Request is too large or empty.')
            data = json.loads(self.rfile.read(length))
            if not isinstance(data, dict): 
                raise Rejected('REQUEST_FORMAT', 'Expected a JSON object.')
                
            if path == '/api/run' and role == 'presenter':
                if set(data) != {'mode'}: 
                    raise Rejected('REQUEST_FORMAT', 'Only the run mode can be set.')
                return self.send(200, {'run_id': app_instance.new_run(data['mode'])})
            if path == '/api/action': 
                return self.send(200, app_instance.action(data['run_id'], role, data['kind'], data['args'], data['request_id'], data['expected_state_version']))
            if path == '/api/upload' and role == 'receiver': 
                return self.send(200, app_instance.upload(data['run_id'], data['name'], data['data']))
            if path == '/api/read': 
                return self.send(200, app_instance.read_message(data['run_id'], role, data['message_id']))
                
            self.send(403, {'error': 'This role cannot use that action.'})
        except Rejected as exc: 
            self.send(409, {'error': str(exc), 'code': exc.code})
        except (KeyError, ValueError, TypeError): 
            self.send(400, {'error': 'The request was incomplete or invalid.'})
        except Exception: 
            self.send(500, {'error': 'A local error stopped this request. No success was assumed.'})
