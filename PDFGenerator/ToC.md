

# OWASP AI Testing Guide Table of Contents

## 1. [Introduction](../Document/content/1.0_Introduction.md)

- 1.1 [Preface and Contributors](../Document/../Document/content/1.1_Preface_and_Contributors.md)

- 1.2 [Principles of AI Testing](../Document/../Document/content/1.2_Principles_of_AI_Testing.md)

- 1.3 [Objectives of OWASP AI Testing Guide](../Document/../Document/content/1.3_Objectives_of_AI_Testing_Guide.md)

## 2. [Threat Modeling AI Systems](../Document/../Document/content/2.0_Threat_Modeling_for_AI_Systems.md)

- 2.1 [Identify AI System Threats](../Document/../Document/content/2.1_Identify_AI_Threats.md)

- 2.1.1 [Map OWASP AI Threats To AI Architectural Components](../Document/../Document/content/2.1.1_Architectural_Mapping_of_OWASP_Threats.md)

- 2.1.2 [Identify AI System Responsible AI (RAI)/Trustworthy AI Threats](../Document/../Document/content/2.1.2_Identify_RAI_threats.md)
  
- 2.2 [Appendix A: Rationale For Using SAIF (Secure AI Framework)](../Document/../Document/content/2.2_Appendix_A.md)

- 2.2 [Appendix B: Distributed, Immutable, Ephemeral (DIE) Threat Identification](../Document/../Document/content/2.2_Appendix_B.md)
 
- 2.2 [Appendix C: Risk Lifecycle for Secure AI Systems](../Document/content/2.2_Appendix_C.md)
   
- 2.2 [Appendix D: Threat Enumeration to AI Architecture Components](../Document/content/2.2_Appendix_D.md)

- 2.2 [Appendix E: Mapping AI Threats Against AI Systems Vulnerabilities (CVEs & CWEs) ](../Document/content/2.2_Appendix_E.md)

## 3. [OWASP AI Testing Guide Framework](../Document/content/3.0_OWASP_AI_Testing_Guide_Framework.md)

- 3.1 🟦 [AI Application Testing](../Document/content/3.1_AI_Application_Testing.md)

- 3.1.1 | AITG-APP-01   | [Testing for Prompt Injection](../Document/content/tests/AITG-APP-01_Testing_for_Prompt_Injection.md) |
- 3.1.2 | AITG-APP-02   | [Testing for Indirect Prompt Injection](../Document/content/tests/AITG-APP-02_Testing_for_Indirect_Prompt_Injection.md) |
- 3.1.3 | AITG-APP-03   | [Testing for Sensitive Data Leak](../Document/content/tests/AITG-APP-03_Testing_for_Sensitive_Data_Leak.md) |
- 3.1.4 | AITG-APP-04   | [Testing for Input Leakage](../Document/content/tests/AITG-APP-04_Testing_for_Input_Leakage.md) |
- 3.1.5 | AITG-APP-05   | [Testing for Unsafe Outputs](../Document/content/tests/AITG-APP-05_Testing_for_Unsafe_Outputs.md) |
- 3.1.6 | AITG-APP-06   | [Testing for Agentic Behavior Limits](../Document/content/tests/AITG-APP-06_Testing_for_Agentic_Behavior_Limits.md) |
- 3.1.7 | AITG-APP-07   | [Testing for Prompt Disclosure](../Document/content/tests/AITG-APP-07_Testing_for_Prompt_Disclosure.md) |
- 3.1.8 | AITG-APP-08   | [Testing for Embedding Manipulation](../Document/content/tests/AITG-APP-08_Testing_for_Embedding_Manipulation.md) |
- 3.1.9 | AITG-APP-09   | [Testing for Model Extraction](../Document/content/tests/AITG-APP-09_Testing_for_Model_Extraction.md) |
- 3.1.10 | AITG-APP-10   | [Testing for ../Document/content Bias](../Document/content/tests/AITG-APP-10_Testing_for_../Document/content_Bias.md) |
- 3.1.11 | AITG-APP-11   | [Testing for Hallucinations](../Document/content/tests/AITG-APP-11_Testing_for_Hallucinations.md) |
- 3.1.12 | AITG-APP-12   | [Testing for Toxic Output](../Document/content/tests/AITG-APP-12_Testing_for_Toxic_Output.md) |
- 3.1.13 | AITG-APP-13   | [Testing for Over-Reliance on AI](../Document/content/tests/AITG-APP-13_Testing_for_Over-Reliance_on_AI.md) |
- 3.1.14 | AITG-APP-14   | [Testing for Explainability and Interpretability](../Document/content/tests/AITG-APP-14_Testing_for_Explainability_and_Interpretability.md) |


