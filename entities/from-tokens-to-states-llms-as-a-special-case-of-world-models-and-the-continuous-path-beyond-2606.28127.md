---
title: "From Tokens to States: LLMs as a Special Case of World Models and the Continuous Path Beyond"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [world-models, LLM-theory, representation-learning, token-prediction]
sources: ["https://arxiv.org/abs/2606.28127"]
---

# From Tokens to States: LLMs as a Special Case of World Models and the Continuous Path Beyond

## Overview
The paper challenges the prevailing dichotomy between LLMs (token predictors) and world models (simulators of reality). The author argues that every autoregressive LLM can be formally embedded within the world model formalism — that token prediction is a special case of world modeling where the "world state" is compressed into token sequences. The paper proposes a continuous spectrum between pure token prediction and full world simulation, and identifies the specific architectural and training choices that push an LLM along this spectrum toward genuine world modeling capability.

## Key Facts
- **Authors**: Dubois, Paul
- **Year**: 2026
- **arXiv**: [2606.28127](https://arxiv.org/abs/2606.28127)

## Key Contributions
- Formal proof that autoregressive LLMs are a strict subset of world models — the world state is just the token history compressed via the model's internal representations
- Introduces the "world model depth" axis: models can range from shallow token-sequence predictors to deep world simulators depending on architectural choices (recurrence, world-state scaffolding, planning-oriented fine-tuning)
- Identifies three concrete mechanisms that push an LLM from token prediction toward world simulation: (1) world-state scaffolding with external memory, (2) cross-episodic representation binding, (3) intervention-directed fine-tuning for counterfactual reasoning
- Resolves the LeCun vs. deep learning debate by showing token prediction and world modeling are not mutually exclusive but hierarchically related

## Related Papers
- [[internalizing-the-future-a-unified-agentic-training-paradigm-for-world-model-planning-2606.27483]] — Parallel work on training paradigms for world model planning in LLM agents
- [[einstein-world-models-2606.26969]] — Physics-informed world models for LLM agents that extend the token→state spectrum in the spatial reasoning direction
- [[hallucination-in-world-models-is-predictable-and-preventable-2606.27326]] — Documents the world model failure mode where compressed token representations create hallucinated state estimates
- [[worldevolver-self-evolving-world-models-for-llm-agent-planning-2606.30639]] — Self-evolving world model training framework for agents that directly implements the "continuous path beyond" proposed in this paper
