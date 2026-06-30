---
title: "Decompose-ToM: Enhancing Theory of Mind Reasoning in Large Language Models through Simulation and Task Decomposition"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [theory-of-mind, cognitive-simulation, llm-reasoning]
sources: ["https://arxiv.org/abs/2501.09056"]
---

# Decompose-ToM: Enhancing Theory of Mind Reasoning in Large Language Models through Simulation and Task Decomposition

## Overview
Decompose-ToM applies cognitive psychology's "Simulation Theory" to LLM-based Theory of Mind reasoning. The approach recursively simulates user perspectives and decomposes complex ToM tasks into simpler functions: subject identification, question-reframing, world model updation, and knowledge availability. This enables LLMs to handle higher-order ToM tasks and conversational ToM that baseline prompting fails on.

## Key Facts
- **Authors**: Sneheel Sarangi, Maha Elgarf, Hanan Salam
- **Year**: 2025
- **arXiv**: [2501.09056](https://arxiv.org/abs/2501.09056)

## Key Contributions
- Pretend-play / Simulation Theory as an LLM inference algorithm for ToM
- Recursive perspective simulation decomposed into 4 functional sub-tasks
- Minimal prompt tuning across tasks, no additional model training required
- Significant improvement on higher-order ToM tasks and conversational ToM benchmarks
- First simulation-theory-driven ToM enhancement in the wiki

## Related Papers
- [[osctom-rl-guided-adversarial-generation-for-high-order-theory-of-mind-2605.20423]] — RL-guided adversarial ToM generation targeting nested belief conflicts
- [[mindgames-a-live-arena-for-evaluating-social-and-strategic-reasoning-in-multi-agent-llms-2605.29512]] — Live arena evaluation of ToM in multi-agent social/strategic settings
- [[socialmembench-are-ai-memory-systems-ready-for-social-group-settings-2605.17789]] — ToM benchmark for AI memory systems in social group contexts
- [[think2-grounded-metacognitive-reasoning-in-large-language-models-2602.18806]] — Metacognitive regulatory cycle as prompting architecture (complementary to simulation-theory approach)
- [[cognitive-llms-towards-integrating-cognitive-architectures-and-large-language-models-2408.09176]] — Systematic integration of Soar/ACT-R cognitive architectures with LLMs (broader cognitive theory context)
