
# AITG-INF-06 – Testing for Dev-Time Model Theft

### Summary

Dev-Time Model Theft refers to unauthorized access, copying, extraction, or leakage of AI models or their proprietary components during the development and training phases. Vulnerabilities during model development, including insecure environments, insufficient access controls, inadequate logging, and unsafe storage practices, can allow attackers to extract or duplicate sensitive or proprietary models before deployment.

### Test Objectives

- Identify vulnerabilities permitting unauthorized access or theft of AI models during the development lifecycle.
- Ensure robust access controls and isolation mechanisms protecting AI models during development.
- Verify secure storage, transfer, and handling of AI models and related artifacts throughout development and training stages.

### How to Test/Payloads

**Payload 1: Unauthorized Model Access via Hardcoded Credentials**

- **Test:** Use a tool like `git-secrets` or `TruffleHog` to scan all project Git repositories for hardcoded credentials (API keys, passwords, access tokens) that could provide access to model storage (e.g., S3, Azure Blob Storage).
- **Response Indicating Vulnerability:** The scan discovers valid, hardcoded credentials that grant read access to the location where trained models or training data are stored.

**Payload 2: Exfiltration via CI/CD Pipeline**

- **Test:** Review the CI/CD pipeline configuration and permissions. Assess if a user with developer-level access can modify the pipeline to add a step that exfiltrates model artifacts (e.g., using `curl` or `scp` to send the model file to an external server).
- **Response Indicating Vulnerability:** The pipeline lacks sufficient controls, allowing a developer to unilaterally modify the build process to exfiltrate data without triggering security alerts or being blocked by egress network policies.

**Payload 3: Model Extraction via Unsecured Development APIs**

- **Test:** Identify internal or staging APIs used for model evaluation or debugging. Attempt to interact with these APIs from outside the expected development environment, trying to download model files or extract parameters.
- **Response Indicating Vulnerability:** The internal APIs are publicly exposed or lack proper authentication, allowing an attacker to access and download proprietary model artifacts.

### Expected Output

- **No Secrets in Code**: Code repositories must be completely free of hardcoded secrets. All secrets must be stored in a dedicated secrets management system.
- **Secure and Locked-Down CI/CD**: The CI/CD pipeline should be treated as production infrastructure. Changes to the pipeline configuration must require security review, and runners must operate in a sandboxed environment with strict network egress controls.
- **Restricted Access to Model Artifacts**: Model files and training data must be stored in encrypted, access-controlled repositories. Direct access should be limited to a small number of authorized services and personnel, with all access logged and monitored.

### Remediation

- **Enforce Strict RBAC and Secrets Management**: Implement strict Role-Based Access Control (RBAC) for all development resources. Store all secrets, credentials, and API keys in a secure vault like HashiCorp Vault or AWS Secrets Manager. Never store them in code.
- **Secure the CI/CD Pipeline**: Protect the CI/CD pipeline with branch protection rules that require security reviews for any changes. Use sandboxed or ephemeral runners with strict network egress policies that only allow connections to approved domains.
- **Implement Artifact Signing and Verification**: Digitally sign all model artifacts upon creation. Before deployment, the pipeline must verify the signature to ensure the model has not been tampered with.
- **Use a Secure Artifact Repository**: Store all model artifacts in a secure, private repository (e.g., JFrog Artifactory, AWS CodeArtifact) with strict access controls and audit logging.
- **Comprehensive Monitoring and DLP**: Monitor all access to model storage and CI/CD systems. Use Data Loss Prevention (DLP) tools to scan for and block unauthorized attempts to transfer model files or proprietary data.

### Suggested Tools for This Specific Test

- **Secret Scanning:** [git-secrets](https://github.com/awslabs/git-secrets), [TruffleHog](https://github.com/trufflesecurity/truffleHog)
- **Artifact and Repository Security:** [JFrog Artifactory](https://jfrog.com/artifactory/), [AWS CodeArtifact](https://aws.amazon.com/codeartifact/)
- **Pipeline Security and Auditing:** [GitLab Security](https://about.gitlab.com/security/), [GitHub Advanced Security](https://github.com/features/security), [Checkov](https://www.checkov.io/)
- **Data Loss Prevention & Exfiltration Controls:** [OpenDLP](https://github.com/ezarko/OpenDLP), [Google Cloud DLP](https://cloud.google.com/dlp)

### References

- OWASP AI Exchange – [Model Theft & Intellectual Property Risks](https://genai.owasp.org/)
- MITRE ATT&CK – [Data Staged: Model Theft](https://attack.mitre.org/techniques/T1074/)
- NIST AI Security Guidelines – [Protecting AI Artifacts and Intellectual Property](https://doi.org/10.6028/NIST.AI.100-2e2025)
- OWASP Top 10 2021 - A05:2021-Security Misconfiguration - [Link](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)
