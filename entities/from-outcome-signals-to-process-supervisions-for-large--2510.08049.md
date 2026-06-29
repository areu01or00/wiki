---
title: "From Outcome Signals to Process Supervisions for Large Language Models"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [process-reward-model, survey, alignment, reasoning, llm]
sources: ["https://arxiv.org/abs/2510.08049"]
---

# From Outcome Signals to Process Supervisions for Large Language Models

## Overview
A systematic survey of Process Reward Models (PRMs), which evaluate and guide reasoning at the step or trajectory level rather than judging only final answers (as ORMs do). Covers the full PRM loop: how to generate process data, how to train PRMs, how to apply PRMs for training (process-supervised RL) and inference (verifier-guided search). Surveys 50+ PRM papers and organizes them by architecture, training method, and application domain.

## Key Facts
- **Authors**: Congmin Zheng, Jiachen Zhu, Zhuoying Ou, Yuxiang Chen, Kangning Zhang, Rong Shan, Zeyu Zheng, Mengyue Yang, Jianghao Lin, Yong Yu, Weinan Zhang
- **Year**: 2025
- **arXiv**: [2510.08049](https://arxiv.org/abs/2510.08049)

## Key Contributions
- First comprehensive taxonomy of PRM literature: generation methods, training objectives, inference strategies
- Identifies 5 key challenges: step-level annotation cost, verifier design, credit assignment, generalizability, scalability
- Surveys process-supervised RL approaches: STaR, RLEF, PRM, APO, DIP
- Surveys verifier-guided search: beam search, MCTS, self-consistency with PRM reranking
- Establishes PRM vs ORM comparison framework across 12 dimensions
- First survey-level synthesis of PRM field in the wiki; complements the individual PRM entity papers (VERM, Process Reward Models That Think, GenPRM, etc.)

## Related Papers
- [[est-prm-stress-testing-process-reward-models-before-they-become-load-bearing-2606.00437]] — Stress-testing PRMs before deployment
- [[unsupervised-process-reward-models-2605.10158]] — Unsupervised PRM training
