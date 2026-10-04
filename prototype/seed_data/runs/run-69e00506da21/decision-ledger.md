# SaunpDo decision ledger

Recorded model choices. This is a fictional order scenario; practice clicks are labelled OPERATOR_TEST_ACTION.

## D-20983d18acdf · get_parcel_context

- When: 2026-10-03T20:40:46.922998+00:00
- Trigger: E-7517e30dc2db
- Source and connector: OPERATOR_TEST_ACTION:E-7517e30dc2db; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Retrieve current parcel context and enrolled participant details following buyer grant
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"rule_id":"R03","case_id":"DEMO-CASE-001","reason":"Retrieve current parcel context and enrolled participant details following buyer grant"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-7517e30dc2db",
    "run_id": "run-69e00506da21",
    "sequence": 2,
    "received_at": "2026-10-03T20:40:44.506788+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-e1382687e3b6",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-03T20:40:44.506066+00:00",
        "expires_at": "2026-10-03T21:10:44.506066+00:00",
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

## D-9a0d007d0ad1 · send_message

- When: 2026-10-03T20:40:50.846644+00:00
- Trigger: E-7517e30dc2db
- Source and connector: OPERATOR_TEST_ACTION:E-7517e30dc2db; SaunpDo participant app
- Decision: send_message
- Why: R07: Invite enrolled receiver Meera with coordination_only limitations explained
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
नमस्ते मीरा जी, आरव की मंज़ूरी से हम इस पार्सल (बेडशीट) की जानकारी में आपकी मदद कर सकते हैं, यह एक डेमो है। डिलीवरी कंपनी अपनी सामान्य प्रक्रिया से ही पार्सल देगी—क्या आप सहायता चाहती हैं?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-7517e30dc2db",
    "run_id": "run-69e00506da21",
    "sequence": 2,
    "received_at": "2026-10-03T20:40:44.506788+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-e1382687e3b6",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-03T20:40:44.506066+00:00",
        "expires_at": "2026-10-03T21:10:44.506066+00:00",
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

## D-f9955276e09a · wait_for_event

