# SaunpDo decision ledger

Recorded model choices. This is a fictional order scenario; practice clicks are labelled OPERATOR_TEST_ACTION.

## D-d3c5c5adf23c · get_parcel_context

- When: 2026-10-04T01:48:17.908926+00:00
- Trigger: E-6ac596c4a2cc
- Source and connector: OPERATOR_TEST_ACTION:E-6ac596c4a2cc; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Read current case facts and enrolled participants after buyer grant
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"rule_id":"R03","case_id":"DEMO-CASE-001","reason":"Read current case facts and enrolled participants after buyer grant"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-6ac596c4a2cc",
    "run_id": "run-78e31f8d0d0a",
    "sequence": 2,
    "received_at": "2026-10-04T01:48:15.695804+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-5f973dec478d",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:48:15.695747+00:00",
        "expires_at": "2026-10-04T02:18:15.695747+00:00",
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

## D-44f3592efa2a · send_message

- When: 2026-10-04T01:48:19.401442+00:00
- Trigger: E-6ac596c4a2cc
- Source and connector: OPERATOR_TEST_ACTION:E-6ac596c4a2cc; SaunpDo participant app
- Decision: send_message
- Why: R07: Invite Meera to coordinate test parcel receipt and explain demo limitations
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
नमस्ते मीरा जी, यह एक डेमो पार्सल की जानकारी है। आरव ने आपके लिए बेडशीट का पार्सल रिसीव करने की मंज़ूरी दी है, क्या आप इसमें मदद चाहती हैं?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-6ac596c4a2cc",
    "run_id": "run-78e31f8d0d0a",
    "sequence": 2,
    "received_at": "2026-10-04T01:48:15.695804+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-5f973dec478d",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:48:15.695747+00:00",
        "expires_at": "2026-10-04T02:18:15.695747+00:00",
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

Earlier tool results available in this decision context: E-1714ddd5ead7

## D-605a3af34611 · wait_for_event

- When: 2026-10-04T01:48:20.596532+00:00
- Trigger: E-6ac596c4a2cc
- Source and connector: OPERATOR_TEST_ACTION:E-6ac596c4a2cc; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for receiver invitation response or direct input
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"event_types":["invitation_responded","receiver_audio_uploaded","receiver_text_received","buyer_revoked"],"reason":"Wait for receiver invitation response or direct input","rule_id":"R12","timeout_seconds":120,"case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-6ac596c4a2cc",
    "run_id": "run-78e31f8d0d0a",
    "sequence": 2,
    "received_at": "2026-10-04T01:48:15.695804+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-5f973dec478d",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:48:15.695747+00:00",
        "expires_at": "2026-10-04T02:18:15.695747+00:00",
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

Earlier tool results available in this decision context: E-1714ddd5ead7, E-0ed243e472e2

## D-1e37943138e2 · get_parcel_context

- When: 2026-10-04T01:48:22.372599+00:00
- Trigger: E-49e6a729ca21
- Source and connector: OPERATOR_TEST_ACTION:E-49e6a729ca21; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Check current facts after invitation acceptance
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"rule_id":"R03","reason":"Check current facts after invitation acceptance","case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-49e6a729ca21",
    "run_id": "run-78e31f8d0d0a",
    "sequence": 15,
    "received_at": "2026-10-04T01:48:19.734463+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-33e9c3126ffe"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-1714ddd5ead7, E-0ed243e472e2, E-5778b1daa3ae

## D-8087fa8f3252 · send_message

- When: 2026-10-04T01:48:23.807453+00:00
- Trigger: E-49e6a729ca21
- Source and connector: OPERATOR_TEST_ACTION:E-49e6a729ca21; SaunpDo participant app
- Decision: send_message
- Why: R06: Explain coordination mode limitations and ask if receiver has questions or is available
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
यह पार्सल प्रीपेड बेडशीट का है। डिलीवरी कंपनी अपनी प्रक्रिया से ही पार्सल देगी। क्या आप इसे लेने के लिए उपलब्ध हैं या कोई सवाल पूछना चाहती हैं?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-49e6a729ca21",
    "run_id": "run-78e31f8d0d0a",
    "sequence": 15,
    "received_at": "2026-10-04T01:48:19.734463+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-33e9c3126ffe"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-1714ddd5ead7, E-0ed243e472e2, E-5778b1daa3ae, E-5d8923f56bce

## D-9b2665f704da · wait_for_event

- When: 2026-10-04T01:48:25.126655+00:00
- Trigger: E-49e6a729ca21
- Source and connector: OPERATOR_TEST_ACTION:E-49e6a729ca21; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for receiver availability or parcel question
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"event_types":["availability_changed","receiver_audio_uploaded","receiver_text_received","buyer_revoked"],"case_id":"DEMO-CASE-001","reason":"Wait for receiver availability or parcel question","rule_id":"R12","timeout_seconds":120}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-49e6a729ca21",
    "run_id": "run-78e31f8d0d0a",
    "sequence": 15,
    "received_at": "2026-10-04T01:48:19.734463+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-33e9c3126ffe"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-1714ddd5ead7, E-0ed243e472e2, E-5778b1daa3ae, E-5d8923f56bce, E-89e4636b0b59

## D-d644eddbfbd4 · transcribe_receiver_audio

- When: 2026-10-04T01:48:27.789846+00:00
- Trigger: E-162a8a40becb
- Source and connector: OPERATOR_TEST_ACTION:E-162a8a40becb; SaunpDo participant app
- Decision: transcribe_receiver_audio
- Why: R02: Transcribe audio message from receiver Meera
- Recipient: Internal tool
- Through: Gnani STT
- Result: succeeded

Exact action/message:

```json
{"case_id":"DEMO-CASE-001","rule_id":"R02","reason":"Transcribe audio message from receiver Meera","audio_id":"sample-19a2acf29199db0c"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-162a8a40becb",
    "run_id": "run-78e31f8d0d0a",
    "sequence": 38,
    "received_at": "2026-10-04T01:48:25.800537+00:00",
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

Earlier tool results available in this decision context: E-1714ddd5ead7, E-0ed243e472e2, E-5778b1daa3ae, E-5d8923f56bce, E-89e4636b0b59, E-8116d515a24c

## D-0aa8b759c0d2 · get_parcel_context

- When: 2026-10-04T01:48:30.729351+00:00
- Trigger: E-f05b35768584
- Source and connector: OPERATOR_TEST_ACTION:E-f05b35768584; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Fetch state to confirm version and facts before answering receiver question
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason":"Fetch state to confirm version and facts before answering receiver question","case_id":"DEMO-CASE-001","rule_id":"R03"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-f05b35768584",
    "run_id": "run-78e31f8d0d0a",
    "sequence": 40,
    "received_at": "2026-10-04T01:48:25.812064+00:00",
    "event_type": "availability_changed",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "I can receive",
      "message_id": "message-63bde5659435"
    },
    "state_version_before": 3,
    "state_version_after": 4
  }
]
```

Earlier tool results available in this decision context: E-1714ddd5ead7, E-0ed243e472e2, E-5778b1daa3ae, E-5d8923f56bce, E-89e4636b0b59, E-8116d515a24c, E-6adfc90ebe2c

## D-335556a4dc34 · send_message

- When: 2026-10-04T01:48:32.493645+00:00
- Trigger: E-f05b35768584
- Source and connector: OPERATOR_TEST_ACTION:E-f05b35768584; SaunpDo participant app
- Decision: send_message
- Why: R09: Answer receiver questions regarding parcel item, payment status, and OTP policy
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
आरव का यह पार्सल मिंत्रा से बेडशीट का है और इसके पैसे पहले ही दिए जा चुके हैं। SaunpDo कभी भी आपसे OTP नहीं मांगता और डिलीवरी कंपनी अपनी सामान्य प्रक्रिया से ही पार्सल देगी।
```

Exact triggering input:

```json
[
  {
    "event_id": "E-f05b35768584",
    "run_id": "run-78e31f8d0d0a",
    "sequence": 40,
    "received_at": "2026-10-04T01:48:25.812064+00:00",
    "event_type": "availability_changed",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "I can receive",
      "message_id": "message-63bde5659435"
    },
    "state_version_before": 3,
    "state_version_after": 4
  }
]
```

Earlier tool results available in this decision context: E-1714ddd5ead7, E-0ed243e472e2, E-5778b1daa3ae, E-5d8923f56bce, E-89e4636b0b59, E-8116d515a24c, E-6adfc90ebe2c, E-e21b46d9e816

## D-00b9ba12479d · send_message

- When: 2026-10-04T01:48:33.884554+00:00
- Trigger: E-f05b35768584
- Source and connector: OPERATOR_TEST_ACTION:E-f05b35768584; SaunpDo participant app
- Decision: send_message
- Why: R07: Notify buyer about receiver coordination and explanation in coordination_only mode
- Recipient: DEMO-BUYER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
Meera was informed about your prepaid bedsheet parcel and that SaunpDo does not ask for OTP. Direct carrier release integration is unavailable in this coordination mode.
```

Exact triggering input:

```json
[
  {
    "event_id": "E-f05b35768584",
    "run_id": "run-78e31f8d0d0a",
    "sequence": 40,
    "received_at": "2026-10-04T01:48:25.812064+00:00",
    "event_type": "availability_changed",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "I can receive",
      "message_id": "message-63bde5659435"
    },
    "state_version_before": 3,
    "state_version_after": 4
  }
]
```

Earlier tool results available in this decision context: E-1714ddd5ead7, E-0ed243e472e2, E-5778b1daa3ae, E-5d8923f56bce, E-89e4636b0b59, E-8116d515a24c, E-6adfc90ebe2c, E-e21b46d9e816, E-996e8dceed79

## D-15f609391579 · close_case

- When: 2026-10-04T01:48:35.478022+00:00
- Trigger: E-f05b35768584
- Source and connector: OPERATOR_TEST_ACTION:E-f05b35768584; SaunpDo participant app
- Decision: close_case
- Why: R14: Receiver questions answered and availability coordinated; closing as unresolved since carrier release is unsupported in coordination_only mode
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"case_id":"DEMO-CASE-001","rule_id":"R14","reason_code":"carrier_delegation_unsupported","reason":"Receiver questions answered and availability coordinated; closing as unresolved since carrier release is unsupported in coordination_only mode","outcome":"unresolved","evidence_refs":["E-6ac596c4a2cc","E-49e6a729ca21","E-162a8a40becb","E-f05b35768584","E-cce770d17a92","E-faa6552a2230"],"expected_state_version":4}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-f05b35768584",
    "run_id": "run-78e31f8d0d0a",
    "sequence": 40,
    "received_at": "2026-10-04T01:48:25.812064+00:00",
    "event_type": "availability_changed",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "I can receive",
      "message_id": "message-63bde5659435"
    },
    "state_version_before": 3,
    "state_version_after": 4
  }
]
```

Earlier tool results available in this decision context: E-1714ddd5ead7, E-0ed243e472e2, E-5778b1daa3ae, E-5d8923f56bce, E-89e4636b0b59, E-8116d515a24c, E-6adfc90ebe2c, E-e21b46d9e816, E-996e8dceed79, E-7baaaf4762c5
