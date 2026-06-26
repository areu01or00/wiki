---
title: "LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [formal-math, theorem-proving, agentic-framework, llm]
sources: ["https://arxiv.org/abs/2606.03303"]
---

# LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks

## Overview
LEAP is an agentic framework that lifts general-purpose foundation models (notably non-formal-math-specialized LLMs) to state-of-the-art performance on automated theorem proving in Lean by decomposing formal proof search into a multi-component agent pipeline. The paper isolates where general LLMs fail at formal math — not language comprehension but generating long, structured proof sequences under formal-grammar constraints — and shows that a careful agentic scaffold overcomes the bottleneck.

## Key Facts
- **Authors**: Kung, Po-Nien; Song, Linfeng; Hwang, Dawsen; Yoon, Jinsung
- **Year**: 2026
- **arXiv**: [2606.03303](https://arxiv.org/abs/2606.03303)

## Key Contributions
- Identifies the bottleneck in LLM-based formal theorem proving as the generation of long, mechanically-verifiable Lean proofs (rather than informal language comprehension).
- Introduces LEAP, an agentic framework that orchestrates planning, tactic generation, and verification loops to enable foundation models without specialized formal-math training to compete with theorem-proving-specialized systems.
- Demonstrates state-of-the-art performance on automated theorem proving benchmarks in Lean using general-purpose LLMs behind an agentic scaffold.

## Related Papers
- [[emergent-concepts]] — Parent discovery chain that surfaced this paper
- [[opid-on-policy-skill-distillation-for-agentic-reinforcement-learning-2606.26790]] — Sibling work on on-policy skill-conditioned self-distillation for agentic RL, both about how to make agents learn structured skill sequences from sparse signal
- [[agent-skill-evaluation-and-evolution-frameworks-benchmarks-2606.11435]] — Sibling survey on agent skill evaluation frameworks; LEAP is a concrete instance of an agentic skill pipeline