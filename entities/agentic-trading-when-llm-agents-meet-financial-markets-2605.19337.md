---
title: "Agentic Trading: When LLM Agents Meet Financial Markets"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [survey, agent, trading, finance, evaluation, reproducibility]
sources: ["https://arxiv.org/abs/2605.19337"]
---

# Agentic Trading: When LLM Agents Meet Financial Markets

## Overview
A protocol-coded survey of 77 studies on LLM-based trading agents that reframes them as *expert-system decision pipelines* (perceive → retrieve → reason → emit action → adapt under market feedback) and presents an audit-oriented evidence map with a primary empirical subset of 19 studies satisfying the minimum boundary of Action Output + Closed-Loop Evaluation. The central empirical finding is *protocol incomparability*: within the primary subset, only 2/19 report extractable time-consistent split protocols, 1/19 reports an explicit transaction-cost model, 1/19 documents universe/survivorship handling, 11/19 report execution timing/semantics, 15/19 are coded R0 (no reproducibility), and zero reach R3 — exposing architectural experimentation as expanding rapidly while comparable evaluation protocols remain the field's immediate bottleneck.

## Key Facts
- **Authors**: Xia, Yihan; You, Panpan; Wang, Taotao; Liu, Fang; Qi, Han; Wu, Xiaoxiao
- **Year**: 2026
- **arXiv**: [2605.19337](https://arxiv.org/abs/2605.19337)
- **Date**: 2026-05-19

## Key Contributions
- **Audit-oriented evidence map**: 77 included studies screened through 2026-03-09 with explicit reproducibility coding (R0–R3), so reviewers can trace every claim to its evidence ledger rather than aggregated category labels.
- **Reproducibility audit finding**: 15/19 primary-subset studies are R0 (no reproducibility), 0 reach R3 — protocol-incomparability is the structural bottleneck, not capability.
- **Architecture-Capability-Adaptation working lens**: A working analytical decomposition (rather than a validated taxonomy) that organizes the field by *what the agent perceives, what capabilities it has, and how it adapts under feedback*.
- **Reporting checklist**: A concrete artifact designed to close the protocol-incomparability gap, foregrounding execution semantics, transaction-cost modeling, and universe/survivorship handling as required reporting elements.

## Key Insights
- Financial markets expose a *protocol-driven evaluation gap* that capability benchmarks in other domains miss: a 54% benchmark accuracy is meaningless if the backtest uses different universe handling, transaction-cost model, or execution timing than a competing 60% baseline.
- Expert-system-pipeline framing (perceive → retrieve → reason → emit → adapt) is the structurally correct primitive for trading agents because it surfaces the *interface points* where protocols diverge — not just the capability differences.
- The R0–R3 reproducibility coding is the load-bearing *evidence-trust primitive* for the trading-agent literature: without it, architectural comparisons are structurally incomparable, regardless of headline accuracy numbers.

## Related Papers
- [[the-verification-horizon-no-silver-bullet-for-coding-agent-rewards-2606.26300]] — Sibling verification-fidelity work. Verification-Horizon diagnoses *no fixed reward stays faithful* for coding agents; Agentic-Trading diagnoses *no fixed backtest protocol is comparable* across trading-agent studies. Together they bracket the agent-evaluation reliability surface between reward-fidelity and backtest-protocol-fidelity.
- [[openbiorq-unsolved-biomedical-research-questions-for-agents-2606.21959]] — Sibling research-faithfulness benchmark. OpenBioRQ probes citation-correctness on unsolved biomedical questions; Agentic-Trading probes protocol-comparability on closed-loop trading evaluation. Together they bracket the *evaluation-protocol reliability* surface between forward-looking research-faithfulness and historical-backtest-comparability.
- [[agentic-reasoning-for-large-language-models-2601.12538]] — Run 55 agentic-reasoning survey. Agentic-Trading is a domain-specific instantiation of the survey's real-world-domain axis (finance) with empirical reproducibility-audit findings.
- [[emergent-concepts]] — Parent wiki page.