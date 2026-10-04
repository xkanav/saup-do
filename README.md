# Phase 4: SaunpDo working demonstration app

**BIG deliverable:** A local app that lets a buyer give limited permission, lets the receiver respond or send a real Hindi recording, and lets Gemini choose and execute its next actions. Every action and service response is saved. There are separate buyer, receiver and presenter views.

**Built:** 4 October 2026. **Scope:** Coordination only. No delivery completion is claimed. Phase 5 has not started.

## Open the app

1. Double-click `Start-SaunpDo.command` in this folder. Keep its Terminal window open while using the app.
2. Open http://127.0.0.1:8765 on this Mac. If the app is already running, the launcher opens it without starting another copy.
3. Choose **Run log**, then **New run +**. Leave the mode on **Practice clicks** when rehearsing or testing.
4. Choose **Aarav**. Read the permission, tick the box, and press **Give permission for this parcel**.
5. Choose **Maa**. Wait for the agent's invitation. Respond to what it actually asks. You may confirm availability, send text, or select a saved recording and press **Send voice note**.
6. Choose **Run log** to inspect model choices, incoming events, API calls, exact responses and stored messages. Press **Export this run** to save the evidence ZIP.

Practice runs still use real API credits. The two provided recordings are already available. Audio is sent to Gnani for transcription. The transcript and fictional case context are sent to Gemini. No microphone permission or WhatsApp setup is needed. The app does not send messages outside its own inboxes.

For a participant rehearsal, start a new **Participant demo** run and let the actual buyer and receiver make their own choices through the role views. The role selector is a demonstration interface, not production identity verification. Do not use participant mode for operator-generated choices.

## What the app can do

- Store one explicit buyer grant for one parcel, one receiver, one fixed home and a chosen expiry. The buyer can withdraw it.
- Keep invitation acceptance and availability separate. Use the exact options **I can receive**, **Not this parcel** and **I cannot receive**. Availability remains nonbinding.
- Let the receiver ask questions in text or with a real audio file. The original Gnani output stays unchanged in the evidence.
- Run Gemini with five enabled tools: read context, transcribe audio, send an in-app message, wait for an event and close the case.
- Resume a saved conversation when a new human input or real deadline arrives. Page refresh does not reset the run.
- Save brief rule-based reasons, raw service calls, model continuation, messages, events and a decision ledger.
- End with **unresolved**, **declined** or **cancelled**, based on the supported facts. “Cancelled” means the SaunpDo permission process ended, not that a merchant order was cancelled.

## The boundary that matters

This app uses the user-provided **fictional Myntra bedsheet, ₹900 prepaid, out for delivery on 3 October 2026** scenario. Real API timestamps show when testing actually happened. The carrier name and merchant name do not imply a partnership or integration.

The proposed Delhivery release capabilities remain unavailable. There is no rider app, real carrier scan, release approval, consumption, handover evidence or delivery confirmation. Pine Labs is not called because this case is prepaid. Optional tracking and Gnani TTS are not enabled.

SaunpDo can answer a parcel question and coordinate a refusal today. It cannot promise that the carrier will waive an OTP. The carrier follows its existing verification and controls actual release.

## Files you can work with

| File or folder | What it contains |
| --- | --- |
| `Start-SaunpDo.command` | Double-click launcher for this Mac |
| `prototype/` | Working application and its tests |
| `prototype/config/system-prompt.md` | Versioned prompt used by new runs |
| `prototype/config/tools.json` | The five enabled tool contracts |
| `prototype/data/saunpdo.sqlite3` | Saved cases, human events, inboxes and model continuation |
| `prototype/data/runs/<run-id>/` | Each run's prompt snapshot, exact calls, evidence and export files |
| `verification/phase-4-results.md` | What was checked, what changed and remaining limits |
| `verification/screenshots/` | Screenshots of the actual app |
| `phase-5-handoff.md` | What the next phase inherits, without starting it |

The evidence ZIP is a working evidence bundle, not a ready-to-publish submission. It includes consented recordings and complete conversation records. Review the selected run and remove unrelated personal information before sharing a public link.

## Setup and troubleshooting

The keys remain in `../phase-02/.env`, outside the app's static files and exports. The app reads `GEMINI_API_KEY`, `GNANI_API_KEY` and `GEMINI_MODEL`. Never paste credentials into the browser, prompt or submission answers.

This build was tested with Python 3.12 and `requests` 2.33.1. On a fresh Mac, install Python 3.12 or later, then run `python3 -m pip install -r requirements.txt` inside `prototype`. M4A inspection uses macOS's built-in audio utility. PCM WAV is the portable fallback. Accepted recordings are nonempty, at most 60 seconds, and at most 20 MB.

If the local app is not open, run `python3 server.py` from `prototype`. Keep the project in this folder structure so it can find Phase 2 credentials and the provided audio files. If a key changes, stop and restart the server.

If a service fails, the run keeps the exact error instead of inventing a response. Do not repair an old transcript or replace a model message. Fix the cause and create a new run. The old run remains evidence of the failure.

The model can wait about two minutes for a person. If you step away, it may close the run after a real timeout. Start a new run when everyone is ready. To stop the app, press Control+C in its Terminal window. An interrupted in-flight action is marked uncertain on restart and is not automatically replayed.

This is a localhost demonstration for one Mac. It is not an internet-hosted service. The buyer and receiver roles share the same screen/session environment. Production authentication, merchant onboarding, carrier integration and a public website are later work.
