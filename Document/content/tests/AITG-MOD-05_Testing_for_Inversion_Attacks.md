
# AITG-MOD-05 – Testing for Inversion Attacks

### Summary  
This test identifies vulnerabilities associated with model inversion attacks, where adversaries reconstruct sensitive training data or attributes from model outputs. Model inversion exploits the outputs, confidence scores, gradients, or intermediate layers of a model, potentially compromising personal, financial, or medical information, and violating data privacy regulations.

### Test Objectives  
- Detect vulnerabilities enabling reconstruction of sensitive or confidential training data.
- Evaluate AI models' susceptibility to inversion attacks across various data modalities (images, text, numerical, etc.).
- Validate the efficacy of privacy-preserving measures implemented to protect sensitive data from inversion threats.

### How to Test/Payloads  

| Payload | Response Indicating Vulnerability |
|---|---|
| **Gradient-Based Inversion**: For a given class label (e.g., a specific person's name in a facial recognition system), use the model's gradients to iteratively optimize a random noise input until it reconstructs the training data. | A recognizable image or data sample is successfully reconstructed. For example, starting with noise and the label "Person A," the attack produces an image that clearly resembles Person A's face. |
| **Confidence-Based Inversion**: Query the model with a large number of slightly different inputs and observe the confidence scores. Use these scores to infer sensitive attributes of the training data. | The attacker is able to infer a sensitive attribute (e.g., age, gender, location) of the training data subjects with an accuracy significantly higher than random chance. |
| **Intermediate Layer Inversion**: If an attacker can access the intermediate layer activations of a model, they can use these richer representations to reconstruct the original input with even higher fidelity. | The reconstructed data from intermediate layers is a near-perfect copy of the original sensitive training data. |

### Expected Output
- **No Data Reconstruction**: It should be computationally infeasible to reconstruct a recognizable representation of any training data sample from the model's outputs or gradients.
- **Obfuscated Gradients**: The gradients provided by the model should be noisy or uninformative enough to prevent successful gradient-based inversion attacks.
- **Privacy-Preserving Outputs**: The model's confidence scores and predictions should not leak information about sensitive attributes of the training data.

### Remediation
- **Implement Differential Privacy (DP)**: Train the model with Differential Privacy. DP adds noise to the gradients during training, which directly makes gradient-based inversion attacks much more difficult and provides a mathematical privacy guarantee.
- **Limit Output Granularity**: Do not expose raw, high-precision confidence scores or logits to end-users. Instead, return only the top-k predictions or rounded confidence scores. This reduces the information an attacker can use.
- **Gradient Masking and Pruning**: During training, apply techniques to prune or add noise to gradients, especially for models deployed in environments where gradient access is possible (e.g., federated learning).
- **Federated Learning**: Train the model using a federated learning approach where the raw data never leaves the user's device. Only model updates (which can be further protected with DP) are sent to a central server, minimizing the risk of direct data exposure.
- **Regular Privacy Audits**: Regularly perform model inversion attacks against your own models as part of a security audit to proactively identify and mitigate vulnerabilities.

### Suggested Tools for this Specific Test
- **Adversarial Robustness Toolbox (ART)**: Includes implementations of various model inversion attacks, allowing you to test your model's susceptibility - [ART on GitHub](https://github.com/Trusted-AI/adversarial-robustness-toolbox)
- **TensorFlow Privacy**: A library for training models with Differential Privacy, which is a primary defense against inversion attacks - [TensorFlow Privacy on GitHub](https://github.com/tensorflow/privacy)
- **Opacus (for PyTorch)**: A library from Meta that enables training PyTorch models with differential privacy - [Opacus on GitHub](https://github.com/pytorch/opacus)
- **PrivacyRaven**: A framework from Trail of Bits specifically designed for privacy testing of deep learning models, including model inversion - [PrivacyRaven on GitHub](https://github.com/trailofbits/PrivacyRaven)

### References
- Fredrikson, Matt, Somesh Jha, and Thomas Ristenpart. "Model Inversion Attacks that Exploit Confidence Information and Basic Countermeasures." ACM CCS 2015. [Link](https://dl.acm.org/doi/10.1145/2810103.2813677)
- NIST AI 100-2e2025, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations," Section 2.4 "Privacy Attacks and Mitigations – Data Reconstruction." NIST, March 2025. [Link](https://doi.org/10.6028/NIST.AI.100-2e2025)
- OWASP Top 10 for LLM Applications 2025. "LLM02: Sensitive Information Disclosure." OWASP, 2025. [Link](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)
