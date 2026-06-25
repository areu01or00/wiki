---
title: "Qwen-AgentWorld: Language World Models for General Agents"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [world-models, agentic-llm, reinforcement-learning, foundation-models, environment-simulation, llm-training, llm-research]
sources: ["https://arxiv.org/abs/2606.24597"]
---

# Qwen-AgentWorld: Language World Models for General Agents

## Overview
This paper introduces Qwen-AgentWorld, the first family of language world models capable of simulating agentic environments across 7 domains via long chain-of-thought reasoning, trained through a three-stage pipeline (CPT → SFT → RL) on 10M+ environment interaction trajectories. Beyond the foundation models themselves, the work establishes two complementary paradigms — decoupled environment simulation for scalable agentic RL, and unified agent foundation models where world-model training acts as an effective warm-up for downstream agentic tasks — and introduces AgentWorldBench for evaluation against frontier closed models.

## Key Facts
- **Authors**: Zuo, Yuxin; Xiao, Zikai; Sheng, Li; Huang, Fei; Tu, Jianhong
- **Year**: 2026
- **Date**: 2026-06-23
- **arXiv**: [2606.24597](https://arxiv.org/abs/2606.24597)
- **Subjects**: Computation and Language (cs.CL)

## Key Contributions
- First language world models for agentic environment simulation — Qwen-AgentWorld-35B-A3B and Qwen-AgentWorld-397B-A17B — trained on 10M+ interaction trajectories across 7 domains via long chain-of-thought reasoning
- Three-stage training pipeline: CPT injects world-modeling capabilities from state-transition dynamics + augmented corpora, SFT activates next-state-prediction reasoning, RL sharpens simulation fidelity with hybrid rubric-and-rule rewards
- Introduces AgentWorldBench, a benchmark built from real-world interactions of 5 frontier models across 9 established benchmarks for evaluating language world models
- Demonstrates Qwen-AgentWorld significantly outperforms existing frontier closed models on world-model simulation
- Decoupled-simulator paradigm: Qwen-AgentWorld supports scalable, controllable simulation of thousands of real-world environments for agentic RL, beating real-environment training alone
- Unified-agent paradigm: world-model training as a warm-up yields downstream gains across 7 agentic benchmarks when integrated into agent foundation models
- Releases code and models at https://github.com/QwenLM/Qwen-AgentWorld

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[openthoughts-agent-data-recipes-for-agentic-models-2606.24855]] — Complementary agentic-training work from the same 2026-06-23 window
- [[tapered-language-models-2606.23670]] — Architectural innovation paper from the same run