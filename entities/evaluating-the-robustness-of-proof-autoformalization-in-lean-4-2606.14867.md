---
title: "Evaluating the Robustness of Proof Autoformalization in Lean 4"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning, formal-verification, theorem-proving, evaluation]
sources: ["https://arxiv.org/abs/2606.14867"]
---

# Evaluating the Robustness of Proof Autoformalization in Lean 4

## Overview
Proof autoformalization translates informal mathematical proofs written in natural language into formal proofs in proof assistants like Lean 4. This paper evaluates the robustness of LLM-based autoformalization systems — testing not just well-formed proofs from curated datasets but also informal proofs with gaps, ambiguous notation, and non-standard structuring that appear in real submissions. The key finding: current models degrade significantly on noisy informal proofs, revealing brittleness that benchmarks from clean datasets miss.

## Key Facts
- **Authors**: Gui, Zhengtao; Yang, Sheng; Shi, Zhouxing
- **Year**: 2026
- **arXiv**: [2606.14867](https://arxiv.org/abs/2606.14867)

## Key Contributions
- Robustness benchmark for proof autoformalization (clean vs noisy informal proofs)
- Evaluation of LLM-based autoformalization models on non-standard proof structures
- Reveals systematic brittleness: models perform well on curated datasets but degrade on real-world informal proofs with gaps, ambiguous notation, or non-standard structuring
- Analysis of failure modes relevant to deploying autoformalization in live mathematical research workflows

## Related Papers
- [[process-verified-reinforcement-theorem-proving-lean-2606.20068]] — Process-verified approach to Lean theorem proving via RL
- [[formalizing-latent-thoughts-four-axioms-of-thought-representation-in-llms-2606.27378]] — Axiomatic framework for thought representation, relevant to the LLM reasoning that underlies autoformalization
- [[leap-supercharging-llms-for-formal-mathematics-with-agentic-frameworks-2606.03303]] — Agentic framework for formal mathematics, complementary evaluation perspective
