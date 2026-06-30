---
title: "Be Your Own Red Teamer: Safety Alignment via Self-Play and Reflective Experience Replay"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [safety, alignment, red-teaming, adversarial, llm]
sources: ["https://arxiv.org/abs/2601.10589"]
---

# Be Your Own Red Teamer: Safety Alignment via Self-Play and Reflective Experience Replay

## Overview
Current safety alignment depends on static external red teaming — fixed defense prompts or pre-collected adversarial datasets — leading to rigid defenses that overfit known patterns and fail against novel attacks. This paper proposes Safety Self-Play (SSP), where a single LLM acts simultaneously as Attacker (generating evolving jailbreaks) and Defender (refusing harmful requests) within a unified RL loop. A Reflective Experience Replay Mechanism with UCB sampling focuses on failure cases, enabling the model to learn from past hard mistakes while balancing exploration and exploitation.

## Key Facts
- **Authors**: Unnamed (arXiv 2601.10589)
- **Year**: 2026
- **arXiv**: [2601.10589](https://arxiv.org/abs/2601.10589)

## Key Contributions
- Safety Self-Play (SSP): single LLM as concurrent Attacker-Defender in unified RL loop for autonomous evolving adversarial attacks
- Reflective Experience Replay with UCB sampling focuses learning on low-reward failure cases from past hard mistakes
- Dynamically evolves attack strategies while simultaneously strengthening defense mechanisms
- Outperforms baselines trained on static adversarial datasets; establishes new benchmark for proactive safety alignment

## Related Papers
- [[muzzle-adaptive-agentic-red-teaming-web-agents-indirect-prompt-injection-attacks-2602.09222]] — Adaptive agentic red teaming for web agent attack surfaces (different attack surface)
- [[ajar-adaptive-jailbreak-architecture-red-teaming-2601.10971]] — Adaptive jailbreak architecture for systematic red teaming evaluation
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — Safety alignment characterization: refusal instability in aligned LLMs
