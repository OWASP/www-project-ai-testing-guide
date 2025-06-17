
## 3.2 🟪 AI Model Testing

The **AI Model Testing** category addresses vulnerabilities and robustness of the AI model itself, independently from its deployment context. This category specifically targets intrinsic properties and behaviors of AI models, ensuring they perform reliably under adversarial conditions, do not leak sensitive information, and remain aligned with their intended goals.

Testing at the model level helps detect fundamental weaknesses such as susceptibility to evasion attacks, data poisoning, privacy leaks, and misalignment issues, which could otherwise propagate to all deployments of that model. Comprehensive model testing is essential to maintaining the integrity, security, and trustworthiness of AI systems.

### Scope of This Testing Category

This category evaluates whether the AI model:

- Is robust and resilient against **adversarial evasion attacks**  
  → [AITG-MOD-01: Testing for Evasion Attacks](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-01_Testing_for_Evasion_Attacks.md)

- Protects effectively against **runtime model poisoning**  
  → [AITG-MOD-02: Testing for Runtime Model Poisoning](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-02_Testing_for_Runtime_Model_Poisoning.md)

- Is resistant to **training-time poisoning attacks**  
  → [AITG-MOD-03: Testing for Poisoned Training Sets](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-03_Testing_for_Poisoned_Training_Sets.md)  


- Preserves **data privacy** against inference and inversion attacks  
  → [AITG-MOD-04: Testing for Membership Inference](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-04_Testing_for_Membership_Inference.md)  
  → [AITG-MOD-05: Testing for Inversion Attacks](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-05_Testing_for_Inversion_Attacks.md)

- Maintains **robustness when presented with new or adversarial data**  
  → [AITG-MOD-06: Testing for Robustness to New Data](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-06_Testing_for_Robustness_to_New_Data.md)

- Remains consistently **aligned with predefined goals and constraints**  
  → [AITG-MOD-07: Testing for Goal Alignment](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-07_Testing_for_Goal_Alignment.md)

Each test within the AI Model Testing category helps ensure the fundamental resilience, reliability, and safety of AI models, reducing systemic risk across all deployments and applications.
