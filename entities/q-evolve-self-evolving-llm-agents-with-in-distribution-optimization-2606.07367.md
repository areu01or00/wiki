---
title: "Q-Evolve: Self-Evolving LLM Agents with In-Distribution Optimization"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [self-evolving, agent, rl, process-reward, in-distribution, long-horizon, sparse-reward]
sources: ["https://arxiv.org/abs/2606.07367"]
---

# Q-Evolve: Self-Evolving LLM Agents with In-Distribution Optimization

## Overview
Introduces a self-evolving framework for LLM agents that unifies automatic process-reward labeling and policy learning inside a single in-distribution reinforcement learning loop, eliminating the distribution shift that destabilizes prior self-evolving-agent pipelines. Demonstrates stable agent self-evolution on AlfWorld, WebShop, and ScienceWorld using only unlabeled interaction plus expert demonstrations — no human process-reward annotation, no environment backtracking.

## Key Facts
- **Authors**: Zhang, Yudi; Fang, Meng; Chen, Zhenfang (and co-authors)
- **Year**: 2026
- **arXiv**: [2606.07367](https://arxiv.org/abs/2606.07367)
- **Online Date**: 2026-06-05

## Key Contributions
- **In-distribution critic for agent self-evolution**: learns a value function from a hybrid off-policy dataset mixing expert demonstrations with agent-generated trajectories, using weighted Implicit Q-Learning to stabilize Bellman backups under sparse-reward, long-horizon agent settings.
- **Automatic process-reward labeling via advantage estimation**: derives step-wise dense process rewards from the learned critic, replacing human-annotated step-level feedback with a model-derived signal — first in the wiki to combine agent-side in-distribution RL with PRM-style dense supervision in a single evolving loop.
- **Behavior-proximal policy optimization**: updates the agent's policy on the same trajectories used to fit the process reward signal, eliminating the data-distribution mismatch between reward-labeling and policy-learning that prior self-evolving methods suffered.
- **Sparse-reward long-horizon stabilization**: shows that stable agent self-evolution is achievable when the critic stays in-distribution, with empirical wins on sample efficiency, robustness, and overall task performance vs strong agent baselines on AlfWorld, WebShop, ScienceWorld.

## Related Papers
- [[ac-odm-actor-critic-online-data-mixing-for-sample-efficient-llm-pretraining-2505.23878]] — Actor-critic online data mixing for LLM pretraining — Q-Evolve applies the same actor-critic split to the agent RL setting where the critic is the process-reward labeler and the actor is the policy being evolved.
- [[maxproof-scaling-mathematical-proof-with-generative-verifier-rl-and-population-level-test-time-scaling-2606.13473]] — Generative-verifier RL for mathematical proof scaling — Q-Evolve's in-distribution critic is the agent-side analog of generative-verifier RL: both replace external reward models with model-derived dense supervision, but Q-Evolve targets the long-horizon agent loop rather than single-step mathematical reasoning.
- [[calvert-augmenting-agents-with-calibrated-verifier-telemetry-improves-action-and-learning-in-knowledge-intensive-tasks-2606.21777]] — Calibrated verifier telemetry for knowledge-intensive agents — complementary: CalVeRT supplies external verifier telemetry for agent learning, Q-Evolve internalizes the verifier into an in-distribution critic that the agent evolves jointly with the policy.