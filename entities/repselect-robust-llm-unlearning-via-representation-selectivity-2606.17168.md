---
title: "RepSelect: Robust LLM Unlearning via Representation Selectivity"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [machine-unlearning, representation-selectivity, llm, privacy, alignment]
sources: ["https://arxiv.org/abs/2606.17168"]
---

# RepSelect: Robust LLM Unlearning via Representation Selectivity

## Overview
RepSelect solves the core failure mode of current LLM unlearning methods: their forgetting is shallow and easily reversed by fine-tuning or few-shot prompting attacks. The root cause is that existing methods target representations shared with both the retain set and the attacker's recovery subspace. RepSelect isolates forget-set-specific representations by collapsing top principal components of weight gradients before each update, leaving general capabilities intact while limiting what adversarial fine-tuning can recover.

## Key Facts
- **Authors**: Filip Sondej, Yushi Yang, Adam Mahdi
- **Year**: 2026
- **arXiv**: [2606.17168](https://arxiv.org/abs/2606.17168)

## Key Contributions
- Identifies representation sharing with retain set AND attacker recovery subspace as the root cause of shallow unlearning
- Collapses top principal components of weight gradients to isolate forget-set-specific representations
- 4-50x larger reduction in post-relearning answer accuracy vs. strongest baseline (GradDiff, NPO, SimNPO, RMU, UNDIAL)
- Near-perfect robustness to few-shot prompting attacks across Llama 3, Qwen 3.5, Gemma 4 E4B, DeepSeek V2 Lite

## Related Papers
- [[emergent-concepts]] — Parent emergent-concepts wiki page that this discovery extends
