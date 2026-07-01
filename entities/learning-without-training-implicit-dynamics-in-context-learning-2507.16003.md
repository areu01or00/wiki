---
title: "Learning without training: The implicit dynamics of in-context learning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [in-context-learning, theory, mechanism-analysis, llm]
sources: ["https://arxiv.org/abs/2507.16003"]
---

# Learning without training: The implicit dynamics of in-context learning

## Overview
Investigates the implicit algorithmic mechanisms by which transformers implement in-context learning (ICL) without weight updates. The paper analyzes how transformers emulate multi-step gradient descent and algorithm execution purely through prompt-context dynamics, bridging the gap between ICL behavior and the underlying in-weight representations that enable it.

## Key Facts
- **Authors**: Dherin, Benoit; Munn, Michael; Mazzawi, Hanna + 2
- **Year**: 2025
- **arXiv**: [2507.16003](https://arxiv.org/abs/2507.16003)

## Key Contributions
- Characterizes ICL as implicit algorithmic emulation (not mere pattern matching)
- Shows transformers implement multi-step gradient descent via chain-of-thought-like intermediate computations
- Provides theoretical framework for when ICL succeeds vs. fails based on task structure
- Demonstrates the duality: ICL and in-weight learning (IWL) are competingreprsentations

## Related Papers
- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* (2201.11903) — foundational CoT reasoning paper
- *Reconciling In-Context and In-Weight Learning via Dual Representation* (2603.13459) — explores ICL vs IWL duality
