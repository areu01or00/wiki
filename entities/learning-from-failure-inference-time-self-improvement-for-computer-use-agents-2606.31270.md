---
title: "Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [llm-agents, self-improvement, computer-use, synthetic-data, inference-time]
sources: ["https://arxiv.org/abs/2606.31270"]
---

# Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents

## Overview
This paper introduces a failure-driven self-improvement loop for computer-use agents. The standard approach to improving agents is self-improving loops that fine-tune on successful trajectories only — this paper shows that failed trajectories carry rich information about model weaknesses and should not be discarded. The approach uses an LLM to diagnose failure modes, propose inference-time solutions, and generate code patches, validated on OSWorld with OpenCUA-72B (42.3% to 48.9%).

## Key Facts
- **arXiv**: [2606.31270](https://arxiv.org/abs/2606.31270)
- **Year**: 2026
- **Theme**: agent-training / self-improvement / failure-data

## Key Contributions
- Identifies that standard self-improving loops exploit only successful trajectories and discard failures, even though failures carry rich information about model weaknesses
- Proposes a complementary failure-driven self-improvement loop: LLM diagnoses failure modes, proposes inference-time solutions, and generates code patches
- Validates on OSWorld benchmark with OpenCUA-72B model: success rate improves from 42.3% to 48.9% (+6.6pp) with no additional training cost
- Demonstrates that failure-driven self-improvement is a viable complement to success-based pipelines

## Related Papers
- [[self-improvement-can-self-regress-rise-and-collapse-llm-self-training-2606.21090]] — Self-improvement collapse failure mode (training-time, complementary to this inference-time approach)
- [[osworld20-benchmarking-computer-use-agents-on-long-horizon-real-world-tasks-2606.29537]] — OSWorld benchmark used for evaluation
- [[capable-but-careless-do-computer-use-agents-follow-contextual-integrity-2606.23189]] — Computer-use agent failures and contextual integrity
