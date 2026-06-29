---
title: "CausalFlow: Causal Attribution and Counterfactual Repair for LLM Agent Failures"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, causal-reasoning, agent-failure, counterfactual]
sources: ["https://arxiv.org/abs/2605.25338"]
---

# CausalFlow: Causal Attribution and Counterfactual Repair for LLM Agent Failures

## Overview
CausalFlow is an interventional framework that converts failed LLM agent traces into minimal counterfactual repairs and reusable supervision. It models execution traces as sequential chains of dependent steps, computes Causal Responsibility Scores (CRS) via step-level counterfactual intervention to identify failure-inducing steps, and generates minimally edited repairs that flip the final outcome to success — producing validated contrastive pairs of the form (wrong step, corrected step).

## Key Facts
- **Authors**: Akash Bonagiri, Devang Borkar, Gerard Janno Anderias, Setareh Rafatirad, Houman Homayoun
- **Year**: 2026
- **arXiv**: [2605.25338](https://arxiv.org/abs/2605.25338)
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
- **Submitted**: 2026-05-25

## Key Contributions
- **Causal Responsibility Scores (CRS)**: Step-level counterfactual intervention quantifies which specific execution step caused the failure, rather than treating the failure as a monolithic outcome.
- **Minimal Counterfactual Repair Generation**: Generates minimally edited repairs that flip the final outcome to success, producing validated contrastive (wrong, corrected) pairs suitable for offline preference optimization or reward modeling.
- **Dual-Use Framework**: Supports both test-time repair (recovers from failures with minimal behavioral drift) and training-time supervision (converts failures into learning-ready data).
- **Causal Consensus**: Demonstrates that causal attribution is necessary for reliable improvement — heuristic refinement fails in complex retrieval settings while CausalFlow produces more localized, causally-consistent repairs.

## Related Papers
- [[pragrest-self-reinforcing-counterfactual-reasoning-for-pragmatic-language-understanding-2606.18624]] — PragReST surfaces counterfactual traces for pragmatic inference (sibling from Run 122)
- [[the-table-says-otherwise-testing-llms-with-counterfactual-relational-data-2606.23667]] — ContraTable provides counterfactual-db-pairs for table-QA faithfulness
- [[hidden-in-memory-sleeper-memory-poisoning-in-llm-agents-2605.15338]] — Sleeper Memory Poisoning (Run 124) covers agent memory contamination; CausalFlow covers counterfactual repair of agent execution failures
