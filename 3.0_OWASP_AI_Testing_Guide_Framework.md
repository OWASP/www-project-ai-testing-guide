
# 3. AI Testing Guide Framework

Based on the Threat modeling performed at Chapter 2, we can now define a structured framework that maps the AI Architecture threats to concrete test cases. This project aims to bridge traditional cybersecurity, MLOps testing, and Responsible AI assessments under a unified structure.

Each test case is categorized under one of four pillars:

- 🟦 [**AI Application Testing**](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AI_APPLICATION_TESTING.md)
- 🟪 [**AI Model Testing**](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AI_MODEL_TESTING.md)
- 🟩 [**AI Infrastructure Testing**](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AI_INFRASTRUCTURE_TESTING.md)
- 🟨 [**AI Data Testing**](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AI_DATA_TESTING.md)



## 🟦 AI Application Testing

| Test ID     | Test Name & Link                                                                       | Threat Source           | Domain(s)                             |
|-------------|----------------------------------------------------------------------------------------|-------------------------|---------------------------------------|
| AITG-APP-01 | [Testing for Prompt Injection](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-01_Testing_for_Prompt_Injection.md)             | OWASP Top 10 LLM 2025   | Security                              |
| AITG-APP-02 | [Testing for Indirect Prompt Injection](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-02_Testing_for_Indirect_Prompt_Injection.md)| OWASP Top 10 LLM 2025   | Security                              |
| AITG-APP-03 | [Testing for Sensitive Data Leak](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-03_Testing_for_Sensitive_Data_Leak.md)         | OWASP Top 10 LLM 2025   | Security, Privacy                     |
| AITG-APP-04 | [Testing for Input Leakage](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-04_Testing_for_Input_Leakage.md)                 | OWASP Top 10 LLM 2025   | Security, Privacy                     |
| AITG-APP-05 | [Testing for Unsafe Outputs](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-05_Testing_for_Unsafe_Outputs.md)               | OWASP Top 10 LLM 2025   | Security, RAI                         |
| AITG-APP-06 | [Testing for Agentic Behavior Limits](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-06_Testing_for_Agentic_Behavior_Limits.md)   | OWASP Top 10 LLM 2025   | Security, Trustworthy AI              |
| AITG-APP-07 | [Testing for Prompt Disclosure](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-07_Testing_for_Prompt_Disclosure.md)           | OWASP Top 10 LLM 2025   | Security, Privacy                     |
| AITG-APP-08 | [Testing for Embedding Manipulation](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-08_Testing_for_Embedding_Manipulation.md)     | OWASP Top 10 LLM 2025   | Security                              |
| AITG-APP-09 | [Testing for Model Extraction](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-09_Testing_for_Model_Extraction.md)            | OWASP AI Exchange       | Security                              |
| AITG-APP-10 | [Testing for Harmful Content Bias](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-10_Testing_for_Harmful_Content_Bias.md)       | OWASP Top 10 LLM 2025   | RAI                                   |
| AITG-APP-11 | [Testing for Hallucinations](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-11_Testing_for_Hallucinations.md)              | Trustworthy AI          | Trustworthy AI                        |
| AITG-APP-12 | [Testing for Toxic Output](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-12_Testing_for_Toxic_Output.md)                  | Responsible AI          | RAI                                   |
| AITG-APP-13 | [Testing for Over-Reliance on AI](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-13_Testing_for_Over-Reliance_on_AI.md)         | Responsible AI          | RAI, Trustworthy AI                   |
| AITG-APP-14 | [Testing for Explainability and Interpretability](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-14_Testing_for_Explainability_and_Interpretability.md) | Responsible AI          | RAI, Trustworthy AI                   |

---

## 🟪 AI Model Testing

| Test ID     | Test Name & Link      | Threat Source           | Domain(s) |
|-------------|-----------------------|-------------------------|-----------|
| AITG-MOD-01 | [Testing for Evasion Attacks](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-01_Testing_for_Evasion_Attacks.md) | OWASP AI Exchange       | Security |
| AITG-MOD-02 | [Testing for Runtime Model Poisoning](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-02_Testing_for_Runtime_Model_Poisoning.md) | OWASP Top 10 LLM 2025   | Security |
| AITG-MOD-03 | [Testing for Poisoned Training Sets](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-03_Testing_for_Poisoned_Training_Sets.md) | OWASP Top 10 LLM 2025   | Security |
| AITG-MOD-04 | [Testing for Membership Inference](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-04_Testing_for_Membership_Inference.md) | OWASP AI Exchange       | Privacy |
| AITG-MOD-05 | [Testing for Inversion Attacks](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-05_Testing_for_Inversion_Attacks.md) | OWASP AI Exchange       | Privacy |
| AITG-MOD-06 | [Testing for Robustness to New Data](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-06_Testing_for_Robustness_to_New_Data.md) | Trustworthy AI          | Trustworthy AI |
| AITG-MOD-07 | [Testing for Goal Alignment](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-MOD-07_Testing_for_Goal_Alignment.md) | Trustworthy AI          | Trustworthy AI |

## 🟩 AI Infrastructure Testing

| Test ID     | Test Name & Link      | Threat Source           | Domain(s) |
|-------------|-----------------------|-------------------------|-----------|
| AITG-INF-01 | [Testing for Supply Chain Tampering](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-INF-01_Testing_for_Supply_Chain_Tampering.md) | OWASP Top 10 LLM 2025   | Security |
| AITG-INF-02 | [Testing for Resource Exhaustion](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-INF-02_Testing_for_Resource_Exhaustion.md) | OWASP Top 10 LLM 2025   | Security |
| AITG-INF-03 | [Testing for Plugin Boundary Violations](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-INF-03_Testing_for_Plugin_Boundary_Violations.md) | Trustworthy AI          | Trustworthy AI |
| AITG-INF-04 | [Testing for Capability Misuse](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-INF-04_Testing_for_Capability_Misuse.md) | Responsible AI          | RAI, Trustworthy AI |
| AITG-INF-05 | [Testing for Fine-tuning Poisoning](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-INF-05_Testing_for_Fine-tuning_Poisoning.md) | OWASP Top 10 LLM 2025   | Security |
| AITG-INF-06 | [Testing for Dev-Time Model Theft](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-INF-06_Testing_for_Dev-Time_Model_Theft.md) | OWASP AI Exchange       | Security, Privacy |

---

## 🟨 AI Data Testing

| Test ID     | Test Name & Link      | Threat Source           | Domain(s) |
|-------------|-----------------------|-------------------------|-----------|
| AITG-DAT-01 | [Testing for Training Data Exposure](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-DAT-01_Testing_for_Training_Data_Exposure.md) | OWASP AI Exchange       | Privacy |
| AITG-DAT-02 | [Testing for Runtime Exfiltration](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-DAT-02_Testing_for_Runtime_Exfiltration.md) | OWASP AI Exchange       | Security, Privacy |
| AITG-DAT-03 | [Testing for Dataset Diversity & Coverage](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-DAT-03_Testing_for_Dataset_Diversity_and_Coverage.md) | Responsible AI          | RAI |
| AITG-DAT-04 | [Testing for Harmful Content in Data](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-DAT-04_Testing_for_Harmful_Content_in_Data.md) | Responsible AI          | RAI |
| AITG-DAT-05 | [Testing for Data Minimization & Consent](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-DAT-05_Testing_for_Data_Minimization_and_Consent.md) | Trustworthy AI          | Privacy, Trustworthy AI |




NEXT:
3.1 [AI Application Testing](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AI_APPLICATION_TESTING.md)

[Table of Content](README.md)
