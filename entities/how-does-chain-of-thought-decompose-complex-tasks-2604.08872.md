---
title: "How does Chain of Thought decompose complex tasks?"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [chain-of-thought, reasoning-decomposition, prompt-engineering, llm-reasoning]
sources: ["https://arxiv.org/abs/2604.08872"]
---

# How does Chain of Thought decompose complex tasks?

## Overview
Models chain-of-thought reasoning as a tree-structured decomposition problem. Shows that CoT-based predictors perform better when they "think deeper" — decomposing problems into more steps — and that classification error scales as a power law in the number of classes. Provides a formal characterization of when CoT decomposition helps vs. when it introduces noise.

## Key Facts
- **Authors**: Nadgir, Amrut; Balasubramanian, Vijay; Chaudhari, Pratik
- **Year**: 2026
- **arXiv**: [2604.08872](https://arxiv.org/abs/2604.08872)

## Key Contributions
- Formalizes CoT as tree-structured task decomposition
- Derives power-law scaling of classification error vs. number of classes
- Characterizes the "thinking depth" tradeoff: more steps = better decomposition but more noise accumulation
- Provides actionable guidance for when to apply CoT vs. direct answering

## Related Papers
- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* (2201.11903) — foundational CoT paper
- *Structured Decomposition for LLM Reasoning* (2601.01609) — cross-domain validation of decomposition approach
