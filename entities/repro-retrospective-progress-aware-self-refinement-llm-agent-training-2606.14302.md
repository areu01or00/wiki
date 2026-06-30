---
title: "Retrospective Progress-Aware Self-Refinement for LLM Agent Training"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agent, self-refinement, metacognition, reinforcement-learning, training]
sources: ["https://arxiv.org/abs/2606.14302"]
---

# Retrospective Progress-Aware Self-Refinement for LLM Agent Training

## Overview
This paper identifies a critical metacognitive gap in LLM-based agents trained with reinforcement learning: they optimize step-wise action prediction but lack awareness of task progress, making them unable to self-correct during long-horizon tasks. The authors present RePro (Retrospective Progress-Aware Training), which trains agents to self-generate progress signals from completed sub-tasks, enabling retrospective self-refinement that outperforms both outcome-reward-only RL and naive progress prompting.

## Key Facts
- **Authors**: Xinbei Ma, Congmin Zheng, Jiyang Qiu, Jiale Hong, Yao Yao, Xiangmou Qu, Jiaxin Yin, Xingyu Lou, Jun Wang, Weiwen Liu, Weinan Zhang, Zhuosheng
- **Year**: 2026
- **arXiv**: [2606.14302](https://arxiv.org/abs/2606.14302)

## Key Contributions
- **Metacognitive gap identification**: RL-trained agents lack progress awareness — they cannot determine whether they are making headway toward goal completion
- **RePro framework**: Retrospective Progress-Aware Training — trains agents to generate retrospective progress demonstrations, enabling self-refinement without external feedback
- **Key finding**: Online progress prompting hurts performance (agents get distracted by progress cues); retrospective demonstrations help (agents learn from completed sub-tasks)
- **Long-horizon scaling evidence**: Without progress-awareness, RL agents hit a scaling ceiling on multi-step tasks; RePro enables continued improvement

## Related Papers
- [[the-metacognitive-monitoring-battery-a-cross-domain-benchmark-for-llm-self-monitoring-2604.15702]] — Cross-domain metacognitive benchmark (complementary: RePro shows how to train progress-awareness, the benchmark measures whether it transfers)
- [[knowing-acting-probe-kapro-benchmarking-self-awareness-capability-of-llm-agents-2606.20661]] — KAPRO self-awareness benchmark (orthogonal: RePro trains agents to have progress awareness, KAPRO evaluates whether they know what they can/cannot solve)
- [[when-agents-commit-too-soon-diagnosing-premature-commitment-in-llm-agents-2606.22936]] — Premature commitment failure in agents (related: both papers identify agent metacognitive failure modes, premature commitment is a different failure type)
