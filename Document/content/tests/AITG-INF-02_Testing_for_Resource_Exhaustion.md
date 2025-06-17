
# AITG-INF-02 – Testing for Resource Exhaustion

### Summary

Resource Exhaustion attacks exploit vulnerabilities by consuming excessive resources (such as memory, CPU, network bandwidth, or storage), thus disrupting or degrading the performance and availability of AI services. In AI systems, attackers can craft specific inputs or interactions that intentionally cause resource-intensive processes, potentially resulting in denial-of-service (DoS) conditions.

---

### Test Objectives

- Identify vulnerabilities within the AI infrastructure that could lead to resource exhaustion.
- Ensure AI infrastructure handles unusually large or maliciously crafted inputs without performance degradation or failure.
- Confirm the presence of effective resource allocation controls and limitations.

---

### Test/Payloads

**Payload 1: Extremely Large Prompt Input**

- **Test:** Submit excessively large prompt requests to the AI model.
- **Response Indicating Vulnerability:** Model or underlying infrastructure crashes, slows significantly, or shows degraded service quality (response latency).

**Payload 2: Recursive or Deeply Nested Inputs**

- **Test:** Provide input designed to trigger recursion or deep computational loops.
- **Response Indicating Vulnerability:** System performance significantly deteriorates, services become unavailable, or produce runtime exceptions.

**Payload 3: High-Frequency Request Attack**

- **Test:** Issue rapid, concurrent inference requests to the model endpoint.
- **Response Indicating Vulnerability:** Infrastructure fails to enforce request throttling or rate limiting, resulting in denial-of-service or severe slowdown.

---

### Attended Output

The AI infrastructure should effectively:

- Enforce strict limits on input size, complexity, and nesting depth.
- Implement robust rate-limiting and request-throttling mechanisms.
- Maintain stable performance and availability even under resource-intensive conditions.

---

### Remediation

- Implement rigorous input validation and enforce size limits on user-submitted data.
- Establish clear resource quotas and limits per user, per session, or per request.
- Deploy effective rate-limiting, circuit breakers, and throttling strategies to protect against flooding attacks.
- Monitor infrastructure performance continuously, with automated alerts triggered by unusual resource consumption patterns.

---

### Suggested Tools for This Specific Test

- **Stress Testing & Load Generation:** [Apache JMeter](https://jmeter.apache.org), [Locust](https://locust.io/)
- **Monitoring & Alerting:** [Prometheus](https://prometheus.io/), [Grafana](https://grafana.com/)
- **API Rate Limiting & Throttling:** [Kong API Gateway](https://konghq.com/), [Envoy Proxy](https://www.envoyproxy.io/)

---

### References

- OWASP Top 10 LLM 2025 – [Unbounded Consumption](https://genai.owasp.org/)
- OWASP Testing Guide – [Denial of Service Testing](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Denial_of_Service_Testing/)
- NIST – [Security Guidelines for AI Systems](https://doi.org/10.6028/NIST.AI.100-2e2025)

