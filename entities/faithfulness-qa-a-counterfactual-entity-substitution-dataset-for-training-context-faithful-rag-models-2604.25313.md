---
title: "Faithfulness-QA: A Counterfactual Entity Substitution Dataset for Training Context-Faithful RAG Models"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [rag, faithfulness, training-data, counterfactual, entity-substitution, retrieval-augmented-generation, hallucination, parametric-memory, llm]
sources: ["https://arxiv.org/abs/2604.25313"]
---

# Faithfulness-QA: A Counterfactual Entity Substitution Dataset for Training Context-Faithful RAG Models

## Overview
Introduces **Faithfulness-QA**, a large-scale dataset of 99,094 samples constructed through counterfactual entity substitution, designed as both a *training resource* for attention-based faithfulness objectives and an *evaluation benchmark* for measuring context-grounding behavior in RAG systems. The dataset addresses a fundamental obstacle to fixing RAG unfaithfulness — the lack of training data that explicitly requires models to prefer context over internal knowledge — by starting from two established extractive QA benchmarks (SQuAD and TriviaQA), automatically identifying answer-bearing named entities in each context, replacing them with type-consistent alternatives drawn from a curated bank of 76,953 entities, and thereby manufacturing *controlled knowledge conflicts* between context and parametric memory. Rigorous quality filtering ensures 100% pass rates across four automated checks on random 200-sample audits. The dataset covers eight named entity categories and provides a complete construction pipeline.

## Key Facts
- **Authors**: Ju, Li; Wang, Junzhe; Zhang, Qi
- **Year**: 2026
- **arXiv**: [2604.25313](https://arxiv.org/abs/2604.25313)
- **Submission Date**: 2026-04-28 (cs.CL / cs.IR)

## Key Contributions
- **Surfaces counterfactual entity substitution as the load-bearing data-construction primitive** for RAG-faithfulness research: manufacturing controlled knowledge conflicts between retrieved context and parametric memory requires a *mechanism* to inject *type-consistent* but *factually-divergent* entities into contexts — which the dataset operationalizes at scale (99,094 samples, 76,953-entity bank).
- **Provides a typed-entity-bank-as-conflict-injection-primitive** — the 76,953-entity bank spans eight named-entity categories, and the substitution preserves type consistency (entity→type-consistent-alternative) while breaking factual continuity (entity→different-specific-instance), enabling controlled parametric-vs-context conflict.
- **Bidirectional role**: training resource *and* evaluation benchmark — most RAG faithfulness resources serve one role; Faithfulness-QA serves both via the same construction pipeline (the substitution procedure is the data; the resulting conflicts are the eval signal).
- **100% pass rate across four automated quality checks on random 200-sample audits** — provides a rigorous quality-filtering standard for synthetic-counterfactual RAG datasets, addressing the prior concern that synthetic data is noisy.
- **Released with full construction pipeline and code** — the dataset is reproducible: SQuAD + TriviaQA → entity identification → type-consistent substitution → quality filtering → 99,094 samples — a *manufactured-conflict-as-first-class-training-signal* primitive.

## Related Papers
- [[off-the-shelf-llms-as-process-scorers-training-free-prm-alternative-chunk-level-guided-generation-2606.01682]] — Run 67 inverse-axis sibling — Off-the-Shelf-LLMs-as-Process-Scorers exploits *off-the-shelf LLM as process reward scorer at inference time* (training-free primitive), Faithfulness-QA exploits *manufactured-conflict training data* (training-required primitive) — together they bracket the LLM-evaluation-fidelity surface between *training-free-inference-time-judging* and *training-data-driven-supervision* primitives, both addressing different facets of the same load-bearing concern: how to ensure LLM-generated signals are reliable when no ground-truth exists.
- [[interpretability-can-be-actionable-2605.11161]] — Run 58 sibling interpretability-evaluation paper — Interpretability-Can-Be-Actionable argues *interpretability must be evaluated by decision-enabling actionability*, Faithfulness-QA operationalizes *RAG faithfulness must be evaluated by counterfactual-conflict-discrimination* — together they bracket the *evaluation-criterion-actionability* surface between interpretability-decision-quality and RAG-context-grounding primitives.
- [[vericache-turning-lossy-kv-cache-into-lossless-llm-inference-2605.17613]] — Run 59 sibling — VeriCache addresses *lossless inference from lossy KV cache*, Faithfulness-QA addresses *faithful generation from conflicting-parametric-and-retrieval memory* — together they bracket the *fidelity-preservation-under-distortion* surface between cache-side and memory-side primitives.
- [[let-llms-judge-each-other-multi-agent-peer-reviewed-reasoning-for-medical-question-answering-2606.15419]] — Run 67 era sibling multi-agent-judging paper — both surface *peer-evaluation-as-fidelity-mechanism* primitives; multi-agent peer-review exploits *inter-LLM disagreement* as the evaluation signal, Faithfulness-QA exploits *intra-LLM context-vs-parametric-memory disagreement* as the training signal — together they bracket the *LLM-as-judge* surface between inter-model disagreement and intra-model disagreement primitives.
- [[emergent-concepts]] — parent wiki page