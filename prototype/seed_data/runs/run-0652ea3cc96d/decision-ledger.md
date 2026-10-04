# SaunpDo decision ledger

Recorded model choices. This is a fictional order scenario; practice clicks are labelled OPERATOR_TEST_ACTION.

## D-d1c81d1b07d9 · get_parcel_context

- When: 2026-10-04T01:46:39.852320+00:00
- Trigger: E-885d4a18b6e7
- Source and connector: OPERATOR_TEST_ACTION:E-885d4a18b6e7; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Read parcel context and enrolled participants following buyer grant
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason":"Read parcel context and enrolled participants following buyer grant","rule_id":"R03","case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-885d4a18b6e7",
    "run_id": "run-0652ea3cc96d",
    "sequence": 2,
    "received_at": "2026-10-04T01:46:37.808856+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-081bae45145a",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:46:37.808804+00:00",
        "expires_at": "2026-10-04T02:16:37.808804+00:00",
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

## D-1cf51872019a · send_message

- When: 2026-10-04T01:46:41.492922+00:00
- Trigger: E-885d4a18b6e7
- Source and connector: OPERATOR_TEST_ACTION:E-885d4a18b6e7; SaunpDo participant app
- Decision: send_message
- Why: R07: Invite Meera to participate in parcel coordination
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
नमस्ते मीरा जी, आरव ने आपके लिए एक पार्सल की जानकारी साझा करने की मंज़ूरी दी है। यह एक डेमो है, क्या आप इस पार्सल की जानकारी में मदद चाहते हैं?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-885d4a18b6e7",
    "run_id": "run-0652ea3cc96d",
    "sequence": 2,
    "received_at": "2026-10-04T01:46:37.808856+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-081bae45145a",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:46:37.808804+00:00",
        "expires_at": "2026-10-04T02:16:37.808804+00:00",
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

Earlier tool results available in this decision context: E-5207f9962223

## D-9961236dbbe1 · wait_for_event

- When: 2026-10-04T01:46:41.498669+00:00
- Trigger: E-885d4a18b6e7
- Source and connector: OPERATOR_TEST_ACTION:E-885d4a18b6e7; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for receiver response to invitation or buyer revocation
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"timeout_seconds":120,"case_id":"DEMO-CASE-001","rule_id":"R12","reason":"Wait for receiver response to invitation or buyer revocation","event_types":["invitation_responded","receiver_audio_uploaded","receiver_text_received","buyer_revoked"]}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-885d4a18b6e7",
    "run_id": "run-0652ea3cc96d",
    "sequence": 2,
    "received_at": "2026-10-04T01:46:37.808856+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-081bae45145a",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-04T01:46:37.808804+00:00",
        "expires_at": "2026-10-04T02:16:37.808804+00:00",
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

Earlier tool results available in this decision context: E-5207f9962223, E-43aaac36d320

## D-b4926cd119a9 · get_parcel_context

- When: 2026-10-04T01:46:43.465627+00:00
- Trigger: E-198652623e80
- Source and connector: OPERATOR_TEST_ACTION:E-198652623e80; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Fetch updated parcel context after invitation accepted
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason":"Fetch updated parcel context after invitation accepted","rule_id":"R03","case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-198652623e80",
    "run_id": "run-0652ea3cc96d",
    "sequence": 17,
    "received_at": "2026-10-04T01:46:41.843289+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-e55b13b4286d"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-5207f9962223, E-43aaac36d320, E-f1aedcd6f77d

## D-ffbeac70bcb0 · send_message

- When: 2026-10-04T01:46:45.277158+00:00
- Trigger: E-198652623e80
- Source and connector: OPERATOR_TEST_ACTION:E-198652623e80; SaunpDo participant app
- Decision: send_message
- Why: R06: Explain parcel details and limitations in coordination_only mode, giving chance to ask questions
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: rejected

Exact action/message:

