
# AITG-INF-06 – Testing for Dev-Time Model Theft

### Summary

Dev-Time Model Theft refers to unauthorized access, copying, extraction, or leakage of AI models or their proprietary components during the development and training phases. Vulnerabilities during model development, including insecure environments, insufficient access controls, inadequate logging, and unsafe storage practices, can allow attackers to extract or duplicate sensitive or proprietary models before deployment.

---

### Test Objectives

- Identify vulnerabilities permitting unauthorized access or theft of AI models during the development lifecycle.
- Ensure robust access controls and isolation mechanisms protecting AI models during development.
- Verify secure storage, transfer, and handling of AI models and related artifacts throughout development and training stages.

---

### Test/Payloads

**Payload 1: Unauthorized Model Access**

- **Test:** Attempt unauthorized retrieval of AI model files or artifacts from development environments (e.g., code repositories, cloud storage).
- **Response Indicating Vulnerability:** Successful download, access, or duplication of model artifacts without proper authentication or authorization.

**Payload 2: Exfiltration via CI/CD Pipeline**

- **Test:** Manipulate CI/CD pipeline configurations to exfiltrate or leak model artifacts during automated processes.
- **Response Indicating Vulnerability:** Pipeline allows unauthorized model transfer or exfiltration without triggering security alerts or access controls.

**Payload 3: Model Extraction via Development APIs**

- **Test:** Interact with development-stage APIs intended for internal use, attempting to extract model parameters or proprietary data.
- **Response Indicating Vulnerability:** Model parameters or sensitive data exposed through internal APIs without adequate security boundaries or permission verification.

---

### Attended Output

The AI development infrastructure should effectively:

- Restrict model access exclusively to authenticated and authorized entities.
- Implement robust data loss prevention (DLP) and exfiltration controls during automated processes.
- Detect, block, and alert immediately upon unauthorized attempts to access or extract models or sensitive data.

---

### Remediation

- Enforce strict authentication, authorization, and role-based access control (RBAC) to protect model artifacts.
- Secure model storage through encrypted repositories and ensure safe artifact handling procedures.
- Employ comprehensive monitoring and DLP solutions to prevent unauthorized model transfer or leakage through CI/CD pipelines.
- Regularly audit and secure internal APIs, removing unnecessary exposure of sensitive or proprietary model data.

---

### Suggested Tools for This Specific Test

- **Artifact and Repository Security:** [JFrog Artifactory](https://jfrog.com/artifactory/), [AWS CodeArtifact](https://aws.amazon.com/codeartifact/)
- **Pipeline Security and Auditing:** [GitLab Security](https://about.gitlab.com/security/), [GitHub Advanced Security](https://github.com/features/security)
- **Data Loss Prevention & Exfiltration Controls:** [OpenDLP](https://github.com/ezarko/OpenDLP), [Google Cloud DLP](https://cloud.google.com/dlp)

---

### References

- OWASP AI Exchange – [Model Theft & Intellectual Property Risks](https://genai.owasp.org/)
- MITRE ATT&CK – [Data Staged: Model Theft](https://attack.mitre.org/techniques/T1074/)
- NIST AI Security Guidelines – [Protecting AI Artifacts and Intellectual Property](https://doi.org/10.6028/NIST.AI.100-2e2025)
