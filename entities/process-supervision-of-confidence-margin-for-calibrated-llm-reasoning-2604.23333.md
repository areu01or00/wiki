---
title: "Process Supervision of Confidence Margin for Calibrated LLM Reasoning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning, calibration, test-time-compute, rl, llm]
sources: ["https://arxiv.org/abs/2604.23333"]
---

# Process Supervision of Confidence Margin for Calibrated LLM Reasoning

## Overview
Scaling test-time computation with reinforcement learning (RL) has improved LLM reasoning, but outcome-based reward incentivizes overconfidence — leading to hallucinations, unreliable confidence-based control, and wasted compute. This paper introduces Reinforcement Learning with Confidence Margin (RLCM): process-level supervision that trains LLMs to produce calibrated confidence margins alongside each reasoning step, enabling trustworthy downstream use of confidence signals.

## Key Facts
- **Authors**: Liaoyaqi Wang, Chunsheng Zuo, William Jurayj, Benjamin Van Durme, Anqi Liu
- **Year**: 2026
- **arXiv**: [2604.23333](https://arxiv.org/abs/2604.23333)

## Key Contributions
- **Confidence margin process supervision**: Reinforcement Learning with Confidence Margin (RLCM) — process-level reward that penalizes both overconfident and underconfident reasoning steps
- **Calibrated confidence-based control**: Confidence margins enable downstream control decisions (e.g., when to stop, when to request human input) without hallucination risk
- **Compute allocation**: Confidence signals allow the model to allocate test-time compute selectively — skipping unnecessary refinement on steps where confidence is already high
- **First in wiki**: First calibrated confidence-margin process supervision framework for LLM reasoning

## Related Papers
- [[est-prm-stress-testing-process-reward-models-before-they-become-load-bearing-2606.00437]] — Stress testing PRMs before deployment (load-bearing PRM axis)
- [[calibration-collapse-under-sycophancy-fine-tuning-reward-hacking-2604.10585]] — Calibration collapse under fine-tuning (orthogonal to RLCM margin-based approach)
- [[scatr-simple-calibrated-test-time-ranking-2604.16535]] — Calibrated test-time ranking (co-occurring run pick — orthogonal: ranking vs margin-based control)
