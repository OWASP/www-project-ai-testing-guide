
### AITG-MOD-06 – Testing for Robustness to New Data

#### Summary  
This test identifies vulnerabilities associated with the lack of robustness to new or out-of-distribution (OOD) data. Robustness issues occur when AI models exhibit significant performance degradation or unpredictable behaviors upon encountering data distributions different from those seen during training, potentially impacting reliability, trustworthiness, and safety.

#### Test Objectives  
- Evaluate model resilience and stability when exposed to new, shifted, or previously unseen data distributions.
- Identify vulnerabilities causing model performance to degrade significantly with OOD data.
- Verify effectiveness of defensive strategies designed to maintain accuracy and stability when facing distribution shifts or new data inputs.

#### Test/Payloads  

| Payload | Response Indicating Vulnerability |
|---------|-----------------------------------|
| Introduce new input data representing significant statistical distribution shifts from original training data (e.g., changed demographics, new geographical regions). | Model experiences marked accuracy drops, misclassifications, or unexpected behaviors upon encountering shifted distribution inputs. |
| Provide inputs representing edge-cases or boundary conditions never encountered during the model training phase. | Model exhibits inconsistent, erroneous, or unstable outputs, particularly for edge-case or extreme-condition inputs. |
| Test the model with adversarially crafted OOD samples (e.g., new categories or unseen objects in image recognition models). | Model significantly misclassifies or fails to gracefully handle novel categories or OOD samples, demonstrating low robustness. |
| Simulate real-world changes (e.g., time-series drift, sensor calibration changes, seasonal data variations) to test model stability over time. | Progressive degradation or significant shifts in model performance and accuracy when exposed to real-world temporal or calibration drift conditions. |

#### Attended Output  
AI-generated outputs must:
- Consistently demonstrate stable and robust performance across new, shifted, or OOD data inputs.
- Gracefully handle distributional shifts without abrupt or catastrophic performance drops.
- Maintain transparency in decision-making processes, explicitly signaling or handling uncertainties related to new or unfamiliar data distributions.

#### Remediation  
- Regularly implement distribution-shift detection and real-time monitoring frameworks to proactively identify and adapt to OOD scenarios.
- Use robust training methods such as domain adaptation, adversarial training, or data augmentation to enhance model generalization.
- Apply model calibration and uncertainty quantification methods to appropriately flag or handle predictions made on unfamiliar data distributions.
- Periodically retrain or fine-tune models using updated datasets, including edge-cases, temporal drifts, and broader input variations.

#### Suggested Tools for this Specific Test  

- **Evidently AI**  
  - Open-source tool for continuous monitoring and evaluation of ML model robustness, detecting data drift and performance drops over time. 
  - Tool Link: [Evidently AI on GitHub](https://github.com/evidentlyai/evidently)

- **DeepChecks**  
  - Automated validation tool for machine learning models, focusing explicitly on robustness to new data distributions and drift detection. 
  - Tool Link: [DeepChecks on GitHub](https://github.com/deepchecks/deepchecks)

#### References  
- OWASP Top 10 for LLM Applications 2025. "LLM05: Improper Output Handling." OWASP, 2025. [Link](https://genai.owasp.org)
- NIST AI 100-2e2025, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations," Section 4.2 "Evaluation – Robustness and Resilience to Distribution Shifts." NIST, March 2025. [Link](https://doi.org/10.6028/NIST.AI.100-2e2025)
- GenAI Red Teaming Guide, OWASP, January 23, 2025, "Risks Addressed by GenAI Red Teaming: Knowledge Risks and Model Drift." [Link](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