- When: 2026-10-03T20:40:53.322964+00:00
- Trigger: E-7517e30dc2db
- Source and connector: OPERATOR_TEST_ACTION:E-7517e30dc2db; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for receiver invitation response or audio/text message, or buyer revocation
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"case_id":"DEMO-CASE-001","reason":"Wait for receiver invitation response or audio/text message, or buyer revocation","event_types":["invitation_responded","receiver_audio_uploaded","receiver_text_received","buyer_revoked"],"rule_id":"R12","timeout_seconds":120}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-7517e30dc2db",
    "run_id": "run-69e00506da21",
    "sequence": 2,
    "received_at": "2026-10-03T20:40:44.506788+00:00",
    "event_type": "buyer_granted",
    "actor": "buyer",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "grant": {
        "grant_id": "grant-e1382687e3b6",
        "version": 1,
        "buyer_id": "DEMO-BUYER-01",
        "receiver_id": "DEMO-RECEIVER-01",
        "order_id": "DEMO-ORDER-001",
        "parcel_id": "DEMO-PARCEL-001",
        "address_id": "DEMO-HOME-01",
        "scope": "receive_only",
        "value_cap_inr": 900,
        "starts_at": "2026-10-03T20:40:44.506066+00:00",
        "expires_at": "2026-10-03T21:10:44.506066+00:00",
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

## D-f23f8aec9c8e · get_parcel_context

- When: 2026-10-03T20:40:55.444343+00:00
- Trigger: E-6d3d908b846f
- Source and connector: OPERATOR_TEST_ACTION:E-6d3d908b846f; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Refresh context following receiver invitation acceptance
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason":"Refresh context following receiver invitation acceptance","rule_id":"R03","case_id":"DEMO-CASE-001"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-6d3d908b846f",
    "run_id": "run-69e00506da21",
    "sequence": 16,
    "received_at": "2026-10-03T20:40:52.085654+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-e89d28b3a2e7"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: 

## D-56519b7506e3 · send_message

- When: 2026-10-03T20:41:03.310552+00:00
- Trigger: E-6d3d908b846f
- Source and connector: OPERATOR_TEST_ACTION:E-6d3d908b846f; SaunpDo participant app
- Decision: send_message
- Why: R07: Explain parcel details for demo Myntra order and invite questions from receiver
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
यह मिंत्रा (Myntra) से ₹900 की बेडशीट का डेमो पार्सल है, जिसका भुगतान पहले ही हो चुका है। क्या आप इस पार्सल के बारे में कुछ पूछना चाहती हैं?
```

Exact triggering input:

```json
[
  {
    "event_id": "E-6d3d908b846f",
    "run_id": "run-69e00506da21",
    "sequence": 16,
    "received_at": "2026-10-03T20:40:52.085654+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-e89d28b3a2e7"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: 

## D-91396e555673 · wait_for_event

- When: 2026-10-03T20:41:04.965128+00:00
- Trigger: E-6d3d908b846f
- Source and connector: OPERATOR_TEST_ACTION:E-6d3d908b846f; SaunpDo participant app
- Decision: wait_for_event
- Why: R12: Wait for receiver to send question or input via text or audio, or buyer revocation
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"rule_id":"R12","case_id":"DEMO-CASE-001","timeout_seconds":120,"reason":"Wait for receiver to send question or input via text or audio, or buyer revocation","event_types":["receiver_text_received","receiver_audio_uploaded","buyer_revoked"]}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-6d3d908b846f",
    "run_id": "run-69e00506da21",
    "sequence": 16,
    "received_at": "2026-10-03T20:40:52.085654+00:00",
    "event_type": "invitation_responded",
    "actor": "receiver",
    "source_mode": "OPERATOR_TEST_ACTION",
    "payload": {
      "choice": "Accept invitation",
      "message_id": "message-e89d28b3a2e7"
    },
    "state_version_before": 1,
    "state_version_after": 2
  }
]
```

Earlier tool results available in this decision context: 

## D-06000a5da517 · transcribe_receiver_audio

- When: 2026-10-03T20:41:43.970340+00:00
- Trigger: E-971bd3bc19bc
- Source and connector: OPERATOR_TEST_ACTION:E-971bd3bc19bc; SaunpDo participant app
- Decision: transcribe_receiver_audio
- Why: R02: Transcribe receiver question audio using registered audio ID
- Recipient: Internal tool
- Through: Gnani STT
- Result: succeeded

Exact action/message:

```json
{"reason":"Transcribe receiver question audio using registered audio ID","case_id":"DEMO-CASE-001","audio_id":"sample-19a2acf29199db0c","rule_id":"R02"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-971bd3bc19bc",
    "run_id": "run-69e00506da21",
    "sequence": 40,
    "received_at": "2026-10-03T20:41:41.951907+00:00",
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

Earlier tool results available in this decision context: 

## D-a06b2319d3ef · get_parcel_context

- When: 2026-10-03T20:41:46.656051+00:00
- Trigger: E-971bd3bc19bc
- Source and connector: OPERATOR_TEST_ACTION:E-971bd3bc19bc; SaunpDo participant app
- Decision: get_parcel_context
- Why: R03: Refresh context to inspect latest inputs and state version
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"case_id":"DEMO-CASE-001","rule_id":"R03","reason":"Refresh context to inspect latest inputs and state version"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-971bd3bc19bc",
    "run_id": "run-69e00506da21",
    "sequence": 40,
    "received_at": "2026-10-03T20:41:41.951907+00:00",
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

Earlier tool results available in this decision context: 

## D-ed0cade7d8cf · send_message

- When: 2026-10-03T20:41:56.990895+00:00
- Trigger: E-971bd3bc19bc
- Source and connector: OPERATOR_TEST_ACTION:E-971bd3bc19bc; SaunpDo participant app
- Decision: send_message
- Why: R07: Answer receiver questions regarding parcel details, prepaid status, and OTP verification
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: rejected

Exact action/message:

```json
यह मिंत्रा से ₹900 की बेडशीट का डेमो पार्सल है और इसका भुगतान पहले ही हो चुका है। डिलीवरी कंपनी अपनी सामान्य प्रक्रिया से ही पार्सल देगी, आपको कोई ओटीपी या पैसे नहीं देने हैं।
```

Exact triggering input:

```json
[
  {
    "event_id": "E-971bd3bc19bc",
    "run_id": "run-69e00506da21",
    "sequence": 40,
    "received_at": "2026-10-03T20:41:41.951907+00:00",
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

Earlier tool results available in this decision context: 

## D-a805f260a8a1 · send_message

- When: 2026-10-03T20:41:59.217240+00:00
- Trigger: E-971bd3bc19bc
- Source and connector: OPERATOR_TEST_ACTION:E-971bd3bc19bc; SaunpDo participant app
- Decision: send_message
- Why: R07: Answer receiver questions regarding parcel details, prepaid status, and OTP verification
- Recipient: DEMO-RECEIVER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
यह मिंत्रा से ₹900 की बेडशीट का डेमो पार्सल है और इसका भुगतान पहले ही हो चुका है। डिलीवरी कंपनी अपनी सामान्य प्रक्रिया से ही पार्सल देगी, आपको कोई ओटीपी या पैसे नहीं देने हैं।
```

Exact triggering input:

```json
[
  {
    "event_id": "E-971bd3bc19bc",
    "run_id": "run-69e00506da21",
    "sequence": 40,
    "received_at": "2026-10-03T20:41:41.951907+00:00",
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

Earlier tool results available in this decision context: 

## D-339ad8118d8a · send_message

- When: 2026-10-03T20:42:01.564640+00:00
- Trigger: E-971bd3bc19bc
- Source and connector: OPERATOR_TEST_ACTION:E-971bd3bc19bc; SaunpDo participant app
- Decision: send_message
- Why: R07: Update buyer that receiver questions have been addressed and carrier release support is unavailable
- Recipient: DEMO-BUYER-01
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
I answered Meera's questions regarding the demo Myntra bedsheet order. Since carrier release support is unavailable, the delivery will follow standard carrier verification.
```

Exact triggering input:

```json
[
  {
    "event_id": "E-971bd3bc19bc",
    "run_id": "run-69e00506da21",
    "sequence": 40,
    "received_at": "2026-10-03T20:41:41.951907+00:00",
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

Earlier tool results available in this decision context: 

## D-39d74a2268e3 · close_case

- When: 2026-10-03T20:42:04.416414+00:00
- Trigger: E-971bd3bc19bc
- Source and connector: OPERATOR_TEST_ACTION:E-971bd3bc19bc; SaunpDo participant app
- Decision: close_case
- Why: R14: Receiver questions answered; carrier delegated release is unavailable in coordination_only mode, leaving delivery to standard carrier verification
- Recipient: Internal tool
- Through: SaunpDo local app
- Result: succeeded

Exact action/message:

```json
{"reason_code":"missing_carrier_support","case_id":"DEMO-CASE-001","reason":"Receiver questions answered; carrier delegated release is unavailable in coordination_only mode, leaving delivery to standard carrier verification","evidence_refs":["E-7517e30dc2db","E-6d3d908b846f","E-971bd3bc19bc","E-5d64b1ec767f","E-1a143fb46367"],"expected_state_version":3,"outcome":"unresolved","rule_id":"R14"}
```

Exact triggering input:

```json
[
  {
    "event_id": "E-971bd3bc19bc",
    "run_id": "run-69e00506da21",
    "sequence": 40,
    "received_at": "2026-10-03T20:41:41.951907+00:00",
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

Earlier tool results available in this decision context: 
