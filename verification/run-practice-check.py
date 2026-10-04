"""Practice-only live integration check. Supplies fixed test-user inputs, never agent decisions."""
import json,time,uuid,urllib.request,sys
from pathlib import Path
scenario=sys.argv[1] if len(sys.argv)>1 else 'question'
assert scenario in ('question','refusal')
base='http://127.0.0.1:8765'
def req(path,body=None,token=None):
    headers={'Content-Type':'application/json'}
    if token: headers['X-SaunpDo-Session']=token
    r=urllib.request.Request(base+path,data=json.dumps(body).encode() if body is not None else None,headers=headers)
    with urllib.request.urlopen(r,timeout=10) as f: return json.load(f)
tokens=req('/api/session')['tokens']
rid=req('/api/run',{'mode':'practice'},tokens['presenter'])['run_id']
def state(): return req('/api/state?run='+rid)
def act(role,kind,args):
    s=state()
    return req('/api/action',{'run_id':rid,'kind':kind,'args':args,'request_id':str(uuid.uuid4()),'expected_state_version':s['case']['state_version']},tokens[role])
def until(check,seconds=80):
    end=time.monotonic()+seconds
    while time.monotonic()<end:
        s=state()
        if check(s): return s
        if s['run']['status'] in ('closed','halted'): raise RuntimeError('Run ended before the expected input opportunity: '+rid)
        time.sleep(1)
    raise RuntimeError('Timed out waiting for the live model: '+rid)
print('Practice '+scenario+' run: '+rid,flush=True)
act('buyer','grant',{'minutes':30,'confirmed':True})
s=until(lambda s:any(m['response_kind']=='invitation' for m in s['messages']))
m=next(m for m in s['messages'] if m['response_kind']=='invitation')
act('receiver','respond',{'message_id':m['id'],'choice':'Accept invitation'})
s=until(lambda s:s['run']['status']=='waiting' and any(m['purpose']=='explain' or m['response_kind']=='text' for m in s['messages']))
if scenario=='refusal': act('receiver','availability',{'choice':'I can receive'})
a=next(a for a in s['samples'] if a['name']=='receiver-'+scenario+'.m4a')
act('receiver','audio',{'audio_id':a['id']})
end=time.monotonic()+100
while time.monotonic()<end:
    s=state()
    if s['run']['status'] in ('closed','halted'): break
    availability=next((m for m in s['messages'] if m['response_kind']=='availability' and not m['answered']),None)
    if availability and not s['case']['receiver_availability']:
        act('receiver','respond',{'message_id':availability['id'],'choice':'I can receive'})
    time.sleep(1)
else: raise RuntimeError('Timed out awaiting actual agent outcome: '+rid)
result={'run_id':rid,'scenario':scenario,'driver':'Local app HTTP integration test','inputs':'Fixed practice grant, invitation acceptance, the selected original recording and availability (before a refusal, or if asked). No model decisions supplied.','status':s['run']['status'],'outcome':s['case']['outcome'],'model_calls':s['run']['model_calls'],'failure':s['run']['failure'],'messages':[{'to':m['recipient'],'text':m['text']} for m in s['messages']]}
Path(__file__).with_name(scenario+'-check-'+rid+'.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2),flush=True)
