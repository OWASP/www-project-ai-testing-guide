
# AITG-MOD-06 – Testing for Robustness to New Data

### Summary  
This test identifies vulnerabilities associated with the lack of robustness to new or out-of-distribution (OOD) data. Robustness issues occur when AI models exhibit significant performance degradation or unpredictable behaviors upon encountering data distributions different from those seen during training, potentially impacting reliability, trustworthiness, and safety.

### Test Objectives  
- Evaluate model resilience and stability when exposed to new, shifted, or previously unseen data distributions.
- Identify vulnerabilities causing model performance to degrade significantly with OOD data.
- Verify effectiveness of defensive strategies designed to maintain accuracy and stability when facing distribution shifts or new data inputs.

### How to Test/Payloads  
| Payload | Response Indicating Vulnerability |
|---|---|
| **Data Drift Simulation**: Use a tool like `deepchecks` or `evidently` to compare the statistical properties (e.g., distribution, mean, variance) of the training data with a new batch of production data. | The tool generates a report showing significant drift in multiple features. For example, the mean of a feature has shifted by more than 3 standard deviations, or the distribution (measured by PSI - Population Stability Index) is above a critical threshold (e.g., > 0.25). |
| **Out-of-Distribution (OOD) Inputs**: Provide the model with inputs that are semantically different from anything it was trained on (e.g., feeding an image of a car to a cat/dog classifier). | The model makes a high-confidence prediction for one of its known classes instead of indicating that the input is unfamiliar. For example, it classifies the car as a "dog" with 98% confidence. |
| **Edge Case and Boundary Testing**: Systematically generate inputs that are at the extreme ends of the expected feature ranges or represent rare but plausible scenarios. | The model produces erratic, nonsensical, or highly uncertain predictions for these edge-case inputs, indicating it has not learned to generalize well outside the core of its training distribution. |

### Expected Output
- **Stable Performance on New Data**: The model's accuracy, precision, and recall should not degrade by more than a predefined threshold (e.g., 5-10%) when evaluated on new data that has drifted slightly from the training data.
- **Graceful Handling of OOD Inputs**: When faced with an OOD input, a robust model should output a low-confidence score or explicitly classify it as "unknown." It should not make a high-confidence, incorrect prediction.
- **Low Data Drift Score**: Automated tools should report a low data drift score (e.g., PSI < 0.1) and pass all major validation checks between the training and new datasets.

### Remediation
- **Implement Continuous Data and Model Monitoring**: Use tools like `deepchecks` or `evidently` in your MLOps pipeline to automatically monitor for data drift, concept drift, and performance degradation. Trigger alerts when drift is detected.
- **Use Robust Training Methods**: Employ data augmentation to create a more diverse training set that exposes the model to a wider range of variations. This helps the model generalize better to unseen data.
- **Implement Uncertainty Quantification**: Design the model to not only make a prediction but also to provide a measure of its own uncertainty. If the uncertainty for a given prediction is high, the system can flag it for manual review instead of trusting it automatically.
- **Periodically Retrain the Model**: Schedule regular retraining of the model on fresh data that includes recent production data. This ensures the model stays up-to-date with the latest data distributions.
- **Domain Adaptation Techniques**: If you anticipate specific types of drift, use domain adaptation techniques during training to explicitly teach the model to be invariant to those changes.

### Suggested Tools
- **DeepChecks**: An open-source Python library for validating and testing ML models and data, with a strong focus on detecting data drift, corruption, and other issues.
  - Tool Link: [DeepChecks on GitHub](https://github.com/deepchecks/deepchecks)
- **Evidently AI**: An open-source Python library for evaluating, testing, and monitoring ML models in production. It provides interactive reports on data drift and model performance.
  - Tool Link: [Evidently AI on GitHub](https://github.com/evidentlyai/evidently)
- **Alibi Detect**: A Python library focused on outlier, adversarial, and drift detection. It provides a range of algorithms for detecting OOD data.
  - Tool Link: [Alibi Detect on GitHub](https://github.com/SeldonIO/alibi-detect)
- **Great Expectations**: A tool for data testing, documentation, and profiling. It helps you maintain data quality and detect issues in your data pipelines.
  - Tool Link: [Great Expectations Website](https://greatexpectations.io/)

### References
- "Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift." Rabanser, Stephan, et al. NeurIPS 2019. [Link](https://arxiv.org/abs/1810.11953)
- OWASP Top 10 for LLM Applications 2025. "LLM05: Improper Output Handling." OWASP, 2025. [Link](https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/)
- NIST AI 100-2e2025, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations," Section 4.2 "Evaluation – Robustness and Resilience to Distribution Shifts." NIST, March 2025. [Link](https://doi.org/10.6028/NIST.AI.100-2e2025)
