---
title: "Diagnosing Task Insensitivity in Language Agents"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agent, evaluation, llm, robustness]
sources: ["https://arxiv.org/abs/2606.26918"]
---

# Diagnosing Task Insensitivity in Language Agents

## Overview
Large language models can serve as long-horizon agents, but their out-of-distribution generalization is brittle — specifically, they exhibit task insensitivity: failing to adapt behavior when task constraints shift mid-execution. This paper systematically diagnoses task insensitivity by constructing contrastive evaluation episodes where minor task parameter changes (budget, tools available, environmental state) should trigger behavioral adaptation. The diagnosis reveals that current LLM agents conflate task identity with surface-level context, missing deep constraint reasoning.

## Key Facts
- **Authors**: Liu, Jingyu; Wu, Xiaopeng; Chen, Kehan + 2
- **Year**: 2026
- **arXiv**: [2606.26918](https://arxiv.org/abs/2606.26918)

## Key Contributions
- Defines and measures task insensitivity as a distinct failure mode from standard OOD brittleness
- Constructs contrastive agent episodes that isolate task constraint adaptation from general capability
- Shows that instruction-tuned agents fail on subtle task shifts even when full task descriptions are provided
- Proposes a diagnostic benchmark and identifies which architectural changes improve task sensitivity

## Related Papers
- Emergent discovery — no prior parent paper; this work contributes a new agent evaluation primitive to the wiki.
