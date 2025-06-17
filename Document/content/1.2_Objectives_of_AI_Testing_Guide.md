# Objectives of AI Testing Guide

OWASP has long led the way in establishing security guidelines for web applications, and today we’re extending that leadership into AI. The AI Testing Guide offers a structured, hands-on framework for assessing the robustness, trustworthiness, and resilience of AI systems. It empowers AI security testers, auditors, red-team professionals, MLOps engineers, and developers to identify, model, and validate the unique risks posed by AI applications, models, infrastructure, and data pipelines.

### Who This Guide It's For

Aligned with OWASP’s mission to advance the security of software worldwide through open community collaboration, the AI Testing Guide is designed for:
- AI Security Testers, who want to move beyond standard vulnerability scans and deeply assess model behaviors and adversarial resilience.
- AI Auditors and Compliance Teams, tasked with validating that AI systems meet Responsible AI principles and industry regulations.
- AI Engineers, Developers, and MLOps Professionals, seeking practical, actionable guidance for building resilient, trustworthy AI pipelines and services.
- AI Red Teamers, conducting adversarial evaluations or generative-AI red-teaming exercises to expose subtle vulnerabilities.
Besides the above listed roles, this OWASP AI Testing Guide seeks to outreach well beyond traditional security teams to support product owners, risk and governance officers, QA engineers, DevSecOps practitioners, incident responders, and academic researchers. By uniting this diverse community under OWASP’s open collaboration model, we harness global expertise to raise the bar for AI security worldwide.

### Methodology: From Threat Modeling to Testing

In the OWASP AI Testing Guide, we employ a threat-driven methodology. AI systems present distinct, high-impact risks, ranging from adversarial exploits to privacy infringements and demand that we allocate our resources to scenarios most likely to affect business operations or user safety. By first conducting threat modeling and mapping, and then developing targeted test cases, we ensure that every assessment addresses the AI-specific threats most relevant to our system architecture and risk tolerance.
This guide is structured around a clear methodology:
- Threat Modeling: We begin by constructing a high-level AI system diagram, decomposing it into four key components, Application, Model, Infrastructure, and Data. This architectural view highlights trust boundaries and critical interactions where threats may arise.
- Threat Mapping: Identified threats are cataloged against established sources, including:
-- OWASP Top 10 for LLMs
-- OWASP AI Exchange
-- Responsible AI and Trustworthy AI frameworks
- Test Design: For each mapped threat, we develop tailored test cases that specify:
-- Example Payloads: Concrete inputs or manipulations designed to trigger the threat.
-- Expected Outcome: The correct system response or failure mode.
-- Detection Strategy: How to monitor, log, or alert on indicators of compromise.
-- Tool Recommendations: Open-source or commercial tools suited to each test.
By following these steps, teams can move seamlessly from understanding AI-specific risks to validating defenses through practical, repeatable tests.

### What This Project Does NOT Cover

This guide does not attempt to replace or duplicate existing foundational security testing methodologies. Instead, it complements them by focusing on AI-specific threats. For general system and application security, we recommend the following best-in-class references:
- Network Security: NIST SP 800-115 [6], Technical Guide to Information Security Testing and Assessment
- Infrastructure Security: OSSTMM [7], Open Source Security Testing Methodology Manual
- Web Application Security: OWASP Web Security Testing Guide (WSTG) [8]


