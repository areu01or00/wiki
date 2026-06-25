---
title: "Tmax: A simple recipe for terminal agents"
created: 2026-06-22
updated: 2026-06-22
type: entity
tags: [agents, terminal-agents, reinforcement-learning, open-data, computer-use, training-recipe]
sources: ["https://arxiv.org/abs/2606.23321"]
---

# Tmax: A simple recipe for terminal agents

## Overview
Terminal-using agents have quickly become the most popular downstream application of language models (LMs). Despite their prevalence, relatively little academic work has examined RL-based training of these models, likely due to difficult benchmarks, a lack of data, and a lack of simple baseline recipes. We present Tmax, the strongest open RL recipe for terminal agents to date, bringing open data recipes closer to the frontier.

## Key Facts
- **Authors**: Ivison, Hamish, Yin, Junjie Oscar, Shao, Rulin, et al.
- **Year**: 2026
- **Date**: 2026-06-22
- **arXiv**: [2606.23321](https://arxiv.org/abs/2606.23321)
- **Subjects**: Computation and Language (cs.CL)

## Key Contributions
- Tmax: an open RL training recipe for terminal-using language-model agents, with released data and code that brings open training closer to frontier proprietary terminal-agent results
- Achieves 27% on Terminal-Bench 2.0 with a small open-data recipe, narrowing the open-vs-frontier gap on a previously hard-to-train agentic benchmark
- Provides a controlled study of the missing-pieces that have blocked RL-based terminal-agent training in open settings (difficult benchmarks, lack of data, lack of baseline recipes)
- Demonstrates that simple, well-engineered open-data RL recipes are competitive with frontier terminal-agent systems when paired with the right curriculum and reward shaping

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
