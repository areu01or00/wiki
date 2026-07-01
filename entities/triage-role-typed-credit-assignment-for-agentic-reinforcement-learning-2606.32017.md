---
title: "TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agentic-rl, credit-assignment, multi-agent, reinforcement-learning]
sources: ["https://arxiv.org/abs/2606.32017"]
---

# TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning

## Overview
TRIAGE addresses a core structural weakness in agentic RL: standard GRPO assigns uniform advantage to all action tokens based only on the final verifier outcome, ignoring that environment-facing actions (searches, clicks, edits, navigation) have heterogeneous causal weight. TRIAGE introduces role-typed credit assignment where each action class gets its own advantage estimate, enabling agents to learn which exploratory actions drive success even in failed rollouts.

## Key Facts
- **Authors**: Xu, Yuanda; Zhou, Zhengze; Sang, Hejian + 5
- **Year**: 2026
- **arXiv**: [2606.32017](https://arxiv.org/abs/2606.32017)

## Key Contributions
- Role-typed credit assignment separating environment-facing actions (search, click, edit, navigation) from internal reasoning tokens
- Per-role advantage estimation replacing uniform GRPO credit
- Demonstrates that role-typed credit recovers useful exploration signal from failed rollouts where outcome supervision fails
- First credit-assignment primitive that distinguishes action types within agentic RL loops

## Related Papers
- *Escaping the Self-Confirmation Trap* (2606.24428) — Execute-Distill-Verify paradigm for agentic experience learning; TRIAGE builds on the insight that failed rollouts contain learnable signal by assigning per-action credit *(not yet in wiki)*
- [[agentic-reasoning-for-large-language-models-2601.12538]] — Agentic reasoning foundational framework; TRIAGE extends this by decomposing the action-level credit structure that agentic reasoning depends on
