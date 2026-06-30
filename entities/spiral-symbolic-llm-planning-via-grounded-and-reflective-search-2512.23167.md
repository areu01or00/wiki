---
title: "SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [planning, symbolic-reasoning, llm-agents]
sources: ["https://arxiv.org/abs/2512.23167"]
---

# SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search

## Overview
SPIRAL addresses the failure mode where LLMs falter at complex planning tasks requiring exploration and self-correction, as their linear reasoning process struggles to recover from early mistakes. The framework embeds a cognitive architecture of three specialized LLM agents into a Monte Carlo Tree Search loop, enabling symbolic planning with self-correction through grounded and reflective search.

## Key Facts
- **Authors**: Yifan Zhang, Giridhar Ganapavarapu, Srideepika Jayaraman, Bhavna Agrawal, Dhaval Patel, Achille Fokoue
- **Year**: 2025
- **arXiv**: [2512.23167](https://arxiv.org/abs/2512.23167)

## Key Contributions
- Three specialized LLM agents embedded in MCTS loop for symbolic planning
- Grounded and reflective search enables self-correction that pure LLM linear reasoning cannot achieve
- Addresses sparse reward failure in MCTS by leveraging rich semantic capabilities of LLMs
- Novel cognitive architecture integration — symbolic search + LLM semantic reasoning

## Related Papers
- [[think2-grounded-metacognitive-reasoning-in-large-language-models-2602.18806]] — Metacognitive reasoning (orthogonal: regulatory-cycle introspection vs. search-based planning)
- [[do-agents-think-deeper-mechanistic-investigation-layer-wise-dynamics-sequential-planning-2605.27935]] — Sequential planning in agents (orthogonal: SPIRAL's cognitive-architecture-MCTS approach vs. mechanistic layer-wise investigation)
