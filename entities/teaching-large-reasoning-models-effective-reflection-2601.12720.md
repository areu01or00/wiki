---
title: "Teaching Large Reasoning Models Effective Reflection"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [reasoning, self-supervision, training, rl]
sources: ["https://arxiv.org/abs/2601.12720"]
---

# Teaching Large Reasoning Models Effective Reflection

## Overview
Addresses the problem of superficial reflection in Large Reasoning Models (LRMs). Proposes SCFT (Self-Critique Fine-Tuning), which uses only self-generated critiques via rejection sampling, and RLERR (Reinforcement Learning with Effective Reflection Rewards) which uses high-quality reflections to construct reward signals for internalizing self-correction. Evaluated on AIME2024 and AIME2025.

## Key Facts
- **Authors**: Hanbin Wang, Jingwei Song, Jinpeng Li, Qi Zhu, Fei Mi, Ganqu Cui, Yasheng Wang, Lifeng Shang
- **Year**: 2026
- **arXiv**: [2601.12720](https://arxiv.org/abs/2601.12720)

## Key Contributions
- Identifies superficial reflection as a distinct failure mode: many LRM reflections are formulaic, offer no improvement, and incur computation overhead
- SCFT: prompts models to critique their own outputs, filters high-quality critiques via rejection sampling, fine-tunes with critique-based objective
- RLERR: leverages SCFT-initialized high-quality reflections to construct reward signals, guiding internalization of self-correction via RL
- Significant improvements on AIME2024 and AIME2025 over state-of-the-art baselines
- All data and code publicly available

## Related Papers
- [[emergent-concepts]] — Parent wiki page for emergent concept discoveries
- [[metaresearcher-scaling-deep-research-via-self-reflective-reinforcement-learning-in-adversarial-virtual-environments-2606.19893]] — MetaResearcher's multi-agent self-reflective RL framework
- [[reflect-an-effective-harness-system-for-complex-long-horizon-llm-reasoning-2605.05737]] — ReFlect harness for error detection and recovery in long-horizon reasoning
