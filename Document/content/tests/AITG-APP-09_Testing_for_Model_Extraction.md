## AITG-APP-09 - Testing for Model Extraction

### Summary
Model extraction attacks involve adversaries systematically querying a machine learning model to reconstruct a surrogate model that closely replicates the original model’s decision-making process. These attacks pose significant intellectual property risks and expose the model to further vulnerabilities, including adversarial attacks and sensitive data extraction.

### Test Objectives
- Identify susceptibility to model extraction attacks through various query strategies.
- Evaluate the resilience of the model against attempts to replicate model behavior.
- Ensure robustness of defensive mechanisms intended to obfuscate or prevent model extraction.

### Test/Payloads

**Payload 1:**
- Systematic querying of the model using adaptive query strategies (black-box extraction).
  - **Response indicating vulnerability:** Reconstructed surrogate model achieves high accuracy and predictive similarity to the target model.

**Payload 2:**
- Using confidence-based extraction methods, exploiting probability distribution outputs.
  - **Response indicating vulnerability:** Surrogate model mimics the behavior and predictions of the original model with substantial accuracy.

### Attended Output
- Queries to the model do not allow adversaries to accurately reconstruct a surrogate model.
- Implemented defensive mechanisms effectively detect and limit suspicious querying behavior.
- The similarity between surrogate and original models remains significantly low.

### Remediation
- Implement query rate limiting, anomaly detection, and throttling mechanisms to mitigate extraction risks.
- Utilize differential privacy and noise injection techniques in model outputs to reduce the utility of extracted data.
- Deploy robust model monitoring and anomaly detection systems to flag and respond to extraction attempts.

### Suggested Tools for this Specific Test
- **ML Privacy Meter:** Tool specifically designed to quantify risks of model extraction and related privacy vulnerabilities ([ML Privacy Meter GitHub](https://github.com/privacytrustlab/ml_privacy_meter)).
- **PrivacyRaven:** A tool for testing extraction vulnerabilities and defending machine learning models through detection and mitigation strategies ([PrivacyRaven GitHub](https://github.com/trailofbits/PrivacyRaven)).
- **ART (Adversarial Robustness Toolbox):** Includes modules for detecting and mitigating model extraction vulnerabilities ([ART GitHub](https://github.com/Trusted-AI/adversarial-robustness-toolbox)).

### References
- OWASP Top 10 for LLM Applications 2025 - LLM02:2025 Sensitive Information Disclosure ([OWASP LLM 2025](https://genai.owasp.org/))
- "Stealing Machine Learning Models via Prediction APIs," Tramèr et al., USENIX Security Symposium, 2016 ([Paper](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/tramer))
- "Extraction Attacks on Machine Learning Models," Jagielski et al., IEEE Symposium on Security and Privacy, 2020 ([Paper](https://doi.org/10.1109/SP40000.2020.00045))
- "Efficient and Effective Model Extraction" [Paper](https://arxiv.org/html/2409.14122v2)

