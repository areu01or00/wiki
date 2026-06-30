---
title: "IAPO: Information-Aware Policy Optimization for Token-Efficient Reasoning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, token-efficiency, rl-post-training, information-theory, reasoning]
sources: ["https://arxiv.org/abs/2602.19049"]
---

# IAPO: Information-Aware Policy Optimization for Token-Efficient Reasoning

## Overview
This paper identifies that existing sequence-level reward-shaping methods for token-efficient reasoning fail to control how reasoning effort is allocated at the token level. The authors propose IAPO (Information-Aware Policy Optimization), an information-theoretic post-training framework that assigns token-wise advantages based on each token's conditional mutual information with the final answer. IAPO provides a principled mechanism to identify informative reasoning steps and suppress low-utility exploration, achieving up to 36% reasoning length reduction while maintaining accuracy — outperforming existing token-efficient RL methods.

## Key Facts
- **arXiv**: [2602.19049](https://arxiv.org/abs/2602.19049)
- **Theme**: token-efficient-reasoning / information-theoretic-advantage / conditional-mutual-information

## Key Contributions
- First information-theoretic (conditional mutual information) token-wise advantage assignment for reasoning
- Monotonic token reduction guarantee (theoretical analysis)
- 36% reasoning length reduction while maintaining accuracy
- General framework applicable across reasoning datasets
- Outperforms existing token-efficient RL methods (GRPO, PPO variants)

## Related Papers
- [[not-all-turns-are-equally-hard-adaptive-thinking-budgets-for-efficient-multi-turn-reasoning-2604.05164]] — TAB: multi-turn adaptive thinking budgets via GRPO; complementary (TAB = turn-level sequential allocation, IAPO = token-level MI-based advantage)
- [[thinkbooster-a-unified-framework-for-seamless-test-time-scaling-2606.06915]] — ThinkBooster: test-time scaling via verifier reranking; addresses inference efficiency differently (verifier-based diversity vs IAPO's information-theoretic token weighting)
- [[draft-thinking-learning-efficient-reasoning-in-long-chain-of-thought-llms-2603.00578]] — Draft-Thinking: efficient long-CoT via draft prediction; distinct approach (speculative decoding vs IAPO's post-training token-level advantage shaping)
