---
title: "Counsel: A Meta-Evaluation Dataset for Agentic Tasks"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [evaluation, agentic, llm-as-judge, meta-evaluation, agents, llm-research]
sources: ["https://arxiv.org/abs/2606.21627"]
---

# Counsel: A Meta-Evaluation Dataset for Agentic Tasks

## Overview
Counsel is the first public dataset of meta-evaluations for agentic tasks — process-level critiques from open-weight LLM-as-judge (LLMJ) models on tau-bench and DA-Code trajectories, paired with human meta-evaluations that label each flagged error as spot-on, correct-location-but-poor-reasoning, or should-not-have-flagged. The dataset stratifies LLMJ critique quality across both error location and reasoning quality, with reliable inter-annotator agreement (Krippendorff's α = 0.78), enabling calibration, improvement, and training of LLMJs for agentic evaluation.

## Key Facts
- **Authors**: Pisupati, Sashank; Broomfield, Henry; Choi, Eujeong; Calvi, Antonia; Wang, Charlie; Engeler, Roman; Bartolo, Max; Lewis, Patrick
- **Year**: 2026
- **Date**: 2026-06-19
- **arXiv**: [2606.21627](https://arxiv.org/abs/2606.21627)
- **Subjects**: Artificial Intelligence (cs.AI)

## Key Contributions
- Introduces the first public dataset of meta-evaluations for agentic tasks, covering both customer-support agents (tau-bench) and coding agents (DA-Code)
- Provides a three-way human-labeled stratification of LLMJ critiques (spot-on / correct-location-but-poor-reasoning / should-not-have-flagged) with Krippendorff's α = 0.78 inter-annotator agreement
- Shows that more capable open-weight judge models and more reasoning effort both improve human alignment — the strongest judge reaches ~88% agreement on location and ~65% on reasoning
- Demonstrates that even the strongest LLMJs leave substantial reasoning-quality gaps, motivating dedicated meta-evaluation data and training pipelines for agent evaluators
- Permissively licensed and generated with open-weight models, enabling broad community use for calibrating and training LLM-based evaluators of agentic systems

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[agora-an-archive-grounded-benchmark-for-agentic-workplace-document-reasoning-2606.24526]] — Workplace document agentic benchmark
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — Real-workplace agent benchmark
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — Long-horizon tool-use agent evaluation
- [[agents-last-exam-2606.05405]] — Cross-domain agentic exam benchmark