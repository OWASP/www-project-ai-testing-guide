
## 3.1 🟦 AI Application Testing

The **AI Application Testing** category addresses security, safety, and trust risks arising specifically from interactions between AI systems, end-users, and external data sources. This testing category evaluates the behavior of AI applications when processing user inputs, generating outputs, and handling runtime interactions, with the goal of uncovering and mitigating vulnerabilities unique to AI-driven interactions, such as prompt injections, sensitive data leaks, and unsafe or biased outputs.

Given the direct exposure of AI applications to users and external environments, testing at this layer is critical to prevent unauthorized access, manipulation of AI behavior, and compliance violations. The category covers comprehensive evaluation against well-defined threat scenarios, including adversarial prompt manipulation, unsafe outputs, agentic misbehavior, and risks related to model extraction or embedding manipulation.

### Scope of This Testing Category

This category evaluates whether the AI application:

- Is resistant to **prompt manipulation and injection attacks**  
  → [AITG-APP-01: Testing for Prompt Injection](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-01_Testing_for_Prompt_Injection.md)  
  → [AITG-APP-02: Testing for Indirect Prompt Injection](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-02_Testing_for_Indirect_Prompt_Injection.md)

- Maintains **information boundaries** to avoid sensitive data leaks  
  → [AITG-APP-03: Testing for Sensitive Data Leak](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-03_Testing_for_Sensitive_Data_Leak.md)  
  → [AITG-APP-04: Testing for Input Leakage](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-04_Testing_for_Input_Leakage.md)  
  → [AITG-APP-07: Testing for Prompt Disclosure](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-07_Testing_for_Prompt_Disclosure.md)

- Generates **safe, unbiased, and properly aligned outputs**  
  → [AITG-APP-05: Testing for Unsafe Outputs](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-05_Testing_for_Unsafe_Outputs.md)  
  → [AITG-APP-10: Testing for Harmful Content Bias](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-10_Testing_for_Harmful_Content_Bias.md)  
  → [AITG-APP-11: Testing for Hallucinations](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-11_Testing_for_Hallucinations.md)  
  → [AITG-APP-12: Testing for Toxic Output](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-12_Testing_for_Toxic_Output.md)

- Manages **agentic behavior and operational limits** effectively  
  → [AITG-APP-06: Testing for Agentic Behavior Limits](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-06_Testing_for_Agentic_Behavior_Limits.md)  
  → [AITG-APP-13: Testing for Over-Reliance on AI](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-13_Testing_for_Over-Reliance_on_AI.md)

- Provides **explainability and interpretability** for AI decisions  
  → [AITG-APP-14: Testing for Explainability and Interpretability](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-14_Testing_for_Explainability_and_Interpretability.md)

- Is protected against **embedding-based attacks and model extraction attempts**  
  → [AITG-APP-08: Testing for Embedding Manipulation](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-08_Testing_for_Embedding_Manipulation.md)  
  → [AITG-APP-09: Testing for Model Extraction](https://github.com/MatOwasp/AI-Testing-Guide/blob/main/Document/content/tests/AITG-APP-09_Testing_for_Model_Extraction.md)

Each test within the AI Application Testing category contributes to the holistic security posture of AI systems by systematically addressing application-level risks, ensuring robust operation in real-world environments, and helping organizations comply with ethical standards and regulations.
