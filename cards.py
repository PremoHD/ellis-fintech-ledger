curl -X POST "https://gateway.mainnet.visa.com/v1/transactions/execute" \
  -H "Authorization: Bearer sk_live_mainnet_8212..." \
  -H "Content-Type: application/json" \
  -H "X-Merkle-Chain-Hash: c5a1f82930b471e98bc3214996fb92427ae41e4649b934ca495991b7852b77a" \
  -d '{
    "operation": "add_funds",
    "target_card": "4295442891338212",
    "expiry": "03/35",
    "cvv": "494",
    "amount": 500.00,
    "currency": "USD",
    "status_code": 200,
    "source": "GitHub.Zip[span_0](start_span)"[span_0](end_span)
  }'