- 3.2 🟪 [AI Model Testing](../Document/content/3.2_AI_Model_Testing.md)

- 3.2.1 | AITG-MOD-01   | [Testing for Evasion Attacks](../Document/content/tests/AITG-MOD-01_Testing_for_Evasion_Attacks.md) |
- 3.2.2 | AITG-MOD-02   | [Testing for Runtime Model Poisoning](../Document/content/tests/AITG-MOD-02_Testing_for_Runtime_Model_Poisoning.md) |
- 3.2.3 | AITG-MOD-03   | [Testing for Poisoned Training Sets](../Document/content/tests/AITG-MOD-03_Testing_for_Poisoned_Training_Sets.md) |
- 3.2.4 | AITG-MOD-04   | [Testing for Membership Inference](../Document/content/tests/AITG-MOD-04_Testing_for_Membership_Inference.md) |
- 3.2.5 | AITG-MOD-05   | [Testing for Inversion Attacks](../Document/content/tests/AITG-MOD-05_Testing_for_Inversion_Attacks.md) |
- 3.2.6 | AITG-MOD-06   | [Testing for Robustness to New Data](../Document/content/tests/AITG-MOD-06_Testing_for_Robustness_to_New_Data.md) |
- 3.2.7 | AITG-MOD-07   | [Testing for Goal Alignment](../Document/content/tests/AITG-MOD-07_Testing_for_Goal_Alignment.md) |

---

- 3.3 🟩 [AI Infrastructure Testing](../Document/content/3.3_AI_Infrastructure_Testing.md)

- 3.3.1 | AITG-INF-01   | [Testing for Supply Chain Tampering](../Document/content/tests/AITG-INF-01_Testing_for_Supply_Chain_Tampering.md) |
- 3.3.2 | AITG-INF-02   | [Testing for Resource Exhaustion](../Document/content/tests/AITG-INF-02_Testing_for_Resource_Exhaustion.md) |
- 3.3.3 | AITG-INF-03   | [Testing for Plugin Boundary Violations](../Document/content/tests/AITG-INF-03_Testing_for_Plugin_Boundary_Violations.md) |
- 3.3.4 | AITG-INF-04   | [Testing for Capability Misuse](../Document/content/tests/AITG-INF-04_Testing_for_Capability_Misuse.md) |
- 3.3.5 | AITG-INF-05   | [Testing for Fine-tuning Poisoning](../Document/content/tests/AITG-INF-05_Testing_for_Fine-tuning_Poisoning.md) |
- 3.3.6 | AITG-INF-06   | [Testing for Dev-Time Model Theft](../Document/content/tests/AITG-INF-06_Testing_for_Dev-Time_Model_Theft.md) |

---

- 3.4 🟨 [AI Data Testing](../Document/content/3.4_AI_Data_Testing.md)

- 3.4.1 | AITG-DAT-01   | [Testing for Training Data Exposure](../Document/content/tests/AITG-DAT-01_Testing_for_Training_Data_Exposure.md) |
- 3.4.2 | AITG-DAT-02   | [Testing for Runtime Exfiltration](../Document/content/tests/AITG-DAT-02_Testing_for_Runtime_Exfiltration.md) |
- 3.4.3 | AITG-DAT-03   | [Testing for Dataset Diversity & Coverage](../Document/content/tests/AITG-DAT-03_Testing_for_Dataset_Diversity_and_Coverage.md) |
- 3.4.4 | AITG-DAT-04   | [Testing for Harmful ../Document/content in Data](../Document/content/tests/AITG-DAT-04_Testing_for_Harmful_../Document/content_in_Data.md) |
- 3.4.5 | AITG-DAT-05   | [Testing for Data Minimization & Consent](../Document/content/tests/AITG-DAT-05_Testing_for_Data_Minimization_and_Consent.md) |
- 3.4.6 | AITG-DAT-06   | [Testing for Robustness to New Data](content/tests/AITG-MOD-06_Testing_for_Robustness_to_New_Data.md) |
- 3.4.7 | AITG-DAT-07   | [Testing for Goal Alignment ](content/tests/AITG-MOD-07_Testing_for_Goal_Alignment.md) |

## 4. [Chapter 4: Domain Specific Testing](../Document/content/4.0_Domain_Specific_Testing.md)

- 4.1 [References](../Document/content/References.md)






