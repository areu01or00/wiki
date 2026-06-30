---
title: "ReFlect: An Effective Harness System for Complex Long-Horizon LLM Reasoning"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [reasoning, inference, harness, self-correction]
sources: ["https://arxiv.org/abs/2605.05737"]
---

# ReFlect: An Effective Harness System for Complex Long-Horizon LLM Reasoning

## Overview
Identifies two assumptions that fail in long-horizon multi-stage reasoning tasks (chain-of-thought, ReAct, post-hoc self-critique) and introduces ReFlect, a deterministic harness wrapper that creates standalone error detection and recovery logic. Addresses error accumulation by making self-critique structural rather than formulaic. Evaluated across 6 reasoning domains with 6 models.

## Key Facts
- **Authors**: Fan Huang
- **Year**: 2026
- **arXiv**: [2605.05737](https://arxiv.org/abs/2605.05737)

## Key Contributions
- Diagnosis: prompt-level self-critique produces formulaic templates that flag no issues in 90/100 audited reflection blocks; LLMs wrongly accept wrong answers in ≥76% of cases
- ReFlect harness: standalone error detection and recovery logic as a deterministic wrapper around the model — training-free, model-agnostic, inference-time only
- Task success rates 41% (gpt-4o-mini) to 56% (Claude Sonnet 4.5), with +7pp to +29pp gains over Direct CoT
- SWE-bench patch-structural quality: 0% (Direct CoT) → 82-87% (ReFlect)
- Inverse relationship between baseline success and harness gain (slope -1.69, r=-0.76): weaker models benefit most
- State/operator addition only yields 15-18.7% pair-mean on Llama-3.3-70B and Qwen2.5-72B — models at this scale cannot reliably populate required state

## Related Papers
- [[emergent-concepts]] — Parent wiki page for emergent concept discoveries
- [[metaresearcher-scaling-deep-research-via-self-reflective-reinforcement-learning-in-adversarial-virtual-environments-2606.19893]] — MetaResearcher's multi-agent self-reflective RL with adversarial world for training-time self-critique
- [[teaching-large-reasoning-models-effective-reflection-2601.12720]] — SCFT + RLERR for training LRMs to filter superficial reflections
