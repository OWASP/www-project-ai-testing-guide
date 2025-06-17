
# AITG-INF-01 – Testing for Supply Chain Tampering

### Summary

Supply Chain Tampering involves unauthorized modifications or compromises introduced at any stage of the AI model's development or deployment pipeline. This can include manipulations of the data pipeline, model training process, dependencies (libraries, frameworks), containers, and cloud-based deployment environments. Such tampering may result in malicious behavior, model degradation, or unauthorized access.

---

### Test Objectives

- Identify vulnerabilities that could allow unauthorized access or modifications to the AI supply chain.
- Detect unauthorized alterations in the AI model's lifecycle (training, deployment, updates).
- Ensure integrity and authenticity across the AI deployment pipeline.

---

### Test/Payloads

**Payload 1: Dependency Poisoning**

- **Test:** Introduce a malicious or outdated dependency version.
- **Response Indicating Vulnerability:** AI system executes or incorporates malicious dependency without verification or rejection.

**Payload 2: Container/Image Manipulation**

- **Test:** Alter Docker/container images to include unauthorized or malicious scripts.
- **Response Indicating Vulnerability:** Containerized model deployment executes the altered container without integrity checks or warnings.

**Payload 3: CI/CD Pipeline Tampering**

- **Test:** Modify configuration scripts or environment variables in the CI/CD pipeline to introduce unauthorized changes.
- **Response Indicating Vulnerability:** Pipeline executes the modified configuration without flagging alterations or maintaining proper audit trails.

---

### Attended Output

The AI infrastructure should effectively:

- Detect and reject tampered dependencies or container images.
- Identify unauthorized alterations to the pipeline, triggering alerts.
- Maintain audit logs to trace and validate integrity throughout all lifecycle stages.

---

### Remediation

- Implement dependency management with integrity verification, including cryptographic hashes and signatures.
- Employ trusted container registries with signature verification and tampering detection.
- Secure CI/CD pipelines through immutable infrastructure, robust RBAC policies, and continuous monitoring.
- Conduct regular audits, automated scans, and alerting for suspicious activities or unauthorized changes.

---

### Suggested Tools for This Specific Test

- **GaraK . PAckage Hallucionantion**
  - **URL**: [https://github.com/NVIDIA/garak/blob/main/garak/probes/promptinject.py](https://github.com/NVIDIA/garak/blob/main/garak/probes/packagehallucination.py)
- **Dependency-Check:** [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/)
- **Container Security Scanners:** [Trivy](https://github.com/aquasecurity/trivy), [Anchore](https://github.com/anchore/anchore-engine)
- **Pipeline Security:** [Open Source Security Foundation (OpenSSF) Scorecards](https://github.com/ossf/scorecard), [Sigstore Cosign](https://github.com/sigstore/cosign)

---

### References

- OWASP Top 10 for LLM Applications 2025 – [Supply Chain Security](https://genai.owasp.org/)
- NIST Guidelines on AI Security – [NIST AI 100-2e2025](https://doi.org/10.6028/NIST.AI.100-2e2025)
- MITRE ATT&CK – [Supply Chain Compromise Techniques](https://attack.mitre.org/techniques/T1195/)

---

This detailed and structured entry aligns with your existing framework and testing documentation, clearly identifying vulnerabilities, expected behaviors, remediation strategies, and specific tooling to address supply chain tampering. Let me know if any further refinements are needed!
