---
title: "Grounded Iterative Language Planning: How Parameterized World Models Reduce Hallucination Propagation in LLM Agents"
created: "2026-06-29"
updated: "2026-06-29"
type: entity
tags: [agent-planning, world-models, hallucination, llm-agents]
sources: ["https://arxiv.org/abs/2606.27806"]
---

# Grounded Iterative Language Planning: How Parameterized World Models Reduce Hallucination Propagation in LLM Agents

## Overview
GILP combines LLM-based language reasoning with parameterized world models for grounded verification. Agent-based world models are flexible but produce hallucinated state transitions; parameterized world models are verifiable but less flexible. GILP bridges both by using the LLM to propose high-level plans while the parameterized model grounds and verifies each step, arresting hallucination propagation through the agent execution loop.

## Key Facts
- **Authors**: Xinyuan Song, Zekun Cai
- **Year**: 2026
- **arXiv**: [2606.27806](https://arxiv.org/abs/2606.27806)
- **Theme**: agent planning / world-model hallucination reduction / grounded iterative planning

## Key Contributions
- **Grounded Iterative Language Planning**: LLM proposes abstract plan steps; parameterized world model grounds each step and verifies state transitions
- **Hallucination propagation arrest**: Systematic detection of hallucinated state changes via learned consistency checks against the parameterized model
- **Combined flexibility + verifiability**: Achieves planning flexibility of agent-based approaches with the rigor of learned state-transition functions
- **Benchmark**: Evaluates on multi-step agent tasks where prior agent-based world models accumulate hallucinated state

## Related Papers
- [[emergent-concepts]] — Parent emergent concept discovery
- [[hallucination-in-world-models-is-predictable-and-preventable-2606.27326]] — Complementary: predicts and prevents world-model hallucinations; GILP verifies and corrects them
- [[textual-belief-states-for-world-models-identifiable-represen-2606.27681]] — Textual world model representations; GILP uses parameterized (non-textual) grounding as the verification layer
- [[simmer-benchmarking-latent-failures-in-llm-executable-planning-with-a-world-model-2606.14574]] — SIMMER benchmarks latent planning failures; GILP addresses one specific failure mode (hallucination propagation) in that class
