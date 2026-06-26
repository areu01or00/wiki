---
title: "Let LLMs Judge Each Other: Multi-Agent Peer-Reviewed Reasoning for Medical Question Answering"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [multi-agent, peer-review, llm-as-judge, medical, reasoning]
sources: ["https://arxiv.org/abs/2606.15419"]
---

# Let LLMs Judge Each Other: Multi-Agent Peer-Reviewed Reasoning for Medical Question Answering

## Overview
Zhan, Zhou, Zhang (2026) propose a **multi-agent peer-reviewed reasoning method** for medical question answering in which multiple LLM agents independently generate chain-of-thought reasoning with candidate answers, then act as peer reviewers to evaluate each other's reasoning for factual correctness and logical soundness, with the highest-rated reasoning chain selected to produce the final answer — addressing the structural limitation of LLM-as-judge methods that focus on answer agreement rather than reasoning quality. Across five SOTA LLMs (Llama-3.1-8B, Qwen2.5-7B, Phi-4, DeepSeek-LLM-7B, GPT-oss-20B) and three medical benchmarks (HeadQA, MedQA-USMLE, PubMedQA), peer-reviewed reasoning consistently outperforms both single-model CoT and CoT-based majority voting — the best combination achieves 0.820 average accuracy, exceeding the strongest single model (0.777) and majority voting ensembles (up to 0.789), with peer assessments reliably distinguishing high- from low-quality reasoning chains.

## Key Facts
- **Authors**: Zhan, Zaifu; Zhou, Shuang; Zhang, Rui
- **Year**: 2026
- **arXiv**: [2606.15419](https://arxiv.org/abs/2606.15419)
- **Date**: 2026-06-13

## Key Contributions
- **Peer-review-as-CoT-selection primitive**: reframes multi-agent LLM reasoning from "ensemble of votes" to "ensemble of evaluated reasoning chains" — peer reviewers rank reasoning chains by factual correctness and logical soundness, not by answer agreement, surfacing *reasoning-quality-as-selection-criterion* as the structurally correct primitive for multi-agent reasoning.
- **Scaling with peer count**: the method scales effectively with more participating models (peer assessments reliably distinguish high- from low-quality chains even as the ensemble grows), inverting the common finding that naive majority voting plateaus with ensemble size — peer-reviewing adds discriminative signal that voting loses.
- **Empirical dominance over voting**: across MedQA benchmarks, peer-reviewed reasoning (0.820) exceeds single-model CoT (0.777) and majority voting ensembles (0.789) — providing the first systematic demonstration that *reasoning evaluation* outperforms *answer agreement* as the multi-agent coordination primitive in high-stakes domain QA.

## Related Papers
- [[emergent-concepts]] — Parent wiki page that motivated this discovery
- [[llm-based-scientific-peer-review-methods-benchmarks-reliability-challenges-2606.25057]] — Sibling peer-review methodology paper — Scientific-Peer-Review surveys *human-mediated* peer-review of LLM outputs, Let-LLMs-Judge-Each-Other provides *machine-mediated* peer-review of LLM reasoning chains — together they bracket the peer-review surface between human-mediated and machine-mediated primitives
- [[benchmarking-open-ended-multi-agent-coordination-in-language-agents-2606.08340]] — Sibling multi-agent evaluation — alem isolates *coordination-as-distinct-bottleneck* in long-horizon open-ended tasks, Let-LLMs-Judge-Each-Other isolates *peer-review-as-reasoning-selection* in single-turn MedQA — together they bracket the multi-agent evaluation surface between long-horizon coordination and single-turn peer-review reasoning
- [[lingxidiagbench-a-multi-agent-framework-for-benchmarking-llms-in-chinese-psychiatric-consultation-and-diagnosis-2602.09379]] — Sibling medical-domain multi-agent benchmark — LingxiDiagBench benchmarks *clinical-reasoning-competence* in Chinese psychiatric consultation, Let-LLMs-Judge-Each-Other benchmarks *peer-review-reasoning-selection* in MedQA — together they bracket the medical-LLM evaluation surface between clinical-competence and peer-review-selection