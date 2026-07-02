---
title: "When LLMs Read Tables Carelessly: Measuring and Reducing Data Referencing Errors"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [hallucination, data-error, factuality, evaluation]
sources: ["https://arxiv.org/abs/2606.32029"]
---

# When LLMs Read Tables Carelessly: Measuring and Reducing Data Referencing Errors

## Overview
While LLMs perform well on table tasks, they systematically make data referencing errors (DREs) — incorrectly citing or omitting table values despite understanding the structure. This paper introduces the first systematic benchmark for measuring DREs and proposes mitigation techniques targeting this specific failure mode.

## Key Facts
- **Authors**: Yang, Yuqing; Zhu, Qi; Han, Zhen + 5
- **Year**: 2026
- **arXiv**: [2606.32029](https://arxiv.org/abs/2606.32029)

## Key Contributions
- First systematic measurement of data referencing errors (DREs) in table-reading LLMs
- Taxonomy of DRE types: value omission, wrong cell citation, hallucinated numbers
- Reduction methods via targeted fine-tuning and retrieval-augmented verification
- New evaluation dimension beyond final-answer accuracy

## Related Papers
- [[hallucination-in-world-models-is-predictable-and-preventable-2606.27326]] — Hallucination taxonomy and predictability in LLM outputs
- [[atomicmed-hierarchical-atomic-fact-checking-for-universal-clinical-aware-medical-report-evaluation-2606.31292]] — Atomic fact-checking framework applied to medical report evaluation
- [[tabclaw-an-interactive-and-self-evolving-agent-for-spreadsheet-manipulation-and-table-reasoning-2606.10316]] — Table reasoning agent with self-evolution
