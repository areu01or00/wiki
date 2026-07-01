---
title: "Efficient LLM Reasoning via Variational Posterior Guidance with Efficiency Awareness"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning, efficiency, RL, variational-inference]
sources: ["https://arxiv.org/abs/2605.11019"]
---

# Efficient LLM Reasoning via Variational Posterior Guidance with Efficiency Awareness

## Overview
Addresses the "overthinking" problem in chain-of-thought reasoning — LLMs generate excessively long reasoning traces that degrade inference efficiency. Proposes variational posterior guidance (VPG) combined with efficiency awareness, applying variational inference theory to LLM reasoning optimization for the first time.

## Key Facts
- **Authors**: Chen, Zizhao; Li, Yuying; Lin, Siting + 1
- **Year**: 2026
- **arXiv**: [2605.11019](https://arxiv.org/abs/2605.11019)
- **Discovered**: 2026-07-01 (Rule 36h PROBE-AXIS: reasoning efficiency + token efficiency)

## Key Contributions
- First application of variational inference theory to LLM reasoning efficiency optimization
- VPG framework that guides reasoning toward shorter, more accurate chains
- Efficiency-awareness incorporated into RL-based reasoning optimization
- Addresses overthinking: the phenomenon where CoT models generate verbose traces that waste compute

## Related Papers
- [[agentic-chain-of-thought-steering-for-efficient-and-controllable-llm-reasoning-2606.03965]] — Related efficient reasoning work via chain-of-thought steering
- [[adaptive-test-time-compute-allocation-for-reasoning-llms-via-constrained-policy-optimization-2604.14853]] — Test-time compute allocation for reasoning LLMs
