# SaunpDo decision ledger

Recorded model choices. This is a fictional order scenario; practice clicks are labelled OPERATOR_TEST_ACTION.

## D-f0b3f67c93f8 · get_parcel_context

- When: 2026-10-03T20:50:05.508837+00:00
- Trigger: E-884cc462157b
- Source and connector: OPERATOR_TEST_ACTION:E-884cc462157b; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Read current case facts and enrolled participants before taking action.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason":"Read current case facts and enrolled participants before taking action.","rule_id":"R03","case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-884cc462157b",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 2,
    "received_at": "2026-10-03T20:50:03.366137+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-fee9a22923d0",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-03T20:50:03.364686+00:00",
        "expires_at": "2026-10-03T21:20:03.364686+00:00",
        "revoked_at": null,
        "source_event_id": null
      },
      "request": "Help my mother understand this test parcel and answer her questions. Carrier release support is unavailable."
    },
    "state_version_before": 0,
    "state_version_after": 1
  }
]
```

Earlier tool results available in this decision context: 

## D-78f7ae5fe98a · send_message

- When: 2026-10-03T20:50:12.581153+00:00
- Trigger: E-884cc462157b
- Source and connector: OPERATOR_TEST_ACTION:E-884cc462157b; SaunpDo participant app
- Decision: send_message
- Why: R07: Invite the receiver to accept help for the fictional parcel demo with Aarav's permission.
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
नमस्ते मीरा जी, यह एक डेमो है। आरव की मंज़ूरी से क्या आप पार्सल में मदद लेना चाहती हैं?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-884cc462157b",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 2,
    "received_at": "2026-10-03T20:50:03.366137+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-fee9a22923d0",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-03T20:50:03.364686+00:00",
        "expires_at": "2026-10-03T21:20:03.364686+00:00",
        "revoked_at": null,
        "source_event_id": null
      },
      "request": "Help my mother understand this test parcel and answer her questions. Carrier release support is unavailable."
    },
    "state_version_before": 0,
    "state_version_after": 1
  }
]
```

Earlier tool results available in this decision context: E-5a1984aec8f6

## D-298f853cf2b7 · wait_for_event

- When: 2026-10-03T20:50:12.583260+00:00
- Trigger: E-884cc462157b
- Source and connector: OPERATOR_TEST_ACTION:E-884cc462157b; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for the receiver to respond to the invitation or send input.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"case_id":"DEMO-CASE-001","rule_id":"R12","event_types":["invitation_responded","receiver_text_received","receiver_audio_uploaded","buyer_revoked"],"reason":"Wait for the receiver to respond to the invitation or send input.","timeout_seconds":120}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-884cc462157b",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 2,
    "received_at": "2026-10-03T20:50:03.366137+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-fee9a22923d0",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-03T20:50:03.364686+00:00",
        "expires_at": "2026-10-03T21:20:03.364686+00:00",
        "revoked_at": null,
        "source_event_id": null
      },
      "request": "Help my mother understand this test parcel and answer her questions. Carrier release support is unavailable."
    },
    "state_version_before": 0,
    "state_version_after": 1
  }
]
```

Earlier tool results available in this decision context: E-5a1984aec8f6, E-d6bba1c7cd0c

## D-20d0bf3d52c3 · get_parcel_context

- When: 2026-10-03T20:51:02.816841+00:00
- Trigger: E-2e10fe3633d7
- Source and connector: OPERATOR_TEST_ACTION:E-2e10fe3633d7; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Refresh parcel context after invitation acceptance.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason":"Refresh parcel context after invitation acceptance.","case_id":"DEMO-CASE-001","rule_id":"R03"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-2e10fe3633d7",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 18,
    "received_at": "2026-10-03T20:51:00.981501+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-bea2fdf64727"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-5a1984aec8f6, E-d6bba1c7cd0c, E-477cbb9d057f

## D-425e5ceb9ff0 · send_message

- When: 2026-10-03T20:51:08.718686+00:00
- Trigger: E-2e10fe3633d7
- Source and connector: OPERATOR_TEST_ACTION:E-2e10fe3633d7; SaunpDo participant app
- Decision: send_message
- Why: R06: Explain demo parcel details and delivery company verification limitations, and invite questions.
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
यह मायंट्रा से चादर का एक डेमो पार्सल है। डिलीवरी कंपनी अपनी जांच खुद करेगी, क्या आपका कोई सवाल है?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-2e10fe3633d7",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 18,
    "received_at": "2026-10-03T20:51:00.981501+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-bea2fdf64727"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-5a1984aec8f6, E-d6bba1c7cd0c, E-477cbb9d057f, E-4a82ffbedb2b

## D-b0ccf41f9871 · wait_for_event

- When: 2026-10-03T20:51:08.721224+00:00
- Trigger: E-2e10fe3633d7
- Source and connector: OPERATOR_TEST_ACTION:E-2e10fe3633d7; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for receiver question or input.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"timeout_seconds":120,"event_types":["receiver_text_received","receiver_audio_uploaded","availability_changed","buyer_revoked"],"rule_id":"R12","reason":"Wait for receiver question or input.","case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-2e10fe3633d7",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 18,
    "received_at": "2026-10-03T20:51:00.981501+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-bea2fdf64727"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-5a1984aec8f6, E-d6bba1c7cd0c, E-477cbb9d057f, E-4a82ffbedb2b, E-b97ebb226424

## D-05f1ffa4f45b · get_parcel_context

- When: 2026-10-03T20:51:34.366927+00:00
- Trigger: E-9cbd7cfa4286
- Source and connector: OPERATOR_TEST_ACTION:E-9cbd7cfa4286; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Refresh parcel context after availability change.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"case_id":"DEMO-CASE-001","reason":"Refresh parcel context after availability change.","rule_id":"R03"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-9cbd7cfa4286",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 34,
    "received_at": "2026-10-03T20:51:32.788759+00:00",
    "event_type": "availability_changed",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "I can receive",
      "interface": "receiver_availability_form"
    },
    "state_version_before": 2,
    "state_version_after": 3
  }
]
```

Earlier tool results available in this decision context: E-5a1984aec8f6, E-d6bba1c7cd0c, E-477cbb9d057f, E-4a82ffbedb2b, E-b97ebb226424, E-d3c2a0b6a93b

## D-bf6360b802df · wait_for_event

- When: 2026-10-03T20:51:46.890800+00:00
- Trigger: E-9cbd7cfa4286
- Source and connector: OPERATOR_TEST_ACTION:E-9cbd7cfa4286; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait briefly to see if receiver sends a question or audio after confirming availability.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"event_types":["receiver_text_received","receiver_audio_uploaded","buyer_revoked"],"case_id":"DEMO-CASE-001","rule_id":"R12","reason":"Wait briefly to see if receiver sends a question or audio after confirming availability.","timeout_seconds":30}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-9cbd7cfa4286",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 34,
    "received_at": "2026-10-03T20:51:32.788759+00:00",
    "event_type": "availability_changed",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "I can receive",
      "interface": "receiver_availability_form"
    },
    "state_version_before": 2,
    "state_version_after": 3
  }
]
```

Earlier tool results available in this decision context: E-5a1984aec8f6, E-d6bba1c7cd0c, E-477cbb9d057f, E-4a82ffbedb2b, E-b97ebb226424, E-d3c2a0b6a93b, E-baf791612b77

## D-741a0cbfaef2 · transcribe_receiver_audio

- When: 2026-10-03T20:51:48.880363+00:00
- Trigger: E-60956065a06a
- Source and connector: OPERATOR_TEST_ACTION:E-60956065a06a; SaunpDo participant app
- Decision: transcribe_receiver_audio
- Why: R02: Transcribe receiver audio upload to understand the receiver input.
- Recipient: Internal tool
- Through: Gnani STT
- Result: succeeded

Exact action/message:

```json
{"reason":"Transcribe receiver audio upload to understand the receiver input.","case_id":"DEMO-CASE-001","rule_id":"R02","audio_id":"sample-d99e628e177c3bd5"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-60956065a06a",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 41,
    "received_at": "2026-10-03T20:51:40.282171+00:00",
    "event_type": "receiver_audio_uploaded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "audio_id": "sample-d99e628e177c3bd5",
      "filename": "receiver-refusal.m4a",
      "sha256": "d99e628e177c3bd5085deac180c171adbafe73c79e72873ec3f61e2aa3d34f5b",
      "duration_seconds": 3.84,
      "recording_source": "USER_SUPPLIED_RECORDING",
      "transcript": null
    },
    "state_version_before": 3,
    "state_version_after": 4
  }
]
```

Earlier tool results available in this decision context: E-5a1984aec8f6, E-d6bba1c7cd0c, E-477cbb9d057f, E-4a82ffbedb2b, E-b97ebb226424, E-d3c2a0b6a93b, E-baf791612b77, E-fcf40f3cb8f9

## D-de6262952bcb · get_parcel_context

- When: 2026-10-03T20:51:51.988634+00:00
- Trigger: E-60956065a06a
- Source and connector: OPERATOR_TEST_ACTION:E-60956065a06a; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Refresh parcel context after audio transcription.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason":"Refresh parcel context after audio transcription.","case_id":"DEMO-CASE-001","rule_id":"R03"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-60956065a06a",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 41,
    "received_at": "2026-10-03T20:51:40.282171+00:00",
    "event_type": "receiver_audio_uploaded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "audio_id": "sample-d99e628e177c3bd5",
      "filename": "receiver-refusal.m4a",
      "sha256": "d99e628e177c3bd5085deac180c171adbafe73c79e72873ec3f61e2aa3d34f5b",
      "duration_seconds": 3.84,
      "recording_source": "USER_SUPPLIED_RECORDING",
      "transcript": null
    },
    "state_version_before": 3,
    "state_version_after": 4
  }
]
```

