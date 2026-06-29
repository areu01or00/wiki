---
title: "ForEx: A Formal Verification Framework for Explainable Reasoning in Logical Fallacy Detection and Annotation"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, formal-verification, lean4, explanation, evaluation, logical-fallacy]
sources: ["https://arxiv.org/abs/2606.21867"]
arxiv_id: "2606.21867"
---

# ForEx: A Formal Verification Framework for Explainable Reasoning in Logical Fallacy Detection and Annotation

## Overview
First paper in the wiki to introduce *machine-checkable analysis of formalized reasoning chains* as an LLM evaluation primitive by translating LLM-generated explanations into Lean4 and verifying whether the translated rationale is derivable under encoded premises — surfacing *explanation-as-formal-proof-primitive* and the *label-vs-derivability gap* as load-bearing primitives for moving LLM evaluation beyond label correctness. Distinguishes prediction outcomes from the formal status of the supporting reasoning via the LLM Argument Verification Matrix (LAVM), which separates label consistency from formal verification status.

## Key Facts
- **Authors**: Huang, Pei-Cing; Liu, Chienyu; Hsu, Chan; Chen, Ci-Siang; Lee, Pei-Ju; Kang, Yihuang
- **Year**: 2026
- **arXiv**: [2606.21867](https://arxiv.org/abs/2606.21867)
- **Online date**: 2026-06-20

## Key Contributions
- **Lean4 translation pipeline**: converts LLM-generated natural-language explanations into Lean4 propositions and verifies derivability under encoded premises — bridging the natural-language reasoning and proof-assistant worlds as a first-class LLM evaluation primitive.
- **LLM Argument Verification Matrix (LAVM)**: separates label consistency from formal verification status, exposing the systematic gap between what an LLM claims and what can be formally derived from its claimed premises.
- **Empirical exposure of label-vs-derivability gap**: on LOGIC-Climate, over 90% of LLM outputs can be translated into formal reasoning chains that pass verification, while agreement with human annotations remains around 20% — exposing a label-derivability gap invisible to prediction-based metrics.
- **Evaluation paradigm shift**: moves LLM evaluation beyond label correctness toward machine-checkable analysis of formalized reasoning chains, establishing *formal-derivation-status* as a primitive alongside accuracy and human-agreement.

## Related Papers
- [[leap-supercharging-llms-for-formal-mathematics-with-agentic-frameworks-2606.03303]] — Sibling LLM-for-formal-math paper using agentic frameworks; ForEx specifically targets Lean4 verification of natural-language explanations
- [[ma-proofbench-a-two-tiered-evaluation-of-llms-for-theorem-proving-in-mathematica-2606.13782]] — Benchmark for LLMs in theorem proving; ForEx adds the verification-of-explanation axis rather than proof generation
- [[logicgraph-benchmarking-multi-path-logical-reasoning-via-neuro-symbolic-generation-and-verification-2602.21044]] — Multi-path logical reasoning via neuro-symbolic verification
- [[veribound-pac-bayesian-generalization-bounds-for-process-reward-models-trained-with-formal-verification-tools-2606.20740]] — Process reward models trained with formal-verification tools
- [[verytrace-verifying-reasoning-traces-through-compilable-formalism-2606.24124]] — Run 96 sibling: DSL-based trace verification; ForEx uses Lean4 rather than a domain-specific language
- [[formalizing-latent-thoughts-four-axioms-of-thought-representation-in-llms-2606.27378]] — Run 96 sibling: formalizes latent thoughts via axioms; ForEx formalizes natural-language explanations via Lean4