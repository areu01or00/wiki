---
title: "Self-ReSET: Learning to Self-Recover from Unsafe Reasoning Trajectories"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [safety, reasoning-models, self-correction, adversarial, rl, llm]
sources: ["https://arxiv.org/abs/2605.08936"]
---

# Self-ReSET: Learning to Self-Recover from Unsafe Reasoning Trajectories

## Overview
Self-ReSET equips Large Reasoning Models (LRMs) with intrinsic self-recovery capability from unsafe reasoning trajectories under adversarial attacks. Uses a pure reinforcement learning framework where the model's own safety error trajectories are collected and reused as initial states for RL, enabling on-policy learning from dynamic reasoning traces rather than static expert data.

## Key Facts
- **Year**: 2025
- **arXiv**: [2605.08936](https://arxiv.org/abs/2605.08936)

## Key Contributions
- Pure RL framework for self-recovery: model generates safety error trajectories then reuses them as RL initial states
- Solves the distribution mismatch between static training data and dynamic on-policy reasoning traces
- Significantly enhances robustness against adversarial jailbreak prompts (OOD setting) while maintaining general utility
- Efficient data utilization — leverages model's own failure trajectories rather than external critics

## Related Papers
- [[learning-from-failure-inference-time-self-improvement-for-computer-use-agents-2606.31270]] — Learning from failure: inference-time self-improvement for computer use agents
- [[adamem-test-time-adaptive-memory-for-language-agents-2606.05684]] — AdaMem: test-time adaptive memory for language agents
- [[ajar-adaptive-jailbreak-architecture-red-teaming-2601.10971]] — Adaptive jailbreak red-teaming architecture (related adversarial safety axis)
