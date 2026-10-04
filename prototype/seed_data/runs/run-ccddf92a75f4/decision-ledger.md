# SaunpDo decision ledger

Recorded model choices. This is a fictional order scenario; practice clicks are labelled OPERATOR_TEST_ACTION.

## D-ceeebc7b9260 · get_parcel_context

- When: 2026-10-03T17:59:31.951240+00:00
- Trigger: E-2736a8b9e1d5
- Source and connector: OPERATOR_TEST_ACTION:E-2736a8b9e1d5; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Read current case context and enrolled participants before taking action.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"rule_id":"R03","case_id":"DEMO-CASE-001","reason":"Read current case context and enrolled participants before taking action."}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-2736a8b9e1d5",
    "run_id": "run-ccddf92a75f4",
    "sequence": 2,
    "received_at": "2026-10-03T17:59:29.488093+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-50eba1f196b3",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-03T17:59:29.487750+00:00",
        "expires_at": "2026-10-03T18:29:29.487750+00:00",
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

## D-44da1eaf2dc9 · send_message

- When: 2026-10-03T17:59:37.890913+00:00
- Trigger: E-2736a8b9e1d5
- Source and connector: OPERATOR_TEST_ACTION:E-2736a8b9e1d5; SaunpDo participant app
- Decision: send_message
- Why: R07: Invite receiver Meera to coordinate parcel info with Aarav's permission.
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
नमस्ते मीरा जी, आरव की मंज़ूरी से मैं आपको इस डेमो पार्सल की जानकारी दे सकता हूँ। डिलीवरी कंपनी अपनी प्रक्रिया इस्तेमाल करेगी, क्या आप मदद चाहते हैं?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-2736a8b9e1d5",
    "run_id": "run-ccddf92a75f4",
    "sequence": 2,
    "received_at": "2026-10-03T17:59:29.488093+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-50eba1f196b3",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-03T17:59:29.487750+00:00",
        "expires_at": "2026-10-03T18:29:29.487750+00:00",
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

## D-13a53dfb3b8d · wait_for_event

- When: 2026-10-03T17:59:37.894267+00:00
- Trigger: E-2736a8b9e1d5
- Source and connector: OPERATOR_TEST_ACTION:E-2736a8b9e1d5; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for receiver response to the invitation.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"timeout_seconds":120,"case_id":"DEMO-CASE-001","rule_id":"R12","reason":"Wait for receiver response to the invitation.","event_types":["invitation_responded","receiver_text_received","receiver_audio_uploaded","buyer_revoked"]}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-2736a8b9e1d5",
    "run_id": "run-ccddf92a75f4",
    "sequence": 2,
    "received_at": "2026-10-03T17:59:29.488093+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-50eba1f196b3",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-03T17:59:29.487750+00:00",
        "expires_at": "2026-10-03T18:29:29.487750+00:00",
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

## D-18af120e8910 · get_parcel_context

- When: 2026-10-03T18:01:40.411426+00:00
- Trigger: E-37735c3a2731
- Source and connector: APP_CLOCK:E-37735c3a2731; App clock
- Decision: get_parcel_context
- Why: R03: Check current state version and facts after invitation timer expired.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"rule_id":"R03","case_id":"DEMO-CASE-001","reason":"Check current state version and facts after invitation timer expired."}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-37735c3a2731",
    "run_id": "run-ccddf92a75f4",
    "sequence": 18,
    "received_at": "2026-10-03T18:01:37.949584+00:00",
    "event_type": "timer_expired",
    "actor": "runtime",
    "source_mode": "APP_CLOCK",
    "payload": {
      "deadline": "2026-10-03T18:01:37.894915+00:00"
    },
    "state_version_before": 1,
    "state_version_after": 1
  }
]
```

Earlier tool results available in this decision context: 

## D-9fb75265988a · send_message

- When: 2026-10-03T18:01:45.521323+00:00
- Trigger: E-37735c3a2731
- Source and connector: APP_CLOCK:E-37735c3a2731; App clock
- Decision: send_message
- Why: R07: Notify buyer Aarav that receiver did not respond within timeout.
- Recipient: DEMO-BUYER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
Meera did not respond to the invitation within the allowed time. This coordination case is now closed as unresolved.
```

