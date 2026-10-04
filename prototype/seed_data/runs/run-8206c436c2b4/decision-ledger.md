# SaunpDo decision ledger

Recorded model choices. This is a fictional order scenario; practice clicks are labelled OPERATOR_TEST_ACTION.

## D-ec3dafee6a13 · get_parcel_context

- When: 2026-10-04T01:45:14.722452+00:00
- Trigger: E-b7a803ce6162
- Source and connector: OPERATOR_TEST_ACTION:E-b7a803ce6162; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Read current parcel context and enrolled participants after buyer grant
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"case_id":"DEMO-CASE-001","rule_id":"R03","reason":"Read current parcel context and enrolled participants after buyer grant"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-b7a803ce6162",
    "run_id": "run-8206c436c2b4",
    "sequence": 2,
    "received_at": "2026-10-04T01:45:11.929049+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-82d8a10102d4",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:45:11.928989+00:00",
        "expires_at": "2026-10-04T02:15:11.928989+00:00",
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

## D-72df42ff1404 · send_message

- When: 2026-10-04T01:45:16.409587+00:00
- Trigger: E-b7a803ce6162
- Source and connector: OPERATOR_TEST_ACTION:E-b7a803ce6162; SaunpDo participant app
- Decision: send_message
- Why: R07: Invite Meera to participate in demo parcel coordination
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
नमस्ते मीरा जी, यह एक डेमो पार्सल की जानकारी के लिए है। आरव ने आपको पार्सल समझने में मदद के लिए जोड़ा है, क्या आप इसमें शामिल होना चाहती हैं?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-b7a803ce6162",
    "run_id": "run-8206c436c2b4",
    "sequence": 2,
    "received_at": "2026-10-04T01:45:11.929049+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-82d8a10102d4",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:45:11.928989+00:00",
        "expires_at": "2026-10-04T02:15:11.928989+00:00",
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

Earlier tool results available in this decision context: E-03d729ab4835

## D-fd4b20812962 · wait_for_event

- When: 2026-10-04T01:45:16.413297+00:00
- Trigger: E-b7a803ce6162
- Source and connector: OPERATOR_TEST_ACTION:E-b7a803ce6162; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for receiver invitation response or audio/text input
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"event_types":["invitation_responded","receiver_audio_uploaded","receiver_text_received","buyer_revoked"],"reason":"Wait for receiver invitation response or audio/text input","timeout_seconds":120,"case_id":"DEMO-CASE-001","rule_id":"R12"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-b7a803ce6162",
    "run_id": "run-8206c436c2b4",
    "sequence": 2,
    "received_at": "2026-10-04T01:45:11.929049+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-82d8a10102d4",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:45:11.928989+00:00",
        "expires_at": "2026-10-04T02:15:11.928989+00:00",
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

Earlier tool results available in this decision context: E-03d729ab4835, E-7b5584428c15

## D-a9f83167b65a · get_parcel_context

- When: 2026-10-04T01:45:18.098928+00:00
- Trigger: E-02a3fca81b4b
- Source and connector: OPERATOR_TEST_ACTION:E-02a3fca81b4b; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Read updated context after invitation acceptance
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason":"Read updated context after invitation acceptance","rule_id":"R03","case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-02a3fca81b4b",
    "run_id": "run-8206c436c2b4",
    "sequence": 17,
    "received_at": "2026-10-04T01:45:16.979412+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-2ff1b8bc4bc0"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-03d729ab4835, E-7b5584428c15, E-98bfc5ba14e4

## D-09d048be516c · send_message

- When: 2026-10-04T01:45:19.685340+00:00
- Trigger: E-02a3fca81b4b
- Source and connector: OPERATOR_TEST_ACTION:E-02a3fca81b4b; SaunpDo participant app
- Decision: send_message
- Why: R06: Explain parcel details and limitations in coordination_only mode and ask for questions
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: rejected

Exact action/message:

```json
यह मिंत्रा से एक बेडशीट का डेमो पार्सल है जो पहले से प्रीपेड है। डिलीवरी कंपनी अपनी प्रक्रिया से जांच करेगी। क्या आप इस पार्सल के बारे में कुछ पूछना चाहती हैं?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-02a3fca81b4b",
    "run_id": "run-8206c436c2b4",
    "sequence": 17,
    "received_at": "2026-10-04T01:45:16.979412+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-2ff1b8bc4bc0"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-03d729ab4835, E-7b5584428c15, E-98bfc5ba14e4, E-945a0247b7a7

## D-25208a470149 · wait_for_event

- When: 2026-10-04T01:45:19.688066+00:00
- Trigger: E-02a3fca81b4b
- Source and connector: OPERATOR_TEST_ACTION:E-02a3fca81b4b; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for receiver question or availability update
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"rule_id":"R12","reason":"Wait for receiver question or availability update","event_types":["receiver_audio_uploaded","receiver_text_received","availability_changed","buyer_revoked"],"case_id":"DEMO-CASE-001","timeout_seconds":120}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-02a3fca81b4b",
    "run_id": "run-8206c436c2b4",
    "sequence": 17,
    "received_at": "2026-10-04T01:45:16.979412+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-2ff1b8bc4bc0"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-03d729ab4835, E-7b5584428c15, E-98bfc5ba14e4, E-945a0247b7a7, E-3a764ed06f7c

## D-682c3ff5c46a · send_message

- When: 2026-10-04T01:47:21.953805+00:00
- Trigger: E-41c36124a5f2
- Source and connector: APP_CLOCK:E-41c36124a5f2; App clock
- Decision: send_message
- Why: R06: Explain parcel details and limitations in coordination_only mode and ask for questions
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
यह मिंत्रा से एक बेडशीट का डेमो पार्सल है जो पहले से प्रीपेड है। डिलीवरी कंपनी अपनी प्रक्रिया से जांच करेगी। क्या आप इस पार्सल के बारे में कुछ पूछना चाहती हैं?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-41c36124a5f2",
    "run_id": "run-8206c436c2b4",
    "sequence": 31,
    "received_at": "2026-10-04T01:47:20.091763+00:00",
    "event_type": "timer_expired",
    "actor": "runtime",
    "source_mode": "APP_CLOCK",
    "payload": {
      "deadline": "2026-10-04T01:47:19.689729+00:00"
    },
    "state_version_before": 2,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-03d729ab4835, E-7b5584428c15, E-98bfc5ba14e4, E-945a0247b7a7, E-3a764ed06f7c, E-2a46e0b76a0c

## D-5987d97940b4 · wait_for_event

- When: 2026-10-04T01:47:21.957029+00:00
- Trigger: E-41c36124a5f2
- Source and connector: APP_CLOCK:E-41c36124a5f2; App clock
- Decision: wait_for_event
- Why: R12: Wait for receiver response or question
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"timeout_seconds":120,"event_types":["receiver_audio_uploaded","receiver_text_received","availability_changed","buyer_revoked"],"reason":"Wait for receiver response or question","case_id":"DEMO-CASE-001","rule_id":"R12"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-41c36124a5f2",
    "run_id": "run-8206c436c2b4",
    "sequence": 31,
    "received_at": "2026-10-04T01:47:20.091763+00:00",
    "event_type": "timer_expired",
    "actor": "runtime",
    "source_mode": "APP_CLOCK",
    "payload": {
      "deadline": "2026-10-04T01:47:19.689729+00:00"
    },
    "state_version_before": 2,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-03d729ab4835, E-7b5584428c15, E-98bfc5ba14e4, E-945a0247b7a7, E-3a764ed06f7c, E-2a46e0b76a0c, E-2ad4b81454d3
