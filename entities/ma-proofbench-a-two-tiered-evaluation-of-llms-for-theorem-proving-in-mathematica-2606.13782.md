---
title: "MA-ProofBench: A Two-Tiered Evaluation of LLMs for Theorem Proving in Mathematical Analysis"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [evaluation, formal-verification, theorem-proving, math-reasoning, llm, benchmark, cross-discipline]
sources: ["https://arxiv.org/abs/2606.13782"]
---

# MA-ProofBench: A Two-Tiered Evaluation of LLMs for Theorem Proving in Mathematical Analysis

## Overview
First benchmark in the wiki to systematically evaluate LLM theorem provers in **mathematical analysis** specifically (real-variable calculus, metric spaces, sequences, series) — a notoriously harder-to-formalize subdomain than the algebra/number-theory focus of prior benchmarks. Introduces a two-tiered difficulty partition (textbook exercises vs research-level analysis problems) and shows most current models perform poorly on the harder tier, surfacing analysis as a frontier.

## Key Facts
- **Authors**: Pu, Lushi; Zhang, Weiming; Xie, Xinheng; Fu, Zixuan et al.
- **Year**: 2026
- **arXiv**: [2606.13782](https://arxiv.org/abs/2606.13782)
- **Online Date**: 2026-06-15
- **Domain**: formal verification × mathematical analysis × LLM evaluation

## Key Contributions
- **Mathematical-analysis-specific theorem-proving benchmark**: targets real-variable calculus, metric spaces, sequences/series, and other analysis subdomains that are underrepresented in existing formal benchmarks (which skew toward algebra and elementary number theory)
- **Two-tiered difficulty partition**: separates textbook exercises (more formulaic, easier to formalize) from research-level analysis problems (require deeper conceptual understanding of limit-based reasoning), enabling separate evaluation of "rote formalization" vs "conceptual analysis reasoning"
- **Most current models perform poorly on the harder tier**: shows that prior benchmarks may have overestimated LLM theorem-proving capability by concentrating on easier-to-formalize domains; analysis is a frontier where reasoning models struggle
- **Cross-discipline primitive**: bridges formal-verification × mathematical-analysis × LLM-evaluation — a triple that prior benchmarks did not address, surfacing analysis-reasoning as a structurally distinct evaluation axis from algebra-reasoning

## Related Papers
- [[maxproof-scaling-mathematical-proof-with-generative-verifier-rl-and-population-level-test-time-scaling-2606.13473]] — Sibling from Run 72 that scales mathematical-proof generation with RL + generative verifier + test-time scaling
- [[leap-supercharging-llms-for-formal-mathematics-with-agentic-frameworks-2606.03303]] — Earlier benchmark exploring agentic frameworks for formal mathematics; MA-ProofBench extends the evaluation domain into analysis
- [[when-the-chain-of-thought-knows-better-failure-modes-in-multi-turn-reasoning-models-2606.10740]] — Run 60 cross-discipline primitive on CoT-monitorability and oversight paradox; complements MA-ProofBench's analysis-frontier finding
- [[a-survey-of-on-policy-distillation-for-large-language-models-2604.00626]] — Run 65 cross-discipline primitive on capability-transfer primitives via on-policy distillation; relevant to theorem-proving training-method primitives
- [[a-theoretical-model-for-task-routing-in-mixture-of-expert-transformers-2606.14398]] — Run 62 primitive on theoretical task-routing; relevant to multi-tier theorem-prover architectures