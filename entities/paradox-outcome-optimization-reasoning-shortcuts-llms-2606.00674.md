---
title: "The Paradox of Outcome Optimization: A Causal Information-Theoretic Bound on Reasoning Shortcuts in LLMs"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [reasoning, RLHF, alignment, failure-mode]
sources: ["https://arxiv.org/abs/2606.00674"]
---

# The Paradox of Outcome Optimization: A Causal Information-Theoretic Bound on Reasoning Shortcuts in LLMs

## Overview
This paper identifies a fundamental failure mode in outcome-based RL-aligned LLMs: Reward-Induced Manifold Collapse, where models achieve strong in-distribution benchmark performance but fail catastrophically on out-of-distribution tasks due to an information shortcut between the reward signal and the reasoning chain.

## Key Facts
- **arXiv**: [2606.00674](https://arxiv.org/abs/2606.00674)
- **Year**: 2026
- **Theme**: reasoning-shortcut RL-alignment

## Key Contributions
- Identifies Reward-Induced Manifold Collapse as a new failure mode distinct from classical reward hacking
- Proves via Structural Causal Models that outcome-based RL inherently creates information shortcuts to the reasoning chain
- Derives an information-theoretic bound on reasoning shortcut magnitude based on mutual information between reward and latent reasoning space
- Shows process-based rewards overcome this limitation while outcome-based RL cannot, across 8 OOD benchmarks

## Related Papers
- [[emergent-concepts]] — Parent emergent concepts discovery framework
