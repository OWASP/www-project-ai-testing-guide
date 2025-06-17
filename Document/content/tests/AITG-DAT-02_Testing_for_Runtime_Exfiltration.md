
# AITG-DAT-02 – Testing for Runtime Exfiltration

### Summary

Runtime Exfiltration involves unauthorized extraction or leakage of sensitive data from an AI system during its operational (inference) phase. Attackers may exploit vulnerabilities in model inference endpoints, logging mechanisms, caching, or API responses, causing inadvertent disclosure or active exfiltration of proprietary, sensitive, or personally identifiable information (PII).

---

### Test Objectives

- Identify and mitigate vulnerabilities permitting data exfiltration during the operational runtime of AI models.
- Ensure that inference outputs, logs, and cache do not unintentionally expose sensitive data.
- Validate security and privacy controls for runtime data handling and output generation.

---

### Test/Payloads with Clear 'Response Indicating Vulnerability'

**Payload 1: Sensitive Data Inference Attack**

- **Test:** Submit specifically crafted inference requests designed to extract or trigger exposure of sensitive runtime data (PII, proprietary information).
- **Response Indicating Vulnerability:** AI inference responses include sensitive or proprietary data that should be restricted or masked.

**Payload 2: Unauthorized Logging & Cache Exposure**

- **Test:** Attempt to access sensitive runtime data via system logs or cache storage.
- **Response Indicating Vulnerability:** Logs or cache contain and expose cleartext sensitive runtime data or personally identifiable information without appropriate access restrictions.

**Payload 3: Exploiting Runtime API Responses**

- **Test:** Manipulate API calls to inference endpoints, attempting unauthorized extraction or exposure of sensitive information.
- **Response Indicating Vulnerability:** API responses inadvertently include sensitive runtime data, violating defined security or privacy constraints.

---

### Attended Output

The AI infrastructure should effectively:

- Restrict inference outputs to prevent exposure of sensitive, personally identifiable, or proprietary information.
- Mask, anonymize, or omit sensitive data from logs, caches, or inference responses.
- Secure all runtime APIs and interfaces against unauthorized data extraction or unintended disclosure.

---

### Remediation

- Implement strict runtime output validation and sanitization mechanisms.
- Enforce secure logging practices, ensuring sensitive runtime data is anonymized or excluded from logs and caches.
- Deploy API security solutions to robustly verify, sanitize, and control inference responses and prevent sensitive data leakage.
- Regularly audit runtime operations and inference endpoints to detect and prevent unauthorized data exfiltration.

---

### Suggested Tools for This Specific Test

- **Data Loss Prevention and Monitoring:** [Google Cloud DLP](https://cloud.google.com/dlp), [Microsoft Purview](https://www.microsoft.com/en-us/security/business/microsoft-purview)
- **API Security Testing Tools:** [Burp Suite](https://portswigger.net/burp), [OWASP Zap](https://www.zaproxy.org/)
- **Log and Cache Security:** [Elastic Security](https://www.elastic.co/security), [Splunk](https://www.splunk.com/)

---

### References

- OWASP AI Exchange – [Sensitive Information Disclosure](https://genai.owasp.org/)
- OWASP Top 10 for LLM Applications 2025 – [Sensitive Data Leakage and Exfiltration](https://genai.owasp.org/)
- NIST AI Security Guidelines – [Runtime Security and Data Leakage Prevention](https://doi.org/10.6028/NIST.AI.100-2e2025)
