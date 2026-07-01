---
title: "NRT-Bench: Benchmarking Multi-Turn Red-Teaming of LLM Operator Agents in Safety-Critical Control Rooms"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [LLM agents, safety, red-teaming, multi-agent, adversarial robustness, safety-critical systems]
sources: ["https://arxiv.org/abs/2606.20408"]
---

# NRT-Bench: Benchmarking Multi-Turn Red-Teaming of LLM Operator Agents in Safety-Critical Control Rooms

## Overview
NRT-Bench is a benchmark for multi-turn red-teaming of LLM agents acting as operators of safety-critical systems, instantiated in a simulated nuclear power plant control room. Five LLM-backed operator roles govern six critical safety functions (CSFs) while adversaries inject messages over four channels in bounded multi-turn sessions. Harm is an objective signal (CSF loss), not LLM-judged text. Key finding: vulnerabilities are nearly disjoint across models — of 149 sessions, none defeat all four models while a third defeat at least one. Defences are strongly model-dependent: the same guardrail stack that lowers attack success for one model can raise it for another.

## Key Facts
- **Year**: 2026
- **arXiv**: [2606.20408](https://arxiv.org/abs/2606.20408)

## Key Contributions
- First multi-turn red-teaming benchmark for LLM agents in safety-critical control rooms
- Five-role operator team, six CSFs, four attack channels, per-turn feedback
- Objective harm signal (CSF loss) rather than LLM-judged text
- Finding: 8.7–12.1% of attack sessions end with plant losing a critical safety function across four frontier models
- Finding: model vulnerabilities are nearly disjoint — no single attack defeats all four models
- Finding: defensive interventions are strongly model-dependent — same guardrail raises ASR for some models
- Simulation venue, attack dataset, and replay tooling released

## Related Papers
- [[ajar-adaptive-jailbreak-architecture-red-teaming-2601.10971]] — Adaptive jailbreak architecture red-teaming (orthogonal: AJAR focuses on jailbreak defense; NRT-Bench focuses on multi-turn red-teaming of operator agents in safety-critical control room settings)
- [[be-your-own-red-teamer-safety-alignment-via-self-play-and-reflective-experience-replay-2601.10589]] — Self-play red-teaming for safety alignment (orthogonal: focuses on self-play for alignment; NRT-Bench focuses on external adversarial pressure on operator agents)
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — Geometric analysis of refusal instability in safety-aligned LLMs (orthogonal: studies refusal geometry in standalone LLMs; NRT-Bench studies multi-turn adversarial pressure on LLM operator agents in safety-critical environments)
