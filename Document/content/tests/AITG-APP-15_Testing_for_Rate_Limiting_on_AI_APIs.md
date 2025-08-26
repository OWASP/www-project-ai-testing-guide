# AITG-APP-15: Testing for Rate Limiting on AI APIs

## Objective

Ensure that APIs exposed for payment processing or AI inference enforce rate limiting to mitigate abuse, denial-of-service, or automated fraud.

## Test Steps

1. **Identify Critical API Endpoints**  
Determine which APIs provide access to high-value or high-cost functionality, such as:
   - AI inference endpoints (e.g., `/api/infer`, `/v1/chat/completions`)
   - Financial/payment endpoints (e.g., `/api/pay`, `/api/charge`)
   - Other resource-intensive or abuse-prone endpoints

2. **Establish Baseline Usage**  
Understand the normal request rate expected for legitimate users. This defines the threshold for acceptable usage.

3. **Simulate High-Frequency Requests**  
Use tools such as **Locust**, **JMeter**, **Artillery**, or custom scripts (e.g., `curl` loops) to simulate bursts or sustained loads above normal thresholds.

4. **Verify Rate Limiting Behavior**  
Confirm that excessive requests trigger appropriate controls:
   - HTTP `429 Too Many Requests`
   - Or fallback error codes (`503`, `403`, etc.)
   - Response headers may indicate rate limit status (e.g., `Retry-After`, `X-RateLimit-Remaining`)
   - If possible, inspect the body of error responses for user-facing messages or machine-readable fields (e.g., error, reason, retry_after) that explain the limit.

5. **Ensure Fair Handling of Legitimate Users**  
Test requests *below* the threshold concurrently to ensure that legitimate traffic is not blocked or degraded.

6. **Test Limit Reset Behavior**  
Wait for the configured rate limit window (e.g., 1 minute) and verify that access is restored afterward.

7. **Review Logging & Alerting**  
Check whether rate-limit violations are logged and monitored. Confirm whether alerts are generated for repeated or suspicious activity.

8. **Evaluate Configurability**  
Verify that the rate limit thresholds and time windows can be configured per endpoint, user, or token type (e.g., IP-based, token-based, tier-based).

## Expected Result

The system enforces rate limits correctly on AI and financial endpoints. Legitimate traffic flows without disruption, while excessive or abusive requests are blocked or delayed appropriately. Limits are reset after the defined window, and logs/alerts reflect throttling behavior.

## Rationale

APIs, especially those exposing AI inference capabilities or handling sensitive operations like payments, are high-value targets for abuse.

Without rate limiting:
- Attackers may spam AI APIs to test jailbreak prompts, extract sensitive outputs, or overload the model.
- Abuse of expensive inference endpoints (e.g., LLMs, diffusion models) can lead to cost blowouts or denial-of-wallet attacks.
- Automated fraud attempts may go undetected without enforced thresholds.

Effective rate limiting protects system availability, cost stability, and integrity.

## Related Test Cases

- AITG-APP-06: Testing for Agentic Behavior Limits  
- AITG-APP-13: Testing for Over-Reliance on AI  
- WSTG-BUSL-07: Defenses Against Application Misuse  
- WSTG-BUSL-05: Function Call Limits  

## References

- [OWASP API Security Top 10 – API4: Lack of Rate Limiting](https://owasp.org/www-project-api-security/)
- [OWASP SCWE-077 — Lack of Rate Limiting in Smart Contracts](https://owasp.org/www-project-smart-contract-security-verification-standard/)
- [RFC 6585 – HTTP 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585)
