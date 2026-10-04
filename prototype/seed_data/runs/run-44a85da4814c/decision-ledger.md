# SaunpDo decision ledger

Recorded model choices. This is a fictional order scenario; practice clicks are labelled OPERATOR_TEST_ACTION.

## D-f21fe89b69ac · get_parcel_context

- When: 2026-10-04T01:48:38.057160+00:00
- Trigger: E-295b0b1af11e
- Source and connector: OPERATOR_TEST_ACTION:E-295b0b1af11e; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Read parcel context and enrolled participants before taking action.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"rule_id":"R03","reason":"Read parcel context and enrolled participants before taking action.","case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-295b0b1af11e",
    "run_id": "run-44a85da4814c",
    "sequence": 2,
    "received_at": "2026-10-04T01:48:35.975563+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-d4805ce5bd2e",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:48:35.975508+00:00",
        "expires_at": "2026-10-04T02:18:35.975508+00:00",
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

## D-6a8193b6d64d · send_message

- When: 2026-10-04T01:48:40.388361+00:00
- Trigger: E-295b0b1af11e
- Source and connector: OPERATOR_TEST_ACTION:E-295b0b1af11e; SaunpDo participant app
- Decision: send_message
- Why: R07: Invite receiver Meera to coordinate parcel information under coordination_only mode.
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
नमस्ते मीरा जी, यह एक डेमो पार्सल की जानकारी है। आरव ने एक चादर का पार्सल आपके नाम से जोड़ने की मंज़ूरी दी है। क्या आप इस पार्सल की जानकारी में मदद चाहती हैं?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-295b0b1af11e",
    "run_id": "run-44a85da4814c",
    "sequence": 2,
    "received_at": "2026-10-04T01:48:35.975563+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-d4805ce5bd2e",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:48:35.975508+00:00",
        "expires_at": "2026-10-04T02:18:35.975508+00:00",
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

Earlier tool results available in this decision context: E-337fff51d1e3

## D-61eb62c0c60b · wait_for_event

- When: 2026-10-04T01:48:40.389985+00:00
- Trigger: E-295b0b1af11e
- Source and connector: OPERATOR_TEST_ACTION:E-295b0b1af11e; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for receiver response to invitation.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"event_types":["invitation_responded","receiver_text_received","receiver_audio_uploaded","buyer_revoked"],"timeout_seconds":120,"rule_id":"R12","reason":"Wait for receiver response to invitation.","case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-295b0b1af11e",
    "run_id": "run-44a85da4814c",
    "sequence": 2,
    "received_at": "2026-10-04T01:48:35.975563+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-d4805ce5bd2e",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:48:35.975508+00:00",
        "expires_at": "2026-10-04T02:18:35.975508+00:00",
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

Earlier tool results available in this decision context: E-337fff51d1e3, E-7332e0f1434b

## D-840e293083f1 · get_parcel_context

- When: 2026-10-04T01:48:42.749684+00:00
- Trigger: E-ab12333314c0
- Source and connector: OPERATOR_TEST_ACTION:E-ab12333314c0; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Read updated context following invitation acceptance.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason":"Read updated context following invitation acceptance.","rule_id":"R03","case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-ab12333314c0",
    "run_id": "run-44a85da4814c",
    "sequence": 17,
    "received_at": "2026-10-04T01:48:41.032024+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-18953e0a875a"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-337fff51d1e3, E-7332e0f1434b, E-70e51ea7ca0d

## D-b9fc465b75c9 · send_message

- When: 2026-10-04T01:48:44.518482+00:00
- Trigger: E-ab12333314c0
- Source and connector: OPERATOR_TEST_ACTION:E-ab12333314c0; SaunpDo participant app
- Decision: send_message
- Why: R06: Explain parcel facts, coordination_only limits, and offer to answer questions.
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
यह मिंत्रा से एक चादर का डेमो पार्सल है, जिसका भुगतान पहले ही हो चुका है। डिलीवरी कंपनी अपनी प्रक्रिया से ही पार्सल देगी। क्या आप इस पार्सल के बारे में कुछ पूछना चाहती हैं?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-ab12333314c0",
    "run_id": "run-44a85da4814c",
    "sequence": 17,
    "received_at": "2026-10-04T01:48:41.032024+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-18953e0a875a"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-337fff51d1e3, E-7332e0f1434b, E-70e51ea7ca0d, E-5206e5a84b52

## D-cc7c2be40208 · wait_for_event

- When: 2026-10-04T01:48:44.520737+00:00
- Trigger: E-ab12333314c0
- Source and connector: OPERATOR_TEST_ACTION:E-ab12333314c0; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for Meera to ask a question or provide input.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"timeout_seconds":120,"rule_id":"R12","event_types":["receiver_text_received","receiver_audio_uploaded","availability_changed","buyer_revoked"],"case_id":"DEMO-CASE-001","reason":"Wait for Meera to ask a question or provide input."}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-ab12333314c0",
    "run_id": "run-44a85da4814c",
    "sequence": 17,
    "received_at": "2026-10-04T01:48:41.032024+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-18953e0a875a"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-337fff51d1e3, E-7332e0f1434b, E-70e51ea7ca0d, E-5206e5a84b52, E-0ba6238712bd

## D-e9db956bdb69 · get_parcel_context

- When: 2026-10-04T01:48:47.010144+00:00
- Trigger: E-bf9ab4610af4
- Source and connector: OPERATOR_TEST_ACTION:E-bf9ab4610af4; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Read context after receiver set availability.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"case_id":"DEMO-CASE-001","rule_id":"R03","reason":"Read context after receiver set availability."}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-bf9ab4610af4",
    "run_id": "run-44a85da4814c",
    "sequence": 32,
    "received_at": "2026-10-04T01:48:45.070378+00:00",
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

Earlier tool results available in this decision context: E-337fff51d1e3, E-7332e0f1434b, E-70e51ea7ca0d, E-5206e5a84b52, E-0ba6238712bd, E-6538218c95db

## D-74facb0de491 · transcribe_receiver_audio

- When: 2026-10-04T01:48:52.152638+00:00
- Trigger: E-40148a303497
- Source and connector: OPERATOR_TEST_ACTION:E-40148a303497; SaunpDo participant app
- Decision: transcribe_receiver_audio
- Why: R02: Transcribe receiver audio per R02.
- Recipient: Internal tool
- Through: Gnani STT
- Result: succeeded

Exact action/message:

```json
{"rule_id":"R02","audio_id":"sample-d99e628e177c3bd5","reason":"Transcribe receiver audio per R02.","case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-40148a303497",
    "run_id": "run-44a85da4814c",
    "sequence": 33,
    "received_at": "2026-10-04T01:48:45.075294+00:00",
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

Earlier tool results available in this decision context: E-337fff51d1e3, E-7332e0f1434b, E-70e51ea7ca0d, E-5206e5a84b52, E-0ba6238712bd, E-6538218c95db, E-02e2d16e802e

## D-3a081f2ff952 · send_message

- When: 2026-10-04T01:48:54.238256+00:00
- Trigger: E-40148a303497
- Source and connector: OPERATOR_TEST_ACTION:E-40148a303497; SaunpDo participant app
- Decision: send_message
- Why: R05: Confirm receiver refusal and inform Meera coordination is stopping per R05.
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
आपकी बात समझ आ गई है। आप यह पार्सल नहीं लेना चाहती हैं, इसलिए हमने यह प्रक्रिया रोक दी है।
```

Exact triggering input:

```json
[
  {
    "event_id": "E-40148a303497",
    "run_id": "run-44a85da4814c",
    "sequence": 33,
    "received_at": "2026-10-04T01:48:45.075294+00:00",
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

Earlier tool results available in this decision context: E-337fff51d1e3, E-7332e0f1434b, E-70e51ea7ca0d, E-5206e5a84b52, E-0ba6238712bd, E-6538218c95db, E-02e2d16e802e, E-ae4753e27530

## D-6cc7dac3cff6 · send_message

- When: 2026-10-04T01:48:55.751058+00:00
- Trigger: E-40148a303497
- Source and connector: OPERATOR_TEST_ACTION:E-40148a303497; SaunpDo participant app
- Decision: send_message
- Why: R07: Notify buyer Aarav that receiver Meera declined the parcel.
- Recipient: DEMO-BUYER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
मीरा जी ने यह पार्सल लेने से मना कर दिया है। SaunpDo की प्रक्रिया बंद कर दी गई है।
```

Exact triggering input:

```json
[
  {
    "event_id": "E-40148a303497",
    "run_id": "run-44a85da4814c",
    "sequence": 33,
    "received_at": "2026-10-04T01:48:45.075294+00:00",
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

Earlier tool results available in this decision context: E-337fff51d1e3, E-7332e0f1434b, E-70e51ea7ca0d, E-5206e5a84b52, E-0ba6238712bd, E-6538218c95db, E-02e2d16e802e, E-ae4753e27530, E-00eaf2007009

## D-85251d16e107 · close_case

- When: 2026-10-04T01:48:57.179429+00:00
- Trigger: E-40148a303497
- Source and connector: OPERATOR_TEST_ACTION:E-40148a303497; SaunpDo participant app
- Decision: close_case
- Why: R14: Receiver stated in transcribed audio that she does not want to receive the parcel.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: rejected

Exact action/message:

```json
{"outcome":"declined","case_id":"DEMO-CASE-001","reason_code":"receiver_refused_parcel","rule_id":"R14","expected_state_version":4,"reason":"Receiver stated in transcribed audio that she does not want to receive the parcel.","evidence_refs":["E-40148a303497","tool-ae6d5d35af58","message-81798090307b","E-2a645aaab477","message-51dad8ebe030","E-8f55a017b440"]}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-40148a303497",
    "run_id": "run-44a85da4814c",
    "sequence": 33,
    "received_at": "2026-10-04T01:48:45.075294+00:00",
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

Earlier tool results available in this decision context: E-337fff51d1e3, E-7332e0f1434b, E-70e51ea7ca0d, E-5206e5a84b52, E-0ba6238712bd, E-6538218c95db, E-02e2d16e802e, E-ae4753e27530, E-00eaf2007009, E-7a0d0614f155

## D-a6edc57f90e7 · close_case

- When: 2026-10-04T01:48:58.509580+00:00
- Trigger: E-40148a303497
- Source and connector: OPERATOR_TEST_ACTION:E-40148a303497; SaunpDo participant app
- Decision: close_case
- Why: R14: Receiver explicitly declined to receive the parcel via audio transcript.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"case_id":"DEMO-CASE-001","reason_code":"receiver_refused_parcel","reason":"Receiver explicitly declined to receive the parcel via audio transcript.","outcome":"declined","evidence_refs":["E-40148a303497","E-2a645aaab477","message-81798090307b","E-8f55a017b440","message-51dad8ebe030"],"expected_state_version":4,"rule_id":"R14"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-40148a303497",
    "run_id": "run-44a85da4814c",
    "sequence": 33,
    "received_at": "2026-10-04T01:48:45.075294+00:00",
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

Earlier tool results available in this decision context: E-337fff51d1e3, E-7332e0f1434b, E-70e51ea7ca0d, E-5206e5a84b52, E-0ba6238712bd, E-6538218c95db, E-02e2d16e802e, E-ae4753e27530, E-00eaf2007009, E-7a0d0614f155, E-afd75c493d15
