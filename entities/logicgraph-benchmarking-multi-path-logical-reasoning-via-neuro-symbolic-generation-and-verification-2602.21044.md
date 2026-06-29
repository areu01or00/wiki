---
title: "LogicGraph: Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [neuro-symbolic, llm, benchmark, multi-path-reasoning, logical-reasoning, divergent-reasoning]
sources: ["https://arxiv.org/abs/2602.21044"]
---

# LogicGraph: Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification

## Overview
Wu, Zhang, Zhang and colleagues introduce LogicGraph, the first benchmark aimed at systematically evaluating *multi-path logical reasoning* — the divergent logical reasoning capability needed when a problem admits multiple valid derivations. The benchmark is constructed via a neuro-symbolic framework that combines *backward logic generation* and *semantic instantiation*, producing solver-verified reasoning problems formalised by high-depth multi-path reasoning and inherent logical distractions, where each instance is associated with an exhaustive set of minimal proofs.

## Key Facts
- **Authors**: Wu, Yanrui; Zhang, Lingling; Zhang, Xinyu et al.
- **Year**: 2026
- **arXiv**: [2602.21044](https://arxiv.org/abs/2602.21044)
- **Online date**: 2026-02-24

## Key Contributions
- **Multi-path logical reasoning benchmark**: LogicGraph targets *divergent* logical reasoning — problems admitting multiple valid derivations — distinct from convergent-reasoning benchmarks that only evaluate whether a model can produce a single correct proof. Each instance is paired with an *exhaustive set of minimal proofs*, enabling reference-free multi-path-coverage evaluation.
- **Neuro-symbolic construction pipeline**: backward logic generation + semantic instantiation produces *solver-verified reasoning problems* — every problem in the benchmark is mechanically verified by an external solver. High-depth multi-path reasoning with inherent logical distractions makes the benchmark robust to shortcut exploitation.
- **Reference-free evaluation framework**: a unified metric that *rigorously assesses model performance in both convergent and divergent regimes* — measuring not just proof correctness on a single derivation but the model's ability to discover all minimal proofs of an instance.
- **Empirical finding of "divergence gap"**: state-of-the-art LLMs tend to *commit early to a single proof route and fail to explore alternatives*; coverage gap grows substantially with reasoning depth — surfacing a structural LLM failure mode where the LLM's path-commitment behaviour systematically under-explores multi-path spaces.

## Related Papers
- [[the-lattice-representation-hypothesis-of-large-language-models-2603.01227]] — Run 79 sibling — Lattice Representation Hypothesis unifies Linear Representation Hypothesis with Formal Concept Analysis via *concept-lattice structure in embedding geometry*; LogicGraph exposes *multi-path logical structure* via solver-verified backward generation. Together they bracket the *symbolic-structure-in-LLM-reasoning* surface between symbolic-structure-as-embedding-geometry and symbolic-structure-as-benchmark-ground-truth primitives.
- [[delta1-with-llm-symbolic-neural-integration-for-credible-and-explainable-reasoning-2603.12953]] — Run 80 sibling — Δ₁–LLM integrates *Full Triangular Standard Contradiction* theorem generation with LLM verbalization for explainability-by-construction; LogicGraph provides *neuro-symbolic benchmark for multi-path reasoning*. Together they bracket the *neuro-symbolic-construction* surface between automated-theorem-generation-with-LLM-verbalization and benchmark-generation-with-solver-verification primitives.
- [[ma-proofbench-a-two-tiered-evaluation-of-llms-for-theorem-proving-in-mathematica-2606.13782]] — Run 74 sibling — MA-ProofBench evaluates LLM theorem-proving in Mathematica via *proof-step correctness* (Tier 1) and *full-proof correctness* (Tier 2); LogicGraph evaluates via *multi-path-coverage-and-divergent-reasoning*. Together they bracket the *LLM-formal-theorem-reasoning-evaluation* surface between single-proof-correctness and multi-path-divergent-reasoning primitives.
- [[calvert-augmenting-agents-with-calibrated-verifier-telemetry-improves-action-and-learning-in-knowledge-intensive-tasks-2606.21777]] — sibling — CalVERT introduces *calibrated verifier telemetry* as an action-and-learning primitive for knowledge-intensive agents; LogicGraph uses *external solver verification* as a benchmark-construction primitive. Together they bracket the *verifier-as-infrastructure* surface between verifier-as-agent-telemetry (CalVERT) and verifier-as-benchmark-construction (LogicGraph) primitives.
- [[sequential-consensus-for-multi-agent-llm-debates-a-wald-sprt-compute-governor-with-calibration-based-failure-detection-2605.19193]] — Run 78 sibling — Sequential-Consensus exposes a structural finding that LLM debate tends to *converge on a single answer via SPRT termination*; LogicGraph exposes a structural finding that LLM logical reasoning tends to *commit early to a single proof route*. Together they bracket the *single-path-commitment-failure-mode* surface between consensus-convergence and reasoning-convergence primitives — both surface path-commitment as a structural LLM limitation requiring different remediation strategies (adaptive-compute-governor vs multi-path-coverage-evaluation).
- [[emergent-concepts]] — parent wiki page

## Theme
neuro-symbolic-grounding / multi-path-reasoning / divergent-reasoning / backward-logic-generation / semantic-instantiation / solver-verified-benchmark / reference-free-evaluation / divergence-gap-failure-mode / early-path-commitment

**First neuro-symbolic multi-path logical reasoning benchmark with reference-free evaluation framework and exhaustive-minimal-proof coverage in the wiki.** Verified via `ls entities/ | grep -iE "(logicgraph|multi.path.logical|divergent.reasoning|backward.logic.gen|minimal.proof.set|divergence.gap)"` returning empty.