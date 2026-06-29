---
title: "REVES: REvision and VErification-Augmented Training for Test-Time Scaling"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, test-time-compute, self-correction, llm]
sources: ["https://arxiv.org/abs/2606.18910"]
---

# REVES: REvision and VErification-Augmented Training for Test-Time Scaling

## Overview
REVES proposes a two-stage iterative framework that alternates between online data/prompt augmentation and policy optimization for test-time scaling. The core insight is that near-miss answers in successful recovery trajectories are high-quality training signal: converting intermediate correction steps into decoupled revision and verification prompts concentrates training on both effective answer transformation and error identification. On LiveCodeBench, REVES gains +6.5 points over RL baseline and +4.0 points over standard multi-turn training, using the smallest base model (4B).

## Key Facts
- **Authors**: Yuanxin Liu, Ruida Zhou, Xinyan Zhao, Amr Sharaf, Hongzhou Lin, Arijit Biswas, Mohammad Ghavamzadeh, Zhaoran Wang, Mingyi Hong
- **Year**: 2026
- **arXiv**: [2606.18910](https://arxiv.org/abs/2606.18910)
- **Submitted**: 17 June 2026
- **Subjects**: Machine Learning (cs.LG); Computation and Language (cs.CL)

## Key Contributions
- Two-stage iterative framework: online data/prompt augmentation ↔ policy optimization
- Near-miss conversion: intermediate "near-miss" answers in recovery trajectories become decoupled revision + verification prompts
- Efficient off-policy data generation reducing computational overhead vs standard multi-turn RL
- +6.5 points over RL baseline, +4.0 points over standard multi-turn training on LiveCodeBench
- Generalizes to constraint-satisfaction puzzles (n-queens, mini-sudoku) with ground-truth verification

## Related Papers
- [[grace-granularity-regulated-adaptive-computational-efficiency-for-optimal-verification-in-test-time-scaling-2606.19354]] — GRACE (this run pick; REVES's revision-verification training is complementary to GRACE's theoretical framework on optimal verification granularity — both address the question of how much verification is enough)
- [[thinkbooster-a-unified-framework-for-seamless-test-time-scaling-2606.06915]] — ThinkBooster unified test-time scaling (sibling test-time compute paper; REVES provides the training-side answer to what verification-augmented training looks like in practice)
- [[escaping-the-self-confirmation-trap-an-execute-distill-verify-paradigm-for-agentic-experience-learning-2606.24428]] — Execute-Distill-Verify paradigm (parallels REVES's revision-and-verification approach; both decompose multi-step correction into verification-enabled learning)
