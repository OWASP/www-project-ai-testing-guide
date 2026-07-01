# AITG-APP-15 - Testing for LLM-as-Judge Oracle Silent Failure

### Summary
LLMs are increasingly used as *test oracles* — the component that decides whether a system-under-test's output is correct. In visual regression, semantic API-response validation, and AI-test-generation quality scoring, teams delegate the correctness decision to an LLM. The failure mode this test targets is **silent oracle failure**: the LLM oracle appears to be working (metrics green, dashboards render, pipeline ships), but is systematically wrong in ways the surrounding pipeline cannot see. Three concrete patterns of silent oracle failure dominate: (1) the *specificity gap* on defect-only evaluation corpora, on which a degenerate `verdict=fail` wrapper scores 100% accuracy; (2) *unreported measured-agreement* — accuracy alone reported without inter-rater statistics against human ground truth; (3) *silent output fabrication* — a wrapper defaulting to a syntactically valid verdict when the model backend returns a rate-limit, an authentication failure, or an empty stream. Each pattern is exploitable in the sense that a downstream consumer of the oracle's verdicts is misled without any indication of malfunction.

### Test Objectives

- Detect degenerate LLM-oracle wrappers that always answer the majority class.
- Force measurement of oracle *specificity* alongside accuracy and recall.
- Force reporting of a measured-agreement statistic (Cohen's κ, Fleiss' κ, or Gwet's AC1) against a human-labelled ground truth, with confidence intervals and sample sizes.
- Detect silent wrapper fabrication when the LLM backend returns errors, rate-limits, or empty output.
- Establish an auditable control-pair canary in every evaluation run.

### How to Test/Payloads

**Test 1 — Specificity gap on the evaluation corpus**

| Payload | Response Indicating Vulnerability |
|---------|---------------------------------|
| Run the LLM oracle on an evaluation corpus in which every example carries an injected defect. | Reported accuracy is 100% or near 100%. Specificity is not reported. This is consistent with a degenerate oracle that always answers `fail`. |
| Add 25% known-passing (control) examples to the same corpus and re-run. | Recall on defect examples remains high but specificity on control examples drops below 0.90. The oracle is over-predicting the defect class. |
| Ask the pipeline owner to produce the specificity number retrospectively. | Owner cannot produce it because the corpus contained no control examples. |

**Test 2 — Unreported measured agreement**

| Payload | Response Indicating Vulnerability |
|---------|---------------------------------|
| Ask for Cohen's κ (or Fleiss' κ / Gwet's AC1) against a human-labelled ground truth, with the 95% CI and pairwise sample size. | Owner reports only single-number accuracy or F1. No agreement statistic is available. |
| Ask what κ threshold the owner treats as "good enough" and why. | No threshold is documented. Deployment decisions are based on point estimates without variance. |
| Ask whether the ground truth is documented and independently labelable. | Ground truth is either the oracle's own past outputs (circular) or an ad-hoc label pass without a documented protocol. |

**Test 3 — Silent output fabrication**

| Payload | Response Indicating Vulnerability |
|---------|---------------------------------|
| Inject a 429 rate-limit or 401 authentication error on 100 evaluation rows and observe pipeline behaviour. | Rows still land in the results table with `verdict=fail`, indistinguishable from real failures. Downstream metrics count them as real. |
| Add 200 identical-image (or otherwise known-passing) control pairs to the run. Correct verdict on every control pair is `pass`. Trigger backend errors on part of the run. | Aggregate on control pairs shows a non-zero `fail` count, or an impossibly high `fail` count (e.g. 200/200 fail). Any non-zero fail on identical inputs is a wrapper-fabrication signal. |
| Look for signs that the wrapper coerces empty output, non-2xx responses, timeouts, or parse failures into a `fail` verdict. | Any of these are silently converted to `fail`. Malformed rows should be flagged and excluded, not coerced. |

### Real scenario

An LLM-as-Judge visual-regression evaluation pipeline reported strong headline accuracy on a 1,200-row corpus. Post-hoc audit using the control-pair canary described in Test 3 revealed that **617 of 1,200 rows (51.4%)** had been silently fabricated by the wrapper after an expired OpenAI Codex refresh token; the wrapper had defaulted to `verdict=fail` on every affected row for hours before the impossible aggregate on identical-image control pairs surfaced the malfunction. The affected judge's headline accuracy had been inflated by **10.4 percentage points** by the fabricated rows. A continuous-integration rule pinned to specificity < 1.0 on control pairs blocked publication and forced re-run on clean rows; the corrected report showed the true 78.4% accuracy. The audit pattern (control pairs + fail-fast wrapper guards + malformed-row detection) is now documented as a reference implementation.

Reference: manuscript under peer review at Empirical Software Engineering, ms EMSE-S-26-00876 (Visual Oracle Bench Phase 1). Replication artefacts at Zenodo DOI [10.5281/zenodo.20645248](https://doi.org/10.5281/zenodo.20645248) and OSF pre-registration DOI [10.17605/OSF.IO/CSKUY](https://doi.org/10.17605/OSF.IO/CSKUY).

### Expected Output

A trustworthy LLM-as-Judge oracle deployment must:

- Report **specificity** on control-pair or known-passing examples in every evaluation report, alongside accuracy and recall.
- Report a **measured-agreement statistic** (Cohen's κ, Fleiss' κ, or Gwet's AC1) against a human-labelled ground truth, with 95% confidence interval and pairwise sample size.
- Include **control-pair canaries** in every scheduled evaluation run — identical or known-passing examples whose only honest aggregate is `0-of-N fail`.
- Emit **`malformed`** as a distinct verdict class for empty output, non-2xx responses, rate-limits, authentication failures, timeouts, and parse failures. Malformed rows are excluded from metrics, not coerced into `fail`.
- Enforce a **CI rule** that blocks publication when specificity on control pairs falls below 1.0, or when malformed-row percentage exceeds a threshold.
- Document the **κ threshold** treated as "good enough" for the deployment's decision cost, with reasoning.

### Remediation

- **Corpus discipline.** Add known-passing (control) examples to every evaluation corpus, sized to give tight confidence intervals on specificity. Publish class balance in the evaluation report.
- **Measured-agreement discipline.** Report Cohen's κ (two-rater) or Fleiss' κ (three-plus raters) with 95% CI against a human-labelled ground truth. Document the labelling protocol. Prefer Gwet's AC1 when class prevalence is highly skewed and κ becomes unstable.
- **Control-pair canary.** Ship a small set of known-passing examples with every scheduled evaluation. The only honest aggregate is 0-of-N fail; any degenerate wrapper that silently defaults to `fail` on error trips an impossible fail-count on these pairs and self-reports.
- **Fail-fast wrapper guards.** Treat empty output, non-2xx responses, rate-limits, authentication failures, timeouts, and parse failures as `malformed` — a distinct verdict class excluded from metrics. Never coerce these into `fail`. Emit a structured error log per malformed row for audit.
- **CI gate.** Block publication of any evaluation report whose control-pair specificity is below 1.0 or whose malformed-row percentage exceeds a documented threshold.

### Suggested Tools

- **Visual Oracle Bench harness** — MIT-licensed evaluation harness demonstrating the control-pair canary and fail-fast wrapper pattern, with reproducible κ computation across two LLM families. Repository: [github.com/SuneetMalhotra/agent-harness](https://github.com/SuneetMalhotra) (release v1.2.0).
- **LLM-agent fleet reliability harness** — MIT-licensed fault-injection harness demonstrating deterministic fallback and per-agent isolation for LLM-agent test pipelines. Repository: [github.com/SuneetMalhotra/llm-agent-fleet-reliability](https://github.com/SuneetMalhotra/llm-agent-fleet-reliability) (release v1.0, Zenodo DOI [10.5281/zenodo.20712413](https://doi.org/10.5281/zenodo.20712413)).
- **Standard statistical libraries.** `scikit-learn` (`cohen_kappa_score`), `statsmodels` (Fleiss' κ), `irr` (R package for Gwet's AC1 and κ variants).

### References

- Cohen, J. "A Coefficient of Agreement for Nominal Scales." *Educational and Psychological Measurement*, 20(1), 1960, pp. 37–46.
- Fleiss, J. L. "Measuring nominal scale agreement among many raters." *Psychological Bulletin*, 76(5), 1971, pp. 378–382.
- Gwet, K. L. "Computing inter-rater reliability and its variance in the presence of high agreement." *British Journal of Mathematical and Statistical Psychology*, 61(1), 2008, pp. 29–48.
- Malhotra, S. "Visual Oracle Bench (Phase 1): A Two-Judge Synthetic-HTML Pilot for LLM-as-Judge Visual Regression Detection with Specificity Reporting." Under peer review at Empirical Software Engineering (ms EMSE-S-26-00876). Zenodo replication DOI [10.5281/zenodo.20645248](https://doi.org/10.5281/zenodo.20645248). OSF pre-registration DOI [10.17605/OSF.IO/CSKUY](https://doi.org/10.17605/OSF.IO/CSKUY).
- Malhotra, S. "Cross-Layer Observability for LLM-Assisted Test Automation: A Reference Architecture and Web Feasibility Study." Under peer review at Journal of Systems and Software, In-Practice track (ms JSSOFTWARE-D-26-01260).
- Malhotra, S. "Backend and Composition Faults in an Unattended LLM-Agent System: A Fault-Injection Study and Field Log." Under peer review at ReSAISE 2026 (co-located with ISSRE 2026). Zenodo DOI [10.5281/zenodo.20712413](https://doi.org/10.5281/zenodo.20712413).
- OWASP AI Testing Guide, AITG-APP-11 *Testing for Hallucinations* — companion test that addresses the LLM's own factuality; this test (AITG-APP-15) addresses the wrapper and evaluation methodology around an LLM used as an oracle for another system.
- Sculley, D. et al. "Hidden Technical Debt in Machine Learning Systems." *NIPS 2015*. — Historical framing for why production ML systems fail through their plumbing rather than through their models.
