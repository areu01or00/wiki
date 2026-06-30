---
title: "AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing"
created: 2026-06-01
updated: 2026-06-01
type: entity
tags: [llm-evaluation, llm-as-judge, uncertainty-quantification]
sources: ["https://arxiv.org/abs/2606.19714"]
---

# AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing

## Overview
Large language models are increasingly used as judges for open-ended generation, as large-scale human evaluation is expensive and difficult to scale, yet their preferences remain imperfect proxies for human judgment. Existing auditing pipelines assume reliable subsample ground truth. AURA introduces adaptive uncertainty-aware refinement for LLM-as-a-Judge auditing, incorporating conformal prediction to quantify judge uncertainty and identify systematic bias patterns that simple accuracy metrics miss.

## Key Contributions
- Introduces adaptive uncertainty-aware framework (AURA) for LLM-as-a-Judge auditing using conformal prediction
- Identifies systematic judge bias patterns that standard accuracy-based auditing misses
- Shows uncertainty quantification enables targeted judge refinement rather than full retraining
- First conformal prediction application to LLM-as-Judge auditing in the wiki

## Key Facts
- **arXiv**: [2606.19714](https://arxiv.org/abs/2606.19714)

## Related Papers
- [[emergent-concepts]] — Parent emergent-concepts chain that led to this discovery
