---
title: "AgentGA: Evolving Code Solutions in Agent-Seed Space via Inherited Parent Archives"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [genetic-algorithm, multi-agent, evolutionary, llm, code-generation, cross-agent-teaching]
sources: ["https://arxiv.org/abs/2604.14655"]
---

# AgentGA: Evolving Code Solutions in Agent-Seed Space via Inherited Parent Archives

## Overview
We present AgentGA, a framework that evolves autonomous code-generation runs by optimizing the agent seed: the task prompt plus optional parent archives that initialize a fresh workspace. The outer loop searches over these reusable starting conditions rather than editing code directly. Each generation launches a fresh autonomous run in an isolated workspace, while selected parent archives provide inherited artifacts that descendants can inspect and reuse.

## Key Facts
- **Authors**: not extracted
- **Year**: 2026
- **arXiv**: [2604.14655](https://arxiv.org/abs/2604.14655)

## Key Contributions
- Introduces the **agent-seed-as-cross-agent-teaching-substrate** primitive — for the first time in the wiki, descendants inherit parent archives as the load-bearing teaching channel across a genetic-algorithm population, with the outer loop optimizing over seeds rather than directly editing generated code
- Couples a population-level genetic algorithm with long-horizon agents via deterministic 1:1 elite tournaments and a modified Hedge controller for online operator allocation
- Achieves 71.90% Exceeds % of Human on the 16-competition Weco-Kaggle Lite benchmark vs 51.38% for the AIDE reference (winning 15/16 competitions) — empirically demonstrating the seed-as-teacher primitive
- Shows that descendants conditioned on inherited parent archives win 51.9% of 1,680 parent-child tournaments vs 8.6% for de novo proposals — establishing inherited-archive teaching as the dominant cross-generation transfer mechanism

## Related Papers
- [[group-evolving-agents-open-ended-self-improvement-via-experience-sharing-2602.04837]] — Sibling Run-93 cross-agent-teaching pick (group-as-evolutionary-unit with explicit experience sharing); AgentGA complements via parent-archive inheritance as the load-bearing teaching channel in a genetic-algorithm outer loop
- [[opid-on-policy-skill-distillation-for-agentic-reinforcement-learning-2606.26790]] — Run-65 pick on on-policy skill distillation; AgentGA extends the skill-distillation idea to seed-space transfer where the seed (task prompt + parent archives) is the teaching artifact
- [[externalization-llm-agents-unified-review-memory-skills-protocols-harness-engineering-2604.08224]] — Externalization-as-unifying-primitive survey; AgentGA's parent-archive inheritance is a concrete realization of the externalization principle for cross-generation teaching