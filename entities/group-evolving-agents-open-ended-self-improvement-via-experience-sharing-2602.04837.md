---
title: "Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [self-improvement, multi-agent, evolutionary, llm, experience-sharing, cross-agent-teaching]
sources: ["https://arxiv.org/abs/2602.04837"]
---

# Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing

## Overview
Open-ended self-improving agents can autonomously modify their own structural designs to advance their capabilities and overcome the limits of pre-defined architectures, thus reducing reliance on human intervention. We introduce Group-Evolving Agents (GEA), a new paradigm for open-ended self-improvements, which treats a group of agents as the fundamental evolutionary unit, enabling explicit experience sharing and reuse within the group throughout evolution.

## Key Facts
- **Authors**: not extracted
- **Year**: 2026
- **arXiv**: [2602.04837](https://arxiv.org/abs/2602.04837)

## Key Contributions
- Introduces the **group-as-evolutionary-unit** cross-agent-teaching primitive — for the first time in the wiki, agents within a group act as both teachers and learners via explicit experience sharing across evolutionary branches, overcoming the isolated-branch limitation of tree-structured self-evolution
- Achieves 71.0% on SWE-bench Verified (vs 56.7% for prior SOTA) and 88.3% on Polyglot (vs 68.3%) — empirically demonstrating the load-bearing nature of cross-branch experience sharing for open-ended agent self-improvement
- Matches or exceeds top human-designed agent frameworks (71.8% / 52.0% on two benchmarks) — establishes that group-evolution cross-agent-teaching reaches the ceiling of human-designed architectures
- Demonstrates that GEA exhibits consistent transferability across different coding models and greater robustness, fixing framework-level bugs in 1.4 iterations on average (vs 5 for self-evolving methods without cross-branch experience sharing)

## Related Papers
- [[q-evolve-self-evolving-llm-agents-with-in-distribution-optimization-2606.07367]] — Single-agent self-evolving framework (Run-85 pick) that GEA extends from individual-agent self-improvement to group-evolution cross-agent-teaching
- [[rise-reliable-improvement-in-self-evolving-vision-language-models-2605.20914]] — Run-85 self-evolving VLM pick; GEA broadens the self-evolution primitive to multi-agent population with explicit experience sharing
- [[mutual-reinforcement-learning-experience-sharing-across-heterogeneous-llm-policies-2605.07244]] — Sibling Run-93 cross-agent-teaching pick (peer-teaching via typed outcome certificates); GEA complements via group-evolution peer-teaching across evolutionary branches