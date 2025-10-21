
# OWASP AI Testing Guide 
**Version 1.0 – 2025**

---

## Preface  

Artificial Intelligence is transforming how software is designed, deployed, and defended yet our ability to **test, verify, and assure AI systems** has not evolved at the same pace. Traditional application security testing is no longer sufficient for systems driven by models that learn, adapt, and behave unpredictably.  

In 2023, OWASP released the *Top 10 for Large Language Model Applications*, the first global effort to map common AI risks. The **OWASP AI Testing Guide (AITG)** takes the next step: providing a **structured, repeatable, and community-driven methodology** for evaluating the **security, safety, and trustworthiness** of AI systems across their entire lifecycle, from data collection and model training to deployment, monitoring, and runtime behavior.  

While its foundations draw on the OWASP Web Security Testing Guide (WSTG) and the NIST AI Risk Management Framework, the AITG extends beyond web or application testing. It introduces an integrated approach combining **AI red-teaming, adversarial testing, risk-based validation, and continuous assurance**, aligned with global standards such as ISO/IEC 42001, ISO/IEC 5338, NIST AI 100-2, and the EU AI Act.  

This guide is written for **security testers, ML engineers, red teamers, risk managers, and auditors** who must translate high-level AI governance principles into **practical, testable controls**. Each test case links objectives, payloads, and observable responses to remediation guidance, enabling consistent assessment and evidence-based reporting.  

**Version 1.0** introduces four testing categories that together form the OWASP AI Testing Framework:  

1️⃣ **AI Application Testing** – validating prompts, interfaces, and integrated logic.  
2️⃣ **AI Model Testing** – probing model robustness, alignment, and adversarial resistance.  
3️⃣ **AI Data Testing** – assessing data integrity, privacy, and provenance.  
4️⃣ **AI Infrastructure Testing** – evaluating pipeline, orchestration, and runtime environments.  

Each category follows a consistent process:  

> **Define Objective → Execute Test → Interpret Response → Recommend Remediation**

Rather than prescribing specific tools, the AITG defines a **standard for methodology** a common language for measuring the resilience of AI systems. The framework is designed to evolve continuously, informed by real-world testing, academic research, and community feedback.  

We would like to acknowledge the **OWASP Foundation**, the contributors of the *Top 10 for LLM Applications* and *GenAI Red Teaming Guide*, and the NIST AI RMF and AI 100-2e teams for their foundational work. Most importantly, we thank the OWASP community and practitioners who dedicate time to testing, breaking, and strengthening AI systems in the open.  

The OWASP AI Testing Guide is a **living document**. It will evolve with new research, regulatory changes, and lessons learned from field testing. We invite you to contribute through GitHub issues, pull requests, and community discussions so that together we can make **AI secure, reliable, and trustworthy by design**.  

Onward,  
**Matteo Meucci & Marco Morana**  
*Project Co-Leads, OWASP AI Testing Guide*  


# AI Testing Guide Authors and Contributors 

We would like to thank you all the people involved in the project.

Authors:
- Matteo Meucci
- Marco Morana
- Federico Dotta
- Federico Ricciuti
- Julio Araujo
- Grao Melo
- Dhanith Krishna
- Yoni Birman
- Maura Pintor
- Luca Demetrio
- Didier Durand
- Roei Arpaly
- Jeremy Redmond
- DotDotSlash
- Nicolas Humblot
- Martí Jordà Roca
- Sita Ram Sai

Contributors:
- Cecil Su 
- Melvin Tan 
- Sebastien Gioria 
- Andrea Fukushima
- Giovanni Cerrato 
- Kunal Sinha 
- Jacob Beers
- Joey Melo

Acknowledgements
We also want to thank everyone in the wider OWASP AITG community — especially those in the Slack channel — who shared feedback, ideas, or encouragement along the way. Your input helped shape this project.
