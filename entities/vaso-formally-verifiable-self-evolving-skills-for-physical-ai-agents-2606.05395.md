---
title: "VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [formal-verification, embodied-agent, skill-learning, robotics, llm]
sources: ["https://arxiv.org/abs/2606.05395"]
---

# VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents

## Overview
VASO addresses the trustworthiness gap in robot skill learning: foundation models have made it cheap to create reusable robot skills from open-ended instructions, but the cost of *trusting* them remains high. The paper proposes a self-evolution loop where skills are continuously refined while maintaining formal verification guarantees — bridging the gap between data-driven skill acquisition and formal proofs of safety/correctness.

## Key Facts
- **Authors**: Yang, Yunhao; Bhatt, Neel P.; Wang, Kevin + 4 more
- **Year**: 2026
- **arXiv**: [2606.05395](https://arxiv.org/abs/2606.05395)
- **Online Date**: 2026-06-03

## Key Contributions
- Formal verification layer integrated into the skill-evolution feedback loop, enabling trust verification alongside reward optimization
- Self-evolving skill framework where skills improve through execution feedback while maintaining formal safety guarantees
- Demonstrates that formal methods and LLM-driven skill learning are complementary, not conflicting — verification cost decreases as skills improve

## Related Papers
- [[automating-formal-verification-with-agent-guided-tree-search-2605.27485]] — Formal verification for agentic tasks (prior art)
- [[causal-reward-world-models-zero-shot-skill-generation-2606.23280]] — Skill generation via world models
- [[agent-skill-evaluation-and-evolution-frameworks-benchmarks-2606.11435]] — Skill evaluation frameworks for LLM agents
