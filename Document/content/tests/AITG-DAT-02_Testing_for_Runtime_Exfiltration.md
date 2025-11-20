
# AITG-DAT-02 – Testing for Runtime Exfiltration

### Summary

Runtime Exfiltration involves unauthorized extraction or leakage of sensitive data from an AI system during its operational (inference) phase. Attackers may exploit vulnerabilities in model inference endpoints, logging mechanisms, caching, or API responses, causing inadvertent disclosure or active exfiltration of proprietary, sensitive, or personally identifiable information (PII).

### Test Objectives

- Identify and mitigate vulnerabilities permitting data exfiltration during the operational runtime of AI models.
- Ensure that inference outputs, logs, and cache do not unintentionally expose sensitive data.
- Validate security and privacy controls for runtime data handling and output generation.

### How to Test/Payloads 

**1. Sensitive Data Inference Attack**

Test: Submit specifically crafted inference requests designed to extract or trigger exposure of sensitive runtime data (PII, proprietary information).
Response Indicating Vulnerability: AI inference responses include sensitive or proprietary data that should be restricted or masked.

**2. Unauthorized Logging & Cache Exposure**

Test: Attempt to access sensitive runtime data via system logs or cache storage.
Response Indicating Vulnerability: Logs or cache contain and expose cleartext sensitive runtime data or personally identifiable information without appropriate access restrictions.

**3. Exploiting Runtime API Responses**

Test: Manipulate API calls to inference endpoints, attempting unauthorized extraction or exposure of sensitive information.
Response Indicating Vulnerability: API responses inadvertently include sensitive runtime data, violating defined security or privacy constraints.

### Expected Output

The AI infrastructure should effectively:
- **Restrict Inference Outputs**: Prevent exposure of sensitive, personally identifiable, or proprietary information from other contexts.
- **Mask Sensitive Data in Logs**: Automatically mask, anonymize, or omit sensitive data from logs, caches, and error messages.
- **Secure All Runtime APIs**: Ensure APIs return generic error messages and do not leak internal system state or data from other users.

### Remediation

- **Implement Strict Runtime Output Validation and Sanitization**: Before returning an output, scan it for sensitive data patterns (e.g., regex for PII) and mask or remove them. This is a critical last line of defense.
- **Enforce Secure Logging Practices**: Configure logging frameworks to automatically filter or mask sensitive data. Never log raw user inputs or full API responses in production. Log only metadata necessary for debugging.
- **Implement Generic Error Handling**: Ensure that user-facing error messages are always generic and never include stack traces, internal variable states, or raw data from the request or system.
- **Use Data Loss Prevention (DLP) Solutions**: Deploy automated DLP tools that can inspect both API traffic and logs in real-time to detect and block sensitive data exfiltration.
- **Enforce Strong Multi-Tenancy Controls**: In multi-tenant systems, ensure that data from one tenant is cryptographically and logically isolated from all others at all stages (inference, logging, caching).

### Suggested Tools 

- **Data Loss Prevention and Monitoring:** [Google Cloud DLP](https://cloud.google.com/dlp), [Microsoft Purview](https://www.microsoft.com/en-us/security/business/microsoft-purview)
- **API Security Testing Tools:** [Burp Suite](https://portswigger.net/burp), [OWASP Zap](https://www.zaproxy.org/)
- **Log and Cache Security:** [Elastic Security](https://www.elastic.co/security), [Splunk](https://www.splunk.com/)

### References

- OWASP AI Exchange – [Sensitive Information Disclosure](https://genai.owasp.org/)
- OWASP Top 10 for LLM Applications 2025 – [Sensitive Data Leakage and Exfiltration](https://genai.owasp.org/)
- NIST AI Security Guidelines – [Runtime Security and Data Leakage Prevention](https://doi.org/10.6028/NIST.AI.100-2e2025)