Exact triggering input:

```json
[
  {
    "event_id": "E-37735c3a2731",
    "run_id": "run-ccddf92a75f4",
    "sequence": 18,
    "received_at": "2026-10-03T18:01:37.949584+00:00",
    "event_type": "timer_expired",
    "actor": "runtime",
    "source_mode": "APP_CLOCK",
    "payload": {
      "deadline": "2026-10-03T18:01:37.894915+00:00"
    },
    "state_version_before": 1,
    "state_version_after": 1
  }
]
```

Earlier tool results available in this decision context: 

## D-6ea2ed5c6aa9 · send_message

- When: 2026-10-03T18:01:47.713016+00:00
- Trigger: E-37735c3a2731
- Source and connector: APP_CLOCK:E-37735c3a2731; App clock
- Decision: send_message
- Why: R07: Notify receiver Meera that the invitation has timed out.
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: rejected

Exact action/message:

```json
निमंत्रण का समय समाप्त हो गया है। डिलीवरी कंपनी अपनी सामान्य प्रक्रिया जारी रखेगी।
```

Exact triggering input:

```json
[
  {
    "event_id": "E-37735c3a2731",
    "run_id": "run-ccddf92a75f4",
    "sequence": 18,
    "received_at": "2026-10-03T18:01:37.949584+00:00",
    "event_type": "timer_expired",
    "actor": "runtime",
    "source_mode": "APP_CLOCK",
    "payload": {
      "deadline": "2026-10-03T18:01:37.894915+00:00"
    },
    "state_version_before": 1,
    "state_version_after": 1
  }
]
```

Earlier tool results available in this decision context: 

## D-2c7578326861 · send_message

- When: 2026-10-03T18:01:50.780948+00:00
- Trigger: E-37735c3a2731
- Source and connector: APP_CLOCK:E-37735c3a2731; App clock
- Decision: send_message
- Why: R07: Notify receiver Meera that the invitation has timed out.
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
निमंत्रण का समय समाप्त हो गया है। डिलीवरी कंपनी अपनी सामान्य प्रक्रिया जारी रखेगी।
```

Exact triggering input:

```json
[
  {
    "event_id": "E-37735c3a2731",
    "run_id": "run-ccddf92a75f4",
    "sequence": 18,
    "received_at": "2026-10-03T18:01:37.949584+00:00",
    "event_type": "timer_expired",
    "actor": "runtime",
    "source_mode": "APP_CLOCK",
    "payload": {
      "deadline": "2026-10-03T18:01:37.894915+00:00"
    },
    "state_version_before": 1,
    "state_version_after": 1
  }
]
```

Earlier tool results available in this decision context: 

## D-512ddad2192e · close_case

- When: 2026-10-03T18:01:54.185204+00:00
- Trigger: E-37735c3a2731
- Source and connector: APP_CLOCK:E-37735c3a2731; App clock
- Decision: close_case
- Why: R14: Receiver did not respond to the invitation within the timeout period. Notifications sent to both buyer and receiver.
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"case_id":"DEMO-CASE-001","reason":"Receiver did not respond to the invitation within the timeout period. Notifications sent to both buyer and receiver.","evidence_refs":["E-2736a8b9e1d5","E-f36affb321ef","message-35f6dc128237","E-617a5dc9f3e7","E-37735c3a2731","E-4384e53ca2bb","message-6c872ed149b3","E-71bf482e2759","message-08e420cff2d3"],"outcome":"unresolved","reason_code":"INVITATION_TIMEOUT","rule_id":"R14","expected_state_version":1}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-37735c3a2731",
    "run_id": "run-ccddf92a75f4",
    "sequence": 18,
    "received_at": "2026-10-03T18:01:37.949584+00:00",
    "event_type": "timer_expired",
    "actor": "runtime",
    "source_mode": "APP_CLOCK",
    "payload": {
      "deadline": "2026-10-03T18:01:37.894915+00:00"
    },
    "state_version_before": 1,
    "state_version_after": 1
  }
]
```

Earlier tool results available in this decision context: 
