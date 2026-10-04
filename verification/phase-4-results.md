# Phase 4 results

**Status:** Complete for the default coordination-only app. The final question and refusal checks both completed with real services. No parcel release or delivery completion was simulated or claimed. Phase 5 has not started.

## The finished artifact

The app has a buyer permission form, receiver inbox with Hindi voice/text input, and a presenter evidence view. Gemini chooses the tools and writes the messages. The local runtime enforces scope, recipient, state and evidence rules. SQLite saves the conversation between events. A real timer resumes a waiting agent.

New runs use prompt **v0.4.1**, model **gemini-3.8-flash**, temperature 1.0, maximum output 8,192 tokens and thinking level LOW. The latter is a supported Gemini 3 setting in the [official thinking guide](https://ai.google.dev/gemini-api/docs/generate-content/thinking). Gnani STT reported **gnani-prisma-v2.5** in the live responses. Prompt, tool contracts and actual model responses are snapshotted per run.

## Final live checks

Both runs below happened on **4 October 2026**. The app shows local time; raw records use UTC. The case's “out for delivery on 3 October” remains a fictional scenario fact.

| Check | Saved run | Result | Actual service responses |
| --- | --- | --- | --- |
| Buyer grant, invitation, real Hindi question and availability | `run-78e31f8d0d0a` | Agent answered the parcel question, kept carrier verification separate, notified both app inboxes and closed as unresolved | 11 Gemini, 1 Gnani STT |
| Invitation accepted, availability confirmed, then real Hindi refusal | `run-44a85da4814c` | Agent interpreted the later refusal, notified both app inboxes and closed as declined | 10 Gemini, 1 Gnani STT |

The final checks used a local HTTP test driver to supply fixed **practice** choices and the original user-supplied recordings. It did not give the model its next tool, decision, interpretation or answer. These are integration tests, not participant interviews or the final competition recording. Earlier UI runs exercised buyer permission, invitation acceptance, availability and both audio choices through the real interface. Final results were also opened and inspected in the browser.

In the final refusal run, an initial close request named an unknown evidence reference. The runtime rejected it, returned the error, and the model corrected its request before closure. This recovery is retained in the decision ledger.

The refusal's actual Gnani transcript was:

> मैंने पहले ही कहा था लेकिन अब मैं यह पार्सल नहीं लेना चाहती।

It is retained exactly. No words were changed to match the suggested recording script. A separate human listening/transcript review belongs in the final rehearsal.

## Checks that passed

**33 automated checks**, with no live provider calls inside the offline suite. The saved output is `offline-test-output.txt`.

They cover explicit buyer permission, role restrictions, invitation requirements, expiry, revocation, later withdrawal, duplicate requests, stale writes, unknown audio, transcription caching, provider failure, invalid arguments, unavailable carrier tools, notification requirements, evidence references, pending input during closure, real timer behavior and restart handling.

The HTTP checks cover foreign Host/Origin rejection, required role sessions, artifact path traversal, persistent read state and export contents. Python compilation, JavaScript syntax and launcher syntax were checked. These are development checks, not a production security audit.

The browser check covered all three role views, accepted invitation, recorded availability, the actual saved audio controls, original Gnani response inspection, and reopening saved results. Keyboard activation was used where the computer-use browser did not deliver pointer clicks reliably. No claim is made that the app has been tested across all browsers or devices.

The two final run ZIPs contain the prompt, enabled tool definitions, configuration, model version evidence, original audio, raw API request/response files, messages, event log, readable trace and a decision ledger. The credential scan found **zero occurrences of the two configured API key values**, including inside ZIP members. It is an exact-key scan, not a general personal-data audit.

## Problems found and corrected

1. **OTP wording.** An early live answer incorrectly implied the receiver would not need an OTP. R09 now says SaunpDo cannot promise a carrier waiver. The final question answer says SaunpDo does not ask for an OTP and the carrier follows its own process.
2. **Response cap.** A retest hit MAX_TOKENS. The adapter saved the response and stopped without executing the partial result. The final configuration uses the larger limit and LOW thinking. It was then verified live.
3. **New input during closure.** A new refusal could remain queued while the model repeatedly tried to close. The runtime now yields at the next tool boundary, saves the continuation and supplies that actual new event on the next worker pass. A regression check covers the race.
4. **Dependent tools in one batch.** A failed message could previously be followed by a wait from the same model response. Later calls in that batch now fail with `PRIOR_TOOL_FAILED`, so the model sees the failure before choosing again.
5. **Unnecessary null field.** `attempt_id` is optional in the enabled coordination-only `send_message` contract. Any non-null attempt is still rejected. This removes a request for an irrelevant null value without silently repairing model output.
6. **Availability controls.** An invited receiver can offer availability directly. The app shows only one set of availability controls when the agent has already asked. Earlier availability is labelled as such after a later spoken refusal.

## Preserve the failed runs

`run-index.json` lists all nine development runs. Older runs remain in `prototype/data/runs/`, including the bad OTP wording, response-limit failure, queue failure and superseded checks. They are diagnostic records. Do not use them as final submission evidence or rewrite their messages. The two final runs above are the verified examples for this build.

## What this phase does not prove

- It does not establish that a fictional order is acceptable under the competition's real-source rule.
- It does not test the proposed Delhivery authorization/consumption APIs. They are disabled and unimplemented here because organiser permission is unresolved.
- It does not call Pine Labs, perform a payment, confirm a delivery or test carrier custody.
- It does not provide production identity verification, carrier account access, WhatsApp messaging, cloud deployment or load testing.
- It does not prove that all future model outputs will be correct. Broader adversarial checks, real participant rehearsal and version freeze remain Phase 6.
- It is not the final screen recording. The recording still needs actual participants, source disclosures, a selected run and a link.

The practical outcome today is a working, observable agent for the supported coordination branch. The main delegated-release promise still depends on carrier-side integration.
