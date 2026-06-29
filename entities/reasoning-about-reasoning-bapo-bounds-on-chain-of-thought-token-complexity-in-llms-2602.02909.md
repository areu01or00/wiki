---
title: "Reasoning about Reasoning: BAPO Bounds on Chain-of-Thought Token Complexity in LLMs"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning-theory, cot-complexity, lower-bounds, bapo, inference-time-compute, cognitive-load]
sources: ["https://arxiv.org/abs/2602.02909"]
authors: ["Kiran Tomlinson", "Tobias Schnabel", "Adith Swaminathan", "Jennifer Neville"]
---

# Reasoning about Reasoning: BAPO Bounds on Chain-of-Thought Token Complexity in LLMs

## Overview
Extends the Bounded Attention Prefix Oracle (BAPO) abstraction to prove formal lower bounds on the number of chain-of-thought tokens required to solve three canonical reasoning tasks (binary majority, triplet matching, graph reachability), establishing that each requires Ω(n) reasoning tokens for input size n. Validates the theoretical bounds empirically with frontier reasoning models, where approximately linear CoT-token scaling is observed with failures when reasoning budgets are constrained.

## Key Facts
- **Authors**: Kiran Tomlinson, Tobias Schnabel, Adith Swaminathan, Jennifer Neville
- **Year**: 2026 (submission 2026-02-02, online 2026-05-27)
- **arXiv**: [2602.02909](https://arxiv.org/abs/2602.02909)
- **Submission**: 2026/02/02
- **Online**: 2026/05/27

## Key Contributions
- Extends the BAPO model (a theoretical abstraction quantifying information flow required to solve a task) to derive Θ-notation lower bounds on CoT tokens for canonical hard tasks.
- Proves Ω(n) lower bounds for binary majority, triplet matching, and graph reachability — establishing that each of these tasks fundamentally requires a linear number of reasoning tokens.
- Provides matching or near-matching upper bounds via explicit constructions for the same tasks.
- Empirically validates linear CoT-token scaling on frontier reasoning models (with constrained-budget failures matching the theoretical bounds).
- Introduces *fundamental-bottleneck-of-inference-time-compute identification* and *optimal-reasoning-length principled analysis* as primitives for reasoning-system design.

## Related Papers
- [[uncovering-the-representation-geometry-of-minimal-cores-in-overcomplete-reasoning-traces-2605.14358]] — Sibling Run 103 paper probing the same CoT-reasoning-trace primitive layer (minimal-cores as overcomplete-trace representation geometry)
- [[off-the-shelf-llms-as-process-scorers-training-free-prm-alternative-chunk-level-guided-generation-2606.01682]] — Training-free process-reward-model alternative probing chunk-level cognitive-budget primitives
- [[adaptive-test-time-compute-allocation-for-reasoning-llms-via-constrained-policy-optimization-2604.14853]] — Complementary test-time compute allocation primitive probing policy-optimization for reasoning-token budgets
- [[safe-few-step-generation-via-velocity-editing-2606.23267]] — Sibling inference-time step-budget primitive via velocity editing
- [[lgmt-logic-grounded-metamorphic-testing-for-llm-reasoning-reliability-2605.23965]] — Sibling reasoning-reliability primitive from Run 102 invariance probe (logical-equivalence-based oracle-free consistency checking)
- [[local-causal-attribution-of-chain-of-thought-reasoning-2606.21821]] — Local causal-attribution primitive for CoT reasoning (sibling reason-trace attribution primitive)