Earlier tool results available in this decision context: E-5a1984aec8f6, E-d6bba1c7cd0c, E-477cbb9d057f, E-4a82ffbedb2b, E-b97ebb226424, E-d3c2a0b6a93b, E-baf791612b77, E-fcf40f3cb8f9, E-5ececf2c517d

## D-d6b815411952 · send_message

- When: 2026-10-03T20:51:56.073933+00:00
- Trigger: E-60956065a06a
- Source and connector: OPERATOR_TEST_ACTION:E-60956065a06a; SaunpDo participant app
- Decision: send_message
- Why: R05: Acknowledge receiver refusal and confirm completion of coordination assistance.
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
आपकी बात समझ आ गई है। SaunpDo की सहायता यहीं समाप्त की जाती है।
```

Exact triggering input:

```json
[
  {
    "event_id": "E-60956065a06a",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 41,
    "received_at": "2026-10-03T20:51:40.282171+00:00",
    "event_type": "receiver_audio_uploaded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "audio_id": "sample-d99e628e177c3bd5",
      "filename": "receiver-refusal.m4a",
      "sha256": "d99e628e177c3bd5085deac180c171adbafe73c79e72873ec3f61e2aa3d34f5b",
      "duration_seconds": 3.84,
      "recording_source": "USER_SUPPLIED_RECORDING",
      "transcript": null
    },
    "state_version_before": 3,
    "state_version_after": 4
  }
]
```

Earlier tool results available in this decision context: E-5a1984aec8f6, E-d6bba1c7cd0c, E-477cbb9d057f, E-4a82ffbedb2b, E-b97ebb226424, E-d3c2a0b6a93b, E-baf791612b77, E-fcf40f3cb8f9, E-5ececf2c517d, E-196a9a327c77

## D-65e5672e4752 · send_message

- When: 2026-10-03T20:51:58.261301+00:00
- Trigger: E-60956065a06a
- Source and connector: OPERATOR_TEST_ACTION:E-60956065a06a; SaunpDo participant app
- Decision: send_message
- Why: R07: Inform buyer of receiver refusal and case closure.
- Recipient: DEMO-BUYER-01
- Through: SaunpDo local app
- Result: rejected

Exact action/message:

```json
Meera has declined to receive the demo parcel. Delegation coordination is now closed.
```

Exact triggering input:

```json
[
  {
    "event_id": "E-60956065a06a",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 41,
    "received_at": "2026-10-03T20:51:40.282171+00:00",
    "event_type": "receiver_audio_uploaded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "audio_id": "sample-d99e628e177c3bd5",
      "filename": "receiver-refusal.m4a",
      "sha256": "d99e628e177c3bd5085deac180c171adbafe73c79e72873ec3f61e2aa3d34f5b",
      "duration_seconds": 3.84,
      "recording_source": "USER_SUPPLIED_RECORDING",
      "transcript": null
    },
    "state_version_before": 3,
    "state_version_after": 4
  }
]
```

Earlier tool results available in this decision context: E-5a1984aec8f6, E-d6bba1c7cd0c, E-477cbb9d057f, E-4a82ffbedb2b, E-b97ebb226424, E-d3c2a0b6a93b, E-baf791612b77, E-fcf40f3cb8f9, E-5ececf2c517d, E-196a9a327c77, E-b01948402324

## D-fca932f12525 · send_message

- When: 2026-10-03T20:52:00.740081+00:00
- Trigger: E-60956065a06a
- Source and connector: OPERATOR_TEST_ACTION:E-60956065a06a; SaunpDo participant app
- Decision: send_message
- Why: R07: Inform buyer that receiver declined the parcel.
- Recipient: DEMO-BUYER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
Meera has declined to receive the demo parcel. Delegation coordination is now closed.
```

