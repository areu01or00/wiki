---
title: "Benchmark Everything Everywhere All at Once"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [benchmark, llm-evaluation, agentic-framework, automated-evaluation]
sources: ["https://arxiv.org/abs/2606.06462"]
---

# Benchmark Everything Everywhere All at Once

## Overview
Introduces Benchmark Agent, a fully autonomous agentic system that orchestrates the complete LLM/MLLM benchmark-construction pipeline (user-query analysis, subtask design, data annotation, quality control). Demonstrates 15 representative benchmarks spanning text understanding, multimodal understanding, and domain-specific reasoning, with continual-evaluation findings that current models struggle with certain domain-specific reasoning tasks.

## Key Facts
- **Authors**: Xiong, Shiyun; Wu, Dongming; Sun, Peiwen; Ai, Yuang; Yang, Bokang; and others
- **Year**: 2026
- **arXiv**: [2606.06462](https://arxiv.org/abs/2606.06462)
- **Online date**: 2026-06-04
- **Submission date**: 2026-06-04

## Key Contributions
- **Benchmark Agent framework** — fully autonomous end-to-end pipeline that takes a natural-language user query and produces a complete benchmark with subtasks, data, and quality-control annotations
- **Demonstration on 15 representative benchmarks** spanning text understanding, multimodal understanding, and domain-specific reasoning tasks
- **Continual-evaluation finding** — current LLMs/MLLMs struggle with certain domain-specific reasoning tasks once continual evaluation is applied (current models saturate fast on fixed benchmarks, but show clear discrimination when benchmark regeneration is automated)
- **Sustainability-and-discrimination co-design** — addresses the dual failure mode where benchmarks are labor-intensive (low sustainability) AND quickly saturate (low discrimination) by making benchmark construction itself an agentic task that can be re-run as models evolve

## Related Papers
- [[emergent-concepts]] — Parent wiki page where this discovery is logged
- [[benchmarking-open-ended-multi-agent-coordination-in-language-agents-2606.08340]] — Sibling multi-agent coordination benchmark (alem Craftax-based open-ended coordination evaluation) — together they bracket the LLM-evaluation surface between *open-ended coordination* (alem) and *automated-benchmark regeneration* (Benchmark-Agent)
- [[the-verification-horizon-no-silver-bullet-for-coding-agent-rewards-2606.26300]] — Sibling verification-co-evolution primitive (no fixed reward stays faithful) — together they bracket the evaluation-fidelity surface between *verifier signal stability* (Verification-Horizon) and *benchmark regeneration as anti-saturation mechanism* (Benchmark-Agent)
- [[openbiorq-unsolved-biomedical-research-questions-for-agents-2606.21959]] — Sibling unsolved-question benchmark primitive (12,553 unsolved biomedical questions, no-answer-key evaluation) — together they bracket the no-answer-key-evaluation surface between *unsolved biomedical research* (OpenBioRQ) and *agentic benchmark regeneration* (Benchmark-Agent)
- [[let-llms-judge-each-other-multi-agent-peer-reviewed-reasoning-for-medical-question-answering-2606.15419]] — Sibling peer-review-as-selection primitive (multi-agent reasoning quality selection) — together they bracket the automated-evaluation surface between *peer-review reasoning selection* (Let-LLMs-Judge-Each-Other) and *automated benchmark construction* (Benchmark-Agent)
- [[the-illusion-of-multi-agent-advantage-2606.13003]] — Sibling Run-66 MAS-advantage falsification primitive — together they bracket the automated-evaluation surface between *MAS-vs-SAS advantage empirical falsification* (Illusion-of-Multi-Agent-Advantage) and *automated benchmark construction* (Benchmark-Agent)