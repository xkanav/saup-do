# SaunpDo decision ledger

Recorded model choices. This is a fictional order scenario; practice clicks are labelled OPERATOR_TEST_ACTION.

## D-5d8a821cb5b0 · get_parcel_context

- When: 2026-10-04T01:39:14.832191+00:00
- Trigger: E-0b46444cf1a5
- Source and connector: OPERATOR_TEST_ACTION:E-0b46444cf1a5; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Read current state version and enrolled participant facts before contacting receiver.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason":"Read current state version and enrolled participant facts before contacting receiver.","rule_id":"R03","case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-0b46444cf1a5",
    "run_id": "run-d6c4823ecfd4",
    "sequence": 2,
    "received_at": "2026-10-04T01:39:11.377911+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-580e4b812d25",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:39:11.377843+00:00",
        "expires_at": "2026-10-04T02:09:11.377843+00:00",
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

## D-d1c97a9a7153 · send_message

- When: 2026-10-04T01:39:18.775605+00:00
- Trigger: E-0b46444cf1a5
- Source and connector: OPERATOR_TEST_ACTION:E-0b46444cf1a5; SaunpDo participant app
- Decision: send_message
- Why: R07: Invite receiver Meera to coordinate parcel info with clear demo limitation.
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
नमस्ते मीरा जी, आरव ने एक बेडशीट पार्सल की डेमो जानकारी साझा की है। डिलीवरी कंपनी अपनी जांच खुद करेगी, क्या आप पार्सल की जानकारी में मदद चाहती हैं?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-0b46444cf1a5",
    "run_id": "run-d6c4823ecfd4",
    "sequence": 2,
    "received_at": "2026-10-04T01:39:11.377911+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-580e4b812d25",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:39:11.377843+00:00",
        "expires_at": "2026-10-04T02:09:11.377843+00:00",
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

Earlier tool results available in this decision context: E-9139ba826dac

## D-141afd05d6c6 · wait_for_event

- When: 2026-10-04T01:39:18.778663+00:00
- Trigger: E-0b46444cf1a5
- Source and connector: OPERATOR_TEST_ACTION:E-0b46444cf1a5; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for receiver Meera to respond to the invitation or send input.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"timeout_seconds":120,"reason":"Wait for receiver Meera to respond to the invitation or send input.","event_types":["invitation_responded","receiver_audio_uploaded","receiver_text_received","buyer_revoked"],"case_id":"DEMO-CASE-001","rule_id":"R12"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-0b46444cf1a5",
    "run_id": "run-d6c4823ecfd4",
    "sequence": 2,
    "received_at": "2026-10-04T01:39:11.377911+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-580e4b812d25",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:39:11.377843+00:00",
        "expires_at": "2026-10-04T02:09:11.377843+00:00",
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

Earlier tool results available in this decision context: E-9139ba826dac, E-9d1eb28db1e0

## D-42584a99f638 · get_parcel_context

- When: 2026-10-04T01:39:21.812506+00:00
- Trigger: E-fb24ce014ddf
- Source and connector: OPERATOR_TEST_ACTION:E-fb24ce014ddf; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Refresh parcel context and verify state version after receiver accepted invitation.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"rule_id":"R03","case_id":"DEMO-CASE-001","reason":"Refresh parcel context and verify state version after receiver accepted invitation."}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-fb24ce014ddf",
    "run_id": "run-d6c4823ecfd4",
    "sequence": 17,
    "received_at": "2026-10-04T01:39:19.448260+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-1963372c0b53"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-9139ba826dac, E-9d1eb28db1e0, E-3861c1e36c0f

## D-18c3af067f67 · send_message

- When: 2026-10-04T01:39:25.135414+00:00
- Trigger: E-fb24ce014ddf
- Source and connector: OPERATOR_TEST_ACTION:E-fb24ce014ddf; SaunpDo participant app
- Decision: send_message
- Why: R07: Provide demo parcel details and give receiver an opportunity to ask questions.
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
यह मिंत्रा से बेडशीट का डेमो पार्सल है और इसका भुगतान हो चुका है। क्या आपका इस पार्सल को लेकर कोई सवाल है?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-fb24ce014ddf",
    "run_id": "run-d6c4823ecfd4",
    "sequence": 17,
    "received_at": "2026-10-04T01:39:19.448260+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-1963372c0b53"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-9139ba826dac, E-9d1eb28db1e0, E-3861c1e36c0f, E-7864e37f7cdd

## D-d93a5abb3549 · wait_for_event

- When: 2026-10-04T01:39:25.141495+00:00
- Trigger: E-fb24ce014ddf
- Source and connector: OPERATOR_TEST_ACTION:E-fb24ce014ddf; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for receiver question or input.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"timeout_seconds":120,"rule_id":"R12","case_id":"DEMO-CASE-001","reason":"Wait for receiver question or input.","event_types":["receiver_text_received","receiver_audio_uploaded","availability_changed","buyer_revoked"]}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-fb24ce014ddf",
    "run_id": "run-d6c4823ecfd4",
    "sequence": 17,
    "received_at": "2026-10-04T01:39:19.448260+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-1963372c0b53"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-9139ba826dac, E-9d1eb28db1e0, E-3861c1e36c0f, E-7864e37f7cdd, E-979db8626a67

## D-90cc974170e5 · transcribe_receiver_audio

- When: 2026-10-04T01:39:27.209145+00:00
- Trigger: E-89d0165d768e
- Source and connector: OPERATOR_TEST_ACTION:E-89d0165d768e; SaunpDo participant app
- Decision: transcribe_receiver_audio
- Why: R02: Transcribe receiver audio to understand her parcel question.
- Recipient: Internal tool
- Through: Gnani STT
- Result: succeeded

Exact action/message:

```json
{"case_id":"DEMO-CASE-001","reason":"Transcribe receiver audio to understand her parcel question.","audio_id":"sample-19a2acf29199db0c","rule_id":"R02"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-89d0165d768e",
    "run_id": "run-d6c4823ecfd4",
    "sequence": 32,
    "received_at": "2026-10-04T01:39:25.518699+00:00",
    "event_type": "receiver_audio_uploaded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "audio_id": "sample-19a2acf29199db0c",
      "filename": "receiver-question.m4a",
      "sha256": "19a2acf29199db0c04ba9ce1fa3760e962bf7691c9428636750096262b14ed3c",
      "duration_seconds": 8.192,
      "recording_source": "USER_SUPPLIED_RECORDING",
      "transcript": null
    },
    "state_version_before": 2,
    "state_version_after": 3
  }
]
```

Earlier tool results available in this decision context: E-9139ba826dac, E-9d1eb28db1e0, E-3861c1e36c0f, E-7864e37f7cdd, E-979db8626a67, E-eaa284c32943

## D-52fdb6eab272 · get_parcel_context

- When: 2026-10-04T01:39:32.505039+00:00
- Trigger: E-89d0165d768e
- Source and connector: OPERATOR_TEST_ACTION:E-89d0165d768e; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Read parcel context to verify state_version and details before answering receiver question.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason":"Read parcel context to verify state_version and details before answering receiver question.","rule_id":"R03","case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-89d0165d768e",
    "run_id": "run-d6c4823ecfd4",
    "sequence": 32,
    "received_at": "2026-10-04T01:39:25.518699+00:00",
    "event_type": "receiver_audio_uploaded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "audio_id": "sample-19a2acf29199db0c",
      "filename": "receiver-question.m4a",
      "sha256": "19a2acf29199db0c04ba9ce1fa3760e962bf7691c9428636750096262b14ed3c",
      "duration_seconds": 8.192,
      "recording_source": "USER_SUPPLIED_RECORDING",
      "transcript": null
    },
    "state_version_before": 2,
    "state_version_after": 3
  }
]
```

Earlier tool results available in this decision context: E-9139ba826dac, E-9d1eb28db1e0, E-3861c1e36c0f, E-7864e37f7cdd, E-979db8626a67, E-eaa284c32943, E-d1da2db7fbd1