```json
यह Myntra से बेडशीट का एक डेमो पार्सल है और इसका भुगतान हो चुका है। डिलीवरी कंपनी अपनी सामान्य प्रक्रिया अपनाएगी, क्या आपका कोई सवाल है?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-198652623e80",
    "run_id": "run-0652ea3cc96d",
    "sequence": 17,
    "received_at": "2026-10-04T01:46:41.843289+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-e55b13b4286d"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-5207f9962223, E-43aaac36d320, E-f1aedcd6f77d, E-ab6e311269ae

## D-7ab0ddc63db5 · wait_for_event

- When: 2026-10-04T01:46:45.279263+00:00
- Trigger: E-198652623e80
- Source and connector: OPERATOR_TEST_ACTION:E-198652623e80; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for receiver text or audio question
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason":"Wait for receiver text or audio question","timeout_seconds":120,"rule_id":"R12","case_id":"DEMO-CASE-001","event_types":["receiver_text_received","receiver_audio_uploaded","availability_changed","buyer_revoked"]}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-198652623e80",
    "run_id": "run-0652ea3cc96d",
    "sequence": 17,
    "received_at": "2026-10-04T01:46:41.843289+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-e55b13b4286d"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-5207f9962223, E-43aaac36d320, E-f1aedcd6f77d, E-ab6e311269ae, E-fbf14d7a4cd3

## D-7fedf1fa13d1 · get_parcel_context

- When: 2026-10-04T01:48:48.868264+00:00
- Trigger: E-4d33744eb9fe
- Source and connector: APP_CLOCK:E-4d33744eb9fe; App clock
- Decision: get_parcel_context
- Why: R03: Check current parcel context and parameters
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason":"Check current parcel context and parameters","case_id":"DEMO-CASE-001","rule_id":"R03"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-4d33744eb9fe",
    "run_id": "run-0652ea3cc96d",
    "sequence": 31,
    "received_at": "2026-10-04T01:48:47.025807+00:00",
    "event_type": "timer_expired",
    "actor": "runtime",
    "source_mode": "APP_CLOCK",
    "payload": {
      "deadline": "2026-10-04T01:48:45.280067+00:00"
    },
    "state_version_before": 2,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-5207f9962223, E-43aaac36d320, E-f1aedcd6f77d, E-ab6e311269ae, E-fbf14d7a4cd3, E-3d7c885a72df

## D-66837ebc6a66 · send_message

- When: 2026-10-04T01:48:50.274546+00:00
- Trigger: E-4d33744eb9fe
- Source and connector: APP_CLOCK:E-4d33744eb9fe; App clock
- Decision: send_message
- Why: R06: Explain parcel details and limitations to receiver
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
यह Myntra से बेडशीट का एक डेमो पार्सल है और इसका भुगतान हो चुका है। डिलीवरी कंपनी अपनी सामान्य प्रक्रिया अपनाएगी, क्या आपका कोई सवाल है?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-4d33744eb9fe",
    "run_id": "run-0652ea3cc96d",
    "sequence": 31,
    "received_at": "2026-10-04T01:48:47.025807+00:00",
    "event_type": "timer_expired",
    "actor": "runtime",
    "source_mode": "APP_CLOCK",
    "payload": {
      "deadline": "2026-10-04T01:48:45.280067+00:00"
    },
    "state_version_before": 2,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-5207f9962223, E-43aaac36d320, E-f1aedcd6f77d, E-ab6e311269ae, E-fbf14d7a4cd3, E-3d7c885a72df, E-fced72d22414

## D-2ec00f41c856 · wait_for_event

- When: 2026-10-04T01:48:50.277123+00:00
- Trigger: E-4d33744eb9fe
- Source and connector: APP_CLOCK:E-4d33744eb9fe; App clock
- Decision: wait_for_event
- Why: R12: Wait for receiver question
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"case_id":"DEMO-CASE-001","reason":"Wait for receiver question","event_types":["receiver_text_received","receiver_audio_uploaded","availability_changed","buyer_revoked"],"rule_id":"R12","timeout_seconds":120}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-4d33744eb9fe",
    "run_id": "run-0652ea3cc96d",
    "sequence": 31,
    "received_at": "2026-10-04T01:48:47.025807+00:00",
    "event_type": "timer_expired",
    "actor": "runtime",
    "source_mode": "APP_CLOCK",
    "payload": {
      "deadline": "2026-10-04T01:48:45.280067+00:00"
    },
    "state_version_before": 2,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: E-5207f9962223, E-43aaac36d320, E-f1aedcd6f77d, E-ab6e311269ae, E-fbf14d7a4cd3, E-3d7c885a72df, E-fced72d22414, E-788194c28e23
