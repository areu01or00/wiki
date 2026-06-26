---
title: "OpenBioRQ: Unsolved Biomedical Research Questions for Agents"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [biomedical, agentic-research, citation-faithfulness, abstention, benchmark]
sources: ["https://arxiv.org/abs/2606.21959"]
---

# OpenBioRQ: Unsolved Biomedical Research Questions for Agents

## Overview
Jeong (2026) introduces OpenBioRQ, a retrieval-grounded agentic benchmark of 12,553 unsolved biomedical research questions across 12 domains, designed as a faithfulness-and-abstention probe — the first biomedical benchmark to combine an agentic setting (where the model must issue multiple tool calls) with unsolved questions that have no answer key. Openness is verified against real follow-up evidence rather than a model's parametric knowledge; difficulty is empirical (anchored on questions three open-weight reference models fail to answer, not on subjective hardness labels); on the hardest subset, held-out models from the same lineage as the difficulty anchors solve only ~17%, while three independent frontier agents (Gemini-3-Pro, Opus-4.7, GPT-5.5) span a wide 29-60% range — making the benchmark hard, non-saturating, and discriminating across capability tiers. Crucially, the paper diagnoses *agentic collapse* on the hardest questions where agents stop using their tools, and shows that for the most collapse-prone model blocking tool access entirely barely changes its score — tools stop paying off exactly where they are needed most.

## Key Facts
- **Authors**: Minbyul Jeong
- **Year**: 2026
- **arXiv**: [2606.21959](https://arxiv.org/abs/2606.21959)
- **Date**: 2026-06-20

## Key Contributions
- **Citation-correctness failure mode**: surfaces that current agentic models rarely *fabricate* citations (over 99% resolve) yet roughly 15.9% link to the *wrong* paper — a failure mode existing benchmarks miss because fixed-answer-key questions let a model reproduce the expected source from that key rather than independently verifying that the source supports the claim. The benchmark thus probes a fundamentally different dimension from answer-correctness evaluation.
- **Faithfulness-and-abstention probe design**: the unsolved-question design forces agents to either verify their claims against real follow-up evidence or *abstain* — surfacing *abstention-as-research-discipline* as the structurally correct primitive for agentic research settings where confident hallucination is the dominant failure mode.
- **Agentic-collapse diagnosis**: identifies that on the hardest questions, agents stop using their tools — and blocking tool access entirely barely changes the collapse-prone model's score. This surfaces *tool-non-use-on-hardest-questions* as a load-bearing primitive where the standard "more tools → better agents" framing inverts exactly at the capability frontier.
- **Frozen per-question checklist as judge-stabilizer**: a frozen per-question checklist raises inter-judge agreement from Spearman 0.35 to 0.82, providing a concrete recipe for stabilizing open-ended research-grade evaluation against judge variance.

## Related Papers
- [[emergent-concepts]] — Parent wiki page that motivated this discovery
- [[lingxidiagbench-a-multi-agent-framework-for-benchmarking-llms-in-chinese-psychiatric-consultation-and-diagnosis-2602.09379]] — Sibling medical-domain multi-agent benchmark — LingxiDiagBench benchmarks *clinical-reasoning-competence* in Chinese psychiatric consultation, OpenBioRQ benchmarks *citation-faithfulness-and-abstention* in unsolved biomedical research — together they bracket the medical-LLM evaluation surface between clinical-competence and research-faithfulness
- [[let-llms-judge-each-other-multi-agent-peer-reviewed-reasoning-for-medical-question-answering-2606.15419]] — Sibling medical-LLM multi-agent reasoning work — Let-LLMs-Judge-Each-Other uses peer-review-as-selection for MedQA, OpenBioRQ uses unsolved-question-and-abstention-probe for biomedical research — together they bracket the medical-LLM evaluation surface between answer-quality selection and research-faithfulness
- [[where-does-the-signal-live-a-web-data-recipe-for-medical-encoder-pretraining-2606.22079]] — Sibling medical-domain LLM work — Where-Does-the-Signal-Live provides data-recipe for medical encoder pretraining, OpenBioRQ provides evaluation-recipe for medical agentic research — together they bracket the medical-LLM development surface between pretraining-data curation and agentic-research evaluation
- [[deep-research-in-physical-sciences-a-multi-agent-framework-and-comprehensive-benchmark-2606.18648]] — Sibling multi-agent deep-research benchmark — Deep-Research evaluates *task-completion* in scientific reasoning workflows, OpenBioRQ evaluates *citation-faithfulness* in unsolved biomedical research — together they bracket the deep-research benchmark surface between task-completion and research-faithfulness primitives
- [[llm-based-scientific-peer-review-methods-benchmarks-reliability-challenges-2606.25057]] — Sibling peer-review reliability work — Scientific-Peer-Review benchmarks *peer-review automation reliability*, OpenBioRQ benchmarks *agentic-research faithfulness* (a different reliability surface — citation correctness and abstention discipline rather than review quality) — together they bracket the LLM-scientific-research reliability surface between review-reliability and research-faithfulness