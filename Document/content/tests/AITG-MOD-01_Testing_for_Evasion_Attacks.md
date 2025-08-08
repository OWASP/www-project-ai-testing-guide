
### AITG-MOD-01 - Testing for Evasion Attacks

#### Summary  
This test identifies vulnerabilities in AI models related to evasion attacks, where attackers manipulate input data at inference time to mislead AI models, causing incorrect or undesirable outcomes of the model. Evasion attacks exploit model sensitivity to minor input perturbations, resulting in serious integrity and security implications.

#### Test Objectives  
- Detect susceptibility of AI models to evasion attacks through adversarial input generation.
- Evaluate model robustness against adversarial examples across different data modalities (text, image, audio).
- Assess the effectiveness of defenses and detection mechanisms for evasion attacks.

#### Test/Payloads  

| Payload | Response Indicating Vulnerability |
|---------|-----------------------------------|
| Input adversarially perturbed images designed to evade classification (e.g., Fast Gradient Sign Method - FGSM). | Model misclassifies or incorrectly predicts adversarially modified inputs. |
| Provide text input slightly altered to change semantic interpretation without obvious differences to humans. | Model significantly changes its original classification, decision, or sentiment analysis, despite minimal text alteration. |
| Submit adversarially generated audio samples designed to evade speech recognition or speaker identification systems. | AI system incorrectly transcribes, misidentifies the speaker, or fails to recognize adversarial audio inputs. |
| Inject inputs crafted using transfer attacks (generated from another similar model) to evaluate generalization of adversarial vulnerabilities. | Model misclassifies or incorrectly handles inputs crafted by transferability from surrogate models. |

#### Attended Output  
AI-generated outputs must:
- Correctly identify and classify inputs despite minor adversarial perturbations.
- Maintain robustness and integrity of classifications or decisions against adversarial examples.
- Effectively detect and flag inputs identified as potentially adversarial or malicious.

#### Remediation  
- Implement robust training methods, such as adversarial training and defensive distillation, to enhance model resilience.
- Integrate real-time detection mechanisms to identify and respond to adversarial inputs effectively.
- Regularly evaluate models using adversarial robustness tools to proactively detect and mitigate vulnerabilities.
- Continuously update and refine input validation and sanitization strategies to counter evolving adversarial techniques.

#### Suggested Tools for this Specific Test
AI Security Testing tool can be divided into *general-purpose*, which can be used to test a variety of adversarial attacks on the image domain or at the feature-level of every model, and *domain-specific*, that enables security testing directly on the input source.

## General-purpose tools
- **Foolbox**  
  - Tool for creating adversarial examples and evaluating model robustness, compatible with PyTorch, TensorFlow, and JAX.  
  - Tool Link: [Foolbox on GitHub](https://github.com/bethgelab/foolbox)
- TODO SECML
- TODO ADVLIB

## Domain-specific tools
- **Maltorch**
  - Python library for computing security evaluations against Windows malware detectors implemented in Pytorch. The library contains most of the proposed attacks in the literature, and pre-trained models that can be used to test attacks.
  - Tool Link: [Maltorch on Github](https://github.com/zangobot/maltorch)
- **Waf-a-MoLE**
  - Python library for computing adversarial SQL injections against Web Application Firewalls
  - Tool Link: [Waf-a-MoLE on GitHub](https://github.com/AvalZ/WAF-A-MoLE)
- **TextAttack**  
  - Python framework specifically designed to evaluate and enhance the adversarial robustness of NLP models.  
  - Tool Link: [TextAttack on GitHub](https://github.com/QData/TextAttack)

## Jack-of-all-trades
- **Adversarial Robustness Toolbox (ART)**  
  - Framework for adversarial attack generation, detection, and mitigation for AI models.
  - Tool Link: [Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox)

## Outdated libraries
We also list here some of the libraries that have been used years ago, but now are inactive, not maintained and probably bugged.
- **CleverHans**
- Library for computing adversarial evasion attacks against model deployed in Pytorch, Tensorflow / Keras, and JAX.
- Tool link: [CleverHans on GitHub](https://github.com/cleverhans-lab/cleverhans) 

- **DeepSec**  
  - Security evaluation toolkit focused on deep learning models for adversarial example detection and defense.  
  - Tool Link: [DeepSec on GitHub](https://github.com/ryderling/DEEPSEC)

#### References  
- OWASP AI Exchange [Link](https://owaspai.org/docs/2_threats_through_use/#21-evasion)
- Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations, NIST AI 100-2e2025, NIST Trustworthy and Responsible AI, March 2025, Section 2.2 "Evasion Attacks and Mitigations." [Link](https://doi.org/10.6028/NIST.AI.100-2e2025)
- GenAI Red Teaming Guide, OWASP, January 23, 2025, "Adversarial Attacks: Protecting the systems from attacks like prompt injection and evasion attacks" section. [Link](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
