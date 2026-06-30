---
title: "The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reinforcement-learning, training-inference-mismatch, policy-optimization]
sources: ["https://arxiv.org/abs/2606.29526"]
---

# The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning

## Overview
This paper reveals a fundamental training-inference mismatch in LLM reinforcement learning: optimizing training policies does not monotonically improve inference policies because LLMs use separate inference and training engines with different numerical precision (FP8 vs BF16), causing inconsistent trajectory probabilities even when model parameters are synchronized. The "mirage" is the assumption that training-policy improvement translates directly to inference-policy improvement.

## Key Facts
- **Authors**: Anonymous
- **Year**: 2026
- **arXiv**: [2606.29526](https://arxiv.org/abs/2606.29526)

## Key Contributions
- Identifies FP8/BF16 engine precision mismatch as the root cause of non-monotonic training-to-inference policy transfer in LLM RL
- Proposes treating inference policy as the actual optimization objective rather than the training policy proxy
- Shows monotonic alignment between inference-policy scores and downstream benchmark performance when using inference-side optimization

## Related Papers
- [[emergent-concepts]] — Parent discovery chain for emergent-concept discoveries
