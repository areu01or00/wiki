---
title: "PS-PPO: Prefix-Sampling PPO for Critic-Free RLHF"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [alignment, reinforcement-learning, llm, inference-efficiency]
sources: ["https://arxiv.org/abs/2606.29758"]
---

# PS-PPO: Prefix-Sampling PPO for Critic-Free RLHF

## Overview
PS-PPO (Prefix-Sampling PPO) addresses a core practical bottleneck in RLHF for LLMs: the need for a learned critic network adds memory overhead and training complexity. The paper proposes sampling multiple prefix continuations and using a pairwise reward comparison to estimate advantage — effectively replacing the value function with a sampling-based baseline. This makes RLHF deployable in critic-free settings without sacrificing the policy improvement signal from PPO.

## Key Facts
- **Authors**: Hwang, Doo Hwan; Kim, Kee-Eung
- **Year**: 2026
- **arXiv**: [2606.29758](https://arxiv.org/abs/2606.29758)

## Key Contributions
- Prefix-sampling baseline replaces learned critic for advantage estimation in PPO
- Pairwise reward comparison across K sampled continuations gives stable advantage signal
- Matches full critic-based PPO on reasoning benchmarks while reducing memory footprint
- Demonstrates critic-free RLHF is viable for production LLM alignment pipelines

## Related Papers
- Emergent discovery — no prior parent paper; this work contributes a new critic-free RLHF primitive to the wiki.
