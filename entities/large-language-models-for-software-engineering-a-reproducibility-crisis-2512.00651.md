---
title: "Large Language Models for Software Engineering: A Reproducibility Crisis"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reproducibility, software-engineering, reproducibility-maturity-model, llm-for-se, meta-research, empirical-study]
sources: ["https://arxiv.org/abs/2512.00651"]
---

# Large Language Models for Software Engineering: A Reproducibility Crisis

## Overview
The first large-scale empirical study of reproducibility practices in LLM-for-SE research: a systematic analysis of 640 papers published 2017-2025 across premier SE/ML/NLP venues, using a seven-category smell taxonomy (Code and Execution, Data, Documentation, Environment and Tooling, Versioning, Model, Access and Legal). The paper finds persistent gaps in artifact availability, environment specification, versioning rigor, and documentation clarity despite modest improvements — and that artifact badges signal *presence* but not *execution fidelity or long-term reproducibility*. Introduces the **Reproducibility Maturity Model (RMM)** to move beyond binary artifact certification toward multi-dimensional, progressive reproducibility evaluation.

## Key Facts
- **Authors**: Siddiq, Mohammed Latif; Islam-Gomes, Arvin; Sekerak, Natalie; Santos, Joanna C. S.
- **Year**: 2026
- **arXiv**: [2512.00651](https://arxiv.org/abs/2512.00651)
- **Online date**: 2025-11-29
- **Categories**: cs.SE, cs.LG

## Key Contributions
- **First large-scale empirical study of LLM-for-SE reproducibility** — mined and analyzed 640 papers from 2017-2025 across premier venues, extracting structured metadata from publications, repositories, and documentation. Guided by four research questions on prevalence of reproducibility smells, temporal evolution, badge-reliability, and venue influence.
- **Seven-category smell taxonomy** — a structured taxonomy covering Code and Execution, Data, Documentation, Environment and Tooling, Versioning, Model, and Access and Legal smells. Manual annotation of all 640 papers + associated artifacts using the taxonomy; provides the *vocabulary* needed to discuss reproducibility rigorously in LLM-for-SE research.
- **Badge-reliability finding** — empirical evidence that artifact evaluation badges signal artifact *presence* but do not consistently guarantee execution fidelity or long-term reproducibility. This is a structural finding about how the community signals reproducibility vs how reproducibility is actually achieved.
- **Reproducibility Maturity Model (RMM)** — moves beyond binary artifact certification toward multi-dimensional, progressive evaluation of reproducibility rigor. Actionable recommendations to mitigate each smell category. RMM provides a *progression pathway* rather than a pass/fail gate.

## Why this matters for the wiki
The first **large-scale empirical reproducibility audit + Reproducibility Maturity Model for LLM-research in any domain** (specifically LLM-for-SE) in the wiki. Distinct from Run 66's [[benchmark-everything-everywhere-all-at-once-2606.06462]] (benchmark *construction* automation) — both address meta-research concerns but at different primitive-classes: reproducibility-audit (this) vs benchmark-construction (Run 66). Distinct from [[agentic-trading-when-llm-agents-meet-financial-markets-2605.19337]] (R0-R3 reproducibility audit for trading agents) — both surface reproducibility-as-audit-grade primitive, but this is a *community-wide empirical study* across 640 papers while Agentic-Trading's R0-R3 is a *protocol* for evaluating individual papers. Together they form a **reproducibility-research primitive pair**: large-scale empirical audit (this paper) + per-paper grading protocol (Agentic-Trading). The RMM is the load-bearing **multi-dimensional-maturity-model-as-progressive-evaluation primitive**: it reframes reproducibility from binary certification to multi-axis progression, structurally distinct from "open source yes/no" signals.

## Related Papers
- [[agentic-trading-when-llm-agents-meet-financial-markets-2605.19337]] — First R0-R3 reproducibility-audit protocol for deployed LLM agents; sibling reproducibility primitive but at *protocol-for-individual-paper* level (R0-R3) vs *empirical-study-of-640-papers* level (this paper). Together they form a *reproducibility-research primitive pair*: large-scale empirical audit + per-paper grading
- [[benchmark-everything-everywhere-all-at-once-2606.06462]] — Run 66's autonomous end-to-end benchmark construction; sibling meta-research primitive but at *benchmark-construction* level rather than *reproducibility-audit*. Both automate meta-research artifacts (benchmarks, audits) but for different downstream uses (evaluation vs rigor certification)
- [[counsel-a-meta-evaluation-dataset-for-agentic-tasks-2606.21627]] — Meta-evaluation dataset for agentic tasks; sibling meta-eval primitive. Counsel targets *task-success-evaluation validity*, while this paper targets *reproducibility rigor*. Together they bracket *meta-research primitive* from evaluation-validity (Counsel) to research-rigor (this paper)
- [[the-defense-trilemma-why-prompt-injection-defense-wrappers-fail-2604.06436]] — Run 70's defense trilemma; both surface impossibility-theorem-style results but at different primitive-classes: defense-trilemma for prompt-injection defense, reproducibility-maturity-model for LLM-research rigor. The structural-rigor framing is the load-bearing sibling