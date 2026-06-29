---
title: "Multi-Agent Transactive Memory: Knowledge Sharing across Heterogeneous Agent Populations"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [collaborative-learning, transactive-memory, multi-agent, retrieval-augmented, knowledge-sharing]
sources: ["https://arxiv.org/abs/2606.19911"]
---

# Multi-Agent Transactive Memory: Knowledge Sharing across Heterogeneous Agent Populations

## Overview
MATM extends retrieval-augmented generation from individual agents to populations of agents — just as search engines index human-generated artifacts to support human problem-solving, retrieval systems can organize agent-generated artifacts for reuse across heterogeneous agent populations. Agent trajectories encode reusable solution patterns that, when indexed and retrieved across the population, allow downstream agents to short-cut similar task exploration.

## Key Facts
- **Authors**: (arXiv 2606.19911)
- **Year**: 2026
- **arXiv**: [2606.19911](https://arxiv.org/abs/2606.19911)
- **Online date**: 2026-06-18

## Key Contributions
- **Agent-generated artifacts as first-class retrieval units**: trajectories encode reusable patterns that, when indexed, support population-of-agents problem solving
- **Population-of-agents retrieval-augmented generation (PRAG)**: extends single-agent RAG to multi-agent populations — retrieval is over *agent-generated* artifacts, not human-authored ones
- **Decentralized deployment motivation**: heterogeneous-capability LLM agents across diverse tasks motivates infrastructure for knowledge sharing — MATM provides that infrastructure
- **Empirical improvement**: retrieving trajectories from MATM improves downstream task performance and reduces interaction steps without full re-training
- **Transactive memory generalization**: extends Wegner's transactive-memory framework (1986) to LLM-agent populations — knowledge is "stored" by which agent has which expertise, plus the indexing/retrieval layer that makes expertise lookup tractable
- **Cross-agent-replay primitive**: indexed trajectories function as replay memory that agents can retrieve without modifying underlying model weights — supports learning-without-forgetting at population scale

## Related Papers
- [[a-technical-taxonomy-of-llm-agent-communication-protocols-2606.19135]] — Communication protocol taxonomy whose transport layer MATM's population retrieval can be integrated with
- [[continuum-memory-architectures-for-long-horizon-llm-agents-2601.09913]] — Long-horizon memory substrate that MATM's population-of-agents retrieval complements as an inter-agent layer
- [[synapse-federated-tool-routing-via-typed-compendium-artifacts-2602.00911]] — Sibling Run 92 pick — federated typed-artifact routing that MATM can dispatch retrieval requests through
- [[cooperative-llm-agents-with-uncertainty-aware-task-allocation-2606.28182]] — Sibling Run 92 pick — embodied cooperation laws, complements MATM's population-retrieval with partner-alignment learning