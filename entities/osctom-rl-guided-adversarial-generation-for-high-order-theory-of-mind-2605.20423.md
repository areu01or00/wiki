---
title: "OSCToM: RL-Guided Adversarial Generation for High-Order Theory of Mind"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [benchmarking, llm-agents, theory-of-mind, adversarial]
sources: ["https://arxiv.org/abs/2605.20423"]
---

# OSCToM: RL-Guided Adversarial Generation for High-Order Theory of Mind

## Overview
OSCToM (Observer-Self Conflict Theory of Mind) addresses a key gap in ToM evaluation: existing benchmarks, including ExploreToM, fail to test recursive beliefs and information asymmetries in complex social settings. The paper uses RL-guided adversarial generation to create nested belief conflict scenarios that stress-test LLM ToM capabilities — specifically targeting the observer-self belief conflicts that make real social settings difficult.

## Key Facts
- **Authors**: Srishty, Sharmin Sultana; Rahman, Kazi Mahathir; Sakkhi, Malaika Parizat; Prianna, Samia Shahid
- **Year**: 2025
- **arXiv**: [2605.20423](https://arxiv.org/abs/2605.20423)

## Key Contributions
- RL-guided adversarial generation of high-order ToM scenarios (nested belief conflicts)
- Observer-Self Conflict (OSC) framework for modeling recursive belief conflicts in LLM ToM tasks
- Addresses information asymmetry gaps in prior ToM benchmarks (ExploreToM)
- First adversarial-RL approach to ToM benchmark generation

## Related Papers
- [[mindgames-a-live-arena-for-evaluating-social-and-strategic-reasoning-in-multi-agent-llms-2605.29512]] — Live arena social reasoning; orthogonal axis (multi-agent live arena vs. adversarial generation methodology)
- [[socialmembench-are-ai-memory-systems-ready-for-social-group-settings-2605.17789]] — Social memory evaluation; orthogonal axis (memory in social groups vs. adversarial ToM generation)
- [[probing-lack-of-stable-internal-beliefs-llms-2603.25187]] — LLM self-modeling; complements OSCToM's observer-other conflict with self-modeling deficit axis