Exact triggering input:

```json
[
  {
    "event_id": "E-60956065a06a",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 41,
    "received_at": "2026-10-03T20:51:40.282171+00:00",
    "event_type": "receiver_audio_uploaded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "audio_id": "sample-d99e628e177c3bd5",
      "filename": "receiver-refusal.m4a",
      "sha256": "d99e628e177c3bd5085deac180c171adbafe73c79e72873ec3f61e2aa3d34f5b",
      "duration_seconds": 3.84,
      "recording_source": "USER_SUPPLIED_RECORDING",
      "transcript": null
    },
    "state_version_before": 3,
    "state_version_after": 4
  }
]
```

Earlier tool results available in this decision context: E-5a1984aec8f6, E-d6bba1c7cd0c, E-477cbb9d057f, E-4a82ffbedb2b, E-b97ebb226424, E-d3c2a0b6a93b, E-baf791612b77, E-fcf40f3cb8f9, E-5ececf2c517d, E-196a9a327c77, E-b01948402324, E-d8cce5caa8f7

## D-3bf8978adc14 · close_case

- When: 2026-10-03T20:52:07.328236+00:00
- Trigger: E-60956065a06a
- Source and connector: OPERATOR_TEST_ACTION:E-60956065a06a; SaunpDo participant app
- Decision: close_case
- Why: R14: Receiver explicitly stated in uploaded audio that she does not want to receive this parcel.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason_code":"receiver_declined","expected_state_version":4,"outcome":"declined","reason":"Receiver explicitly stated in uploaded audio that she does not want to receive this parcel.","rule_id":"R14","evidence_refs":["E-60956065a06a","E-0e98f56bdfec","message-02db57ba887a","E-3245d22508e3","message-2cee487fc109"],"case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-60956065a06a",
    "run_id": "run-0ed8189fd1fd",
    "sequence": 41,
    "received_at": "2026-10-03T20:51:40.282171+00:00",
    "event_type": "receiver_audio_uploaded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "audio_id": "sample-d99e628e177c3bd5",
      "filename": "receiver-refusal.m4a",
      "sha256": "d99e628e177c3bd5085deac180c171adbafe73c79e72873ec3f61e2aa3d34f5b",
      "duration_seconds": 3.84,
      "recording_source": "USER_SUPPLIED_RECORDING",
      "transcript": null
    },
    "state_version_before": 3,
    "state_version_after": 4
  }
]
```

Earlier tool results available in this decision context: E-5a1984aec8f6, E-d6bba1c7cd0c, E-477cbb9d057f, E-4a82ffbedb2b, E-b97ebb226424, E-d3c2a0b6a93b, E-baf791612b77, E-fcf40f3cb8f9, E-5ececf2c517d, E-196a9a327c77, E-b01948402324, E-d8cce5caa8f7, E-5e554f41a3e2
