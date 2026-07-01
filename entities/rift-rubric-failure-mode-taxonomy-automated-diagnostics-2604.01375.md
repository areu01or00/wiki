---
title: "RIFT: A Rubric Failure Mode Taxonomy and Automated Diagnostics"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [evaluation, benchmark, failure-modes, rubric-based, diagnostic]
sources: ["https://arxiv.org/abs/2604.01375"]
---

# RIFT: A Rubric Failure Mode Taxonomy and Automated Diagnostics

## Overview
Rubric-based evaluation is ubiquitous in LLM benchmarks for open-ended, less-verifiable tasks. Yet rubric-driven pipelines have failure modes: rubric gaming, criterion misalignment, and automatic evaluation score inflation without real capability gain. RIFT provides the first principled taxonomy of rubric failure modes in LLM evaluation, with an automated diagnostic toolkit to detect each failure type. The authors demonstrate that widely-used benchmarks (SWE-bench-Verified, τ-bench) exhibit rubric failure modes that inflate apparent performance.

## Key Facts
- **Authors**: Qi, Zhengyang; Dickens, Charles; Pham, Derek + 4
- **Year**: 2026
- **arXiv**: [2604.01375](https://arxiv.org/abs/2604.01375)

## Key Contributions
- First systematic taxonomy of rubric failure modes in LLM evaluation (gaming, misalignment, score inflation)
- Automated diagnostic framework to detect each failure mode in deployed benchmarks
- Empirical audit of SWE-bench-Verified and τ-bench revealing benchmark inflation via rubric failure modes
- **First rubric-failure taxonomy paper in the wiki** — bridges evaluation methodology and deployment reliability

## Related Papers
- [[qval-cheaply-evaluating-dense-supervision-signals-for-long-horizon-llm-agents-2606.32034]] — Both concern evaluation methodology for long-horizon tasks; QVal measures supervision signals while RIFT audits the rubric framework itself
- [[a-multi-dataset-benchmark-for-evaluating-llm-agents-in-microservice-failure-diagnosis-2606.29193]] — Both diagnose agent failures; RIFT focuses on rubric/evaluation failures while the benchmark focuses on microservice deployment failures
- [[compositional-skill-routing-for-llm-agents-decompose-retrieve-and-compose-2606.18051]] — Both provide frameworks for understanding agent capabilities; RIFT diagnoses evaluation failure while CSR routes at the skill level
