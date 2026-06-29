---
title: "Belief or Circuitry? Causal Evidence for In-Context Graph Learning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [causal-reasoning, in-context-learning, mechanistic-interpretability, llm]
sources: ["https://arxiv.org/abs/2605.08405"]
---

# Belief or Circuitry? Causal Evidence for In-Context Graph Learning

## Overview
How do LLMs learn in-context — by pattern-matching recent tokens or by inferring latent graph structure? The authors use a toy graph random-walk task with two competing graph structures where the answer is in principle decidable: either the model tracks global topology or copies local transitions. Causal intervention experiments show neither account alone is sufficient — LLMs exhibit a hybrid mechanism that integrates both causal structure inference and token-level pattern matching.

## Key Facts
- **Authors**: Katharine Kowalyshyn, Timothy Duggan, Daniel Little, Michael C Hughes
- **Year**: 2026
- **arXiv**: [2605.08405](https://arxiv.org/abs/2605.08405)

## Key Contributions
- **Causal intervention design** using graph topology manipulation to isolate mechanism (pattern-matching vs structure inference)
- **Hybrid mechanism evidence** — neither pure pattern-matching nor pure causal inference; models integrate both
- **Tool for diagnosing in-context learning** — randomised graph structures can expose the underlying mechanism in any LLM
- **First "causal vs statistical" decomposition for in-context learning** in LLMs via graph-walk methodology

## Related Papers
- [[causality-is-key-for-interpretability-claims-to-generalise-2602.16698]] — Framework for valid causal mapping from activations to high-level structures; positions this paper's causal interventions as the correct methodology for interpretability
- [[emergent-causal-geometric-dynamics-across-depth-in-large-language-models-2602.04931]] — Depth-dependent causal geometry; the graph-walk topology-tracking mechanism may have a depth profile
