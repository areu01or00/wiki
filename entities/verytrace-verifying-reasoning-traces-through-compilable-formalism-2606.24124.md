---
title: "VeryTrace: Verifying Reasoning Traces through Compilable Formalism and Structured Verification"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, formal-verification, dsl, trace-verification, process-reward]
sources: ["https://arxiv.org/abs/2606.24124"]
arxiv_id: "2606.24124"
---

# VeryTrace: Verifying Reasoning Traces through Compilable Formalism and Structured Verification

## Overview
First paper in the wiki to introduce a zero-shot verification-and-repair framework that formalizes natural-language reasoning traces into a structured, compilable representation via a Domain-Specific Language (DSL) and verifies them with a hybrid deterministic-plus-LLM-audit verifier — establishing *trace-as-compilable-program* as a load-bearing formal-foundation primitive for LLM reasoning reliability. Multi-step Chain-of-Thought reasoning remains fragile because logical errors and hallucinations in early steps silently propagate, producing confident but incorrect conclusions; VeryTrace exposes these failure modes through structured compilation and step-level repair without domain-specific training or in-context examples.

## Key Facts
- **Authors**: Zhong, Ninghan; Tanriverdi, Ahmet Ege; Kale, Kaan; Vishwanath, Sriram
- **Year**: 2026
- **arXiv**: [2606.24124](https://arxiv.org/abs/2606.24124)
- **Online date**: 2026-06-23

## Key Contributions
- **Domain-Specific Language for reasoning traces**: introduces a DSL that (i) makes step dependencies explicit, (ii) mechanizes quantitative content as executable expressions, and (iii) structures semantic inferences via deduction schemas (direct entailment, modus ponens, transitivity, case analysis), ensuring even "soft" steps have explicit form and declared premises.
- **Hybrid verification framework**: combines deterministic checks for computational correctness, dependency resolution, and constraint satisfaction with targeted LLM audits for non-mechanizable semantic judgments, enabling step-level error localization and repair.
- **Zero-shot transfer across domains**: improves accuracy on competition mathematics (AIME 2025), robotics planning (LLM-BabyBench), and kinship reasoning (CLUTRR) without requiring domain-specific training or in-context examples — demonstrating that formalized trace verification achieves both precision and generalization.
- **Iterative repair loop**: when the LLM audit detects a soft-step error, the framework prompts the LLM to iteratively repair the reasoning trace under the DSL's well-formedness constraints — surfacing *trace-repair-as-compilation-recovery* as the load-bearing mechanism for converting formalization failures into verified repairs.

## Related Papers
- [[local-causal-attribution-of-chain-of-thought-reasoning-2606.21821]] — Sibling paper that attributes CoT errors to causal-local interventions; VeryTrace formalizes the trace itself for verification, complementing causal-localization
- [[reasoning-models-struggle-to-control-their-chains-of-thought-2603.05706]] — Surfaces the controllability gap VeryTrace addresses by making traces formally auditable
- [[lifting-traces-to-logic-programmatic-skill-induction-with-neuro-symbolic-learning-for-long-horizon-agentic-tasks-2605.01293]] — Programmatic trace lifting to logic; VeryTrace generalizes this to verification across multiple domains
- [[formalizing-latent-thoughts-four-axioms-of-thought-representation-in-llms-2606.27378]] — Run 96 sibling: formalizes latent thoughts via axioms rather than via compilable programs
- [[forex-a-formal-verification-framework-for-explainable-reasoning-in-logical-fallacy-detection-and-annotation-2606.21867]] — Run 96 sibling: Lean4 verification of LLM explanations; VeryTrace uses a DSL rather than a general proof assistant
- [[from-agent-traces-to-trust-a-survey-of-evidence-tracing-and-execution-provenance-in-llm-agents-2606.04990]] — Survey of trace verification across LLM agents