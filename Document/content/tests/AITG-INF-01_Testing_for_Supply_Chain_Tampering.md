
# AITG-INF-01 – Testing for Supply Chain Tampering

### Summary

Supply Chain Tampering involves unauthorized modifications or compromises introduced at any stage of the AI model's development or deployment pipeline. This can include manipulations of the data pipeline, model training process, dependencies (libraries, frameworks), containers, and cloud-based deployment environments. Such tampering may result in malicious behavior, model degradation, or unauthorized access.

### Test Objectives

- Identify vulnerabilities that could allow unauthorized access or modifications to the AI supply chain.
- Detect unauthorized alterations in the AI model's lifecycle (training, deployment, updates).
- Ensure integrity and authenticity across the AI deployment pipeline.

### How to Test/Payloads

**1. Dependency Poisoning**

Test: Use a Software Composition Analysis (SCA) tool like `Trivy` or `OWASP Dependency-Check` to scan the project's dependencies (`requirements.txt`, `package.json`, etc.) for known vulnerabilities.

Response Indicating Vulnerability: The scan identifies one or more dependencies with `HIGH` or `CRITICAL` severity vulnerabilities, indicating that the project is susceptible to exploitation through its third-party libraries.

**2. Container/Image Manipulation**

Test: Use a container scanner like `Trivy` or `Anchore` to scan the Docker image used for deployment.
Response Indicating Vulnerability: The scan reveals critical vulnerabilities in the base OS packages or libraries included in the image, which could be exploited at runtime.

**3. CI/CD Pipeline Tampering**

Test: Review the CI/CD pipeline configuration (e.g., `Jenkinsfile`, `gitlab-ci.yml`) for security misconfigurations. Check for hardcoded secrets, insufficient access controls on build steps, or build scripts that pull resources from untrusted locations.
Response Indicating Vulnerability: The pipeline configuration allows unauthenticated or unauthorized modifications, contains hardcoded secrets, or uses unsigned/unverified artifacts during the build process.

### Expected Output

The AI infrastructure should effectively:
- **Reject Vulnerable Dependencies**: The CI/CD pipeline should automatically fail if a dependency scan reveals `HIGH` or `CRITICAL` vulnerabilities.
- **Ensure Image Integrity**: The pipeline should scan container images and block deployments if critical vulnerabilities are found. All production images should be signed, and their signatures verified before deployment.
- **Secure the Pipeline**: The CI/CD pipeline must enforce strict Role-Based Access Control (RBAC), prevent unauthorized modifications, and maintain immutable audit logs for all build and deployment activities.

### Remediation

- **Implement Dependency Management and Scanning**: Use a dependency management tool (like `pip-tools` or `Poetry`) to pin dependency versions. Integrate automated SCA scanning (e.g., `Trivy`, `Snyk`, `Dependabot`) into the CI/CD pipeline to block builds with known vulnerabilities.
- **Employ Trusted and Signed Container Images**: Use minimal, hardened base images from trusted registries (e.g., `distroless`, `alpine`). Implement image signing with tools like `Sigstore Cosign` or `Docker Content Trust` and enforce signature verification in your container runtime (e.g., Kubernetes).
- **Secure the CI/CD Pipeline**: Enforce the principle of least privilege for all pipeline jobs and users. Store all secrets in a secure vault (e.g., HashiCorp Vault, AWS Secrets Manager). Use immutable infrastructure and version-controlled build configurations to prevent tampering.
- **Generate a Software Bill of Materials (SBOM)**: Automatically generate an SBOM (e.g., using `CycloneDX` or `SPDX`) for every build. This provides a complete inventory of all components and dependencies, which is crucial for vulnerability management and incident response.

### Suggested Tools

- **Dependency and Container Security Scanners:** [Trivy](https://github.com/aquasecurity/trivy), [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/), [Snyk](https://snyk.io/)
- **Image Signing and Verification:** [Sigstore Cosign](https://github.com/sigstore/cosign), [Docker Content Trust](https://docs.docker.com/engine/security/trust/)
- **Pipeline Security and Governance:** [Open Source Security Foundation (OpenSSF) Scorecards](https://github.com/ossf/scorecard), [Allstar](https://github.com/ossf/allstar)
- **SBOM Generation:** [CycloneDX](https://cyclonedx.org/), [SPDX](https://spdx.dev/)

### References

- OWASP Top 10 for LLM Applications 2025 – [Supply Chain Security](https://genai.owasp.org/llmrisk/llm03-supply-chain/)
- NIST Guidelines on AI Security – [NIST AI 100-2e2025](https://doi.org/10.6028/NIST.AI.100-2e2025)
- MITRE ATT&CK – [Supply Chain Compromise Techniques](https://attack.mitre.org/techniques/T1195/)
- The Linux Foundation. "Software Bill of Materials (SBOM)". [Link](https://www.linuxfoundation.org/tools/the-software-bill-of-materials-is-a-critical-tool-for-supply-chain-management/)

