---
title: "Not All Turns Are Equally Hard: Adaptive Thinking Budgets For Efficient Multi-Turn Reasoning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, test-time-compute, multi-turn-reasoning, adaptive-budget, grpo]
sources: ["https://arxiv.org/abs/2604.05164"]
---

# Not All Turns Are Equally Hard: Adaptive Thinking Budgets For Efficient Multi-Turn Reasoning

## Overview
This paper formulates multi-turn LLM reasoning as a sequential compute allocation problem and proposes TAB (Turn-Adaptive Budgets), a GRPO-trained policy that learns to allocate smaller token budgets to easier conversation turns while preserving appropriate tokens for harder reasoning steps. TAB handles sequential dependencies that prior single-turn budget methods ignore, achieving up to 35% token savings while maintaining accuracy. A variant TAB-All-SubQ further saves 40% tokens when sub-question plans are available.

## Key Facts
- **arXiv**: [2604.05164](https://arxiv.org/abs/2604.05164)
- **Theme**: adaptive-thinking-budget-allocation / multi-turn-sequential-compute / grpo-post-training

## Key Contributions
- First multi-turn-specific adaptive thinking budget framework (prior work focuses on single-turn)
- GRPO-trained sequential budget policy that models multi-turn reasoning as a multi-objective MDP
- TAB-All-SubQ variant for when sub-question plans are available apriori (40% token savings)
- Comprehensive evaluation on mathematical reasoning benchmarks

## Related Papers
- [[mid-think-training-free-intermediate-budget-reasoning-via-token-level-triggers-2601.07036]] — Mid-Think: training-free token-level intermediate budget reasoning via triggers; different approach (training-free vs TAB's GRPO-trained policy) but same goal of reducing unnecessary thinking tokens
- [[draft-thinking-learning-efficient-reasoning-in-long-chain-of-thought-llms-2603.00578]] — Draft-Thinking: efficient long-CoT reasoning via draft token prediction; complementary approach using speculative decoding to reduce thinking costs
- [[thinkbooster-a-unified-framework-for-seamless-test-time-scaling-2606.06915]] — ThinkBooster: unified test-time scaling via verifier reranking; addresses multi-sample compute allocation differently (verifier-based vs TAB's learned MDP-based policy)
