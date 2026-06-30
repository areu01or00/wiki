---
title: "Learning What to Forget: Improving LLM Unlearning via Learned Token-Level Importance"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [unlearning, llm, privacy, token-level]
sources: ["https://arxiv.org/abs/2606.06320"]
---

# Learning What to Forget: Improving LLM Unlearning via Learned Token-Level Importance

## Overview
Machine unlearning aims to remove targeted knowledge from trained models while preserving general capabilities. For autoregressive language models, not all tokens in a forget sample are equally relevant to forgetting. This paper introduces Alternating Token-Weighted Unlearning (ATWU), which jointly learns token forget-specificity and model parameters during unlearning using a linear scorer over hidden states — without external token-level supervision. ATWU characterizes token forget-specificity through interaction with the retain objective: a token is forget-specific to the extent that minimizing the forget loss on that token does not conflict with retain optimality.

## Key Facts
- **Authors**: Gizem Yüce, Georgios Nikolaou, Nicolas Flammarion
- **Year**: 2026
- **arXiv**: [2606.06320](https://arxiv.org/abs/2606.06320)
- **Subjects**: Machine Learning (cs.LG), Artificial Intelligence (cs.AI), Computation and Language (cs.CL)
- **Submitted**: 2026-06-04

## Key Contributions
- Joint optimization over model parameters and token weights under a natural separation condition, recovering oracle forget-specific token support
- Alternating Token-Weighted Unlearning (ATWU) — lightweight framework using a simple linear scorer over hidden states
- Achieves state-of-the-art forget-retain trade-offs on TOFU and RWKU benchmarks
- Learned scores align substantially with ground truth forget-specific spans, identifying semantically meaningful token-level forgetting signals
- Demonstrates that retain conflict provides an effective criterion for unsupervised learning of token-level forget-specificity

## Related Papers
- [[selective-forgetting-for-large-reasoning-models-2604.03571]] — Sibling from same run — LRM-specific selective forgetting via RAG-based CoT trace analysis
- [[tmas-scaling-test-time-compute-via-multi-agent-synergy-2605.10344]] — Sibling from same run — multi-agent test-time compute scaling
- [[knowledgesmith-uncovering-knowledge-updating-in-llms-with-model-editing-and-unlearning-2510.02392]] — Parent: KnowledgeSmith — foundational LLM unlearning taxonomy
