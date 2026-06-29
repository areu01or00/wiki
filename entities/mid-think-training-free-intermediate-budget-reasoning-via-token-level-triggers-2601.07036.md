---
title: "Mid-Think: Training-Free Intermediate-Budget Reasoning via Token-Level Triggers"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning-mode-control, hybrid-reasoning, training-free, token-triggers, cognitive-load, inference-time-control]
sources: ["https://arxiv.org/abs/2601.07036"]
authors: ["Wang Yang", "Debargha Ganguly", "Xinpeng Li", "Chaoda Song", "Shouren Wang", "Vikash Singh", "Vipin Chaudhary", "Xiaotian Han"]
---

# Mid-Think: Training-Free Intermediate-Budget Reasoning via Token-Level Triggers

## Overview
Identifies that hybrid reasoning language models are controlled not by high-level Think/No-think instructions but by a small set of specific trigger tokens, and introduces Mid-Think — a training-free prompting format that combines these tokens (a leading "Okay" plus the newline-after-``</think>`` pattern) to achieve intermediate-budget reasoning that beats fixed-token and prompt-based baselines on accuracy-length trade-off. Applied after SFT, also reduces RL training time by ~15% and improves Qwen3-8B on AIME from 69.8% to 72.4% and GPQA from 58.5% to 61.1%.

## Key Facts
- **Authors**: Wang Yang, Debargha Ganguly, Xinpeng Li, Chaoda Song, Shouren Wang, Vikash Singh, Vipin Chaudhary, Xiaotian Han
- **Year**: 2026 (submission 2026-01-11, online 2026-06-02)
- **arXiv**: [2601.07036](https://arxiv.org/abs/2601.07036)
- **Submission**: 2026/01/11
- **Online**: 2026/06/02

## Key Contributions
- Establishes via attention analysis and controlled prompting that mode switching in hybrid reasoning models is driven by a small set of trigger tokens, not the high-level Think/No-think instructions themselves.
- Identifies a leading "Okay" token as inducing reasoning behavior and the newline pattern following ``</think>`` as suppressing it — providing the first formal token-level-trigger primitive for hybrid-reasoning mode control.
- Introduces Mid-Think as a simple training-free prompting format combining these triggers to enable intermediate-budget reasoning, consistently outperforming fixed-token and prompt-based baselines on accuracy-length trade-off.
- Demonstrates post-SFT RL training improvement: Qwen3-8B on AIME 69.8% → 72.4%, GPQA 58.5% → 61.1%, with ~15% training-time reduction.
- Surfaces *training-free-intermediate-budget-reasoning-primitive* and *token-level-trigger-as-mode-switch-primitive* and *inference-time-cognitive-load-via-token-prompts-primitive* as the load-bearing hybrid-reasoning cognitive-load primitives.
- Distinct from high-level-instruction mode-control primitives (where the load-bearing axis is *token-triggers-as-suppression-mechanism* rather than *instruction-conditioning*).

## Related Papers
- [[off-the-shelf-llms-as-process-scorers-training-free-prm-alternative-chunk-level-guided-generation-2606.01682]] — Training-free inference-time cognitive budget primitive (sibling training-free reasoning control)
- [[reasoning-models-struggle-to-control-their-chains-of-thought-2603.05706]] — Sibling CoT-control primitive identifying CoT-vs-output controllability asymmetry on Claude Sonnet 4.5
- [[agentic-chain-of-thought-steering-for-efficient-and-controllable-llm-reasoning-2606.03965]] — Sibling CoT-steering primitive for efficient and controllable LLM reasoning
- [[adaptive-test-time-compute-allocation-for-reasoning-llms-via-constrained-policy-optimization-2604.14853]] — Sibling constrained-policy test-time compute allocation primitive
- [[safe-few-step-generation-via-velocity-editing-2606.23267]] — Sibling inference-time step-budget primitive
