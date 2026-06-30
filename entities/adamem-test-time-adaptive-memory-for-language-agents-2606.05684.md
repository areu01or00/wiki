---
title: "AdaMEM: Test-Time Adaptive Memory for Language Agents"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [agent, memory, test-time-adaptation, long-horizon]
sources: ["https://arxiv.org/abs/2606.05684"]
---

# AdaMEM: Test-Time Adaptive Memory for Language Agents

## Overview
Language agents are forced to rely on static guidance that becomes increasingly misaligned as long-horizon tasks unfold. AdaMEM introduces a test-time adaptive memory mechanism that dynamically retrieves from past experience during inference, allowing agents to update their memory representations based on the evolving context of multi-turn interactions.

## Key Facts
- **Authors**: Yunxiang Zhang, Yiheng Li, Ali Payani, Lu Wang
- **Year**: 2026
- **arXiv**: [2606.05684](https://arxiv.org/abs/2606.05684)

## Key Contributions
- Test-time adaptive memory that retrieves relevant past experiences at each step, not just at episode initiation
- Addresses the "rigidity problem" where static memory guidance becomes misaligned during long-horizon tasks
- Dynamically updates memory representations based on current context, not pre-loaded episodic prompts
- Evaluated on long-horizon agent benchmarks (WebArena, ToolBench) showing significant improvement over static-memory baselines

## Related Papers
- [[agentic-memory-agemem-learning-unified-long-term-and-short-term-memory-management-for-llm-agents-2601.01885]] — Prior work on unified memory management for agents (episode-initiation only)
- [[stop-when-further-reasoning-won't-help-attention-state-adaptive-generation-in-reasoning-models-2606.15070]] — Test-time compute allocation for reasoning models
