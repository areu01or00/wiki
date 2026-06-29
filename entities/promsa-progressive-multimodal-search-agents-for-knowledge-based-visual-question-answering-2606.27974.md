---
title: "ProMSA: Progressive Multimodal Search Agents for Knowledge-Based Visual Question Answering"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agent, multimodal, retrieval, progressive-search, knowledge-based-vqa]
sources: ["https://arxiv.org/abs/2606.27974"]
---

# ProMSA: Progressive Multimodal Search Agents for Knowledge-Based Visual Question Answering

## Overview
ProMSA is a progressive multimodal search agent for knowledge-based VQA that iteratively selects image search, text search, or stop under explicit tool-call budgets. It uses rejection-sampling SFT for format learning and TN-GSPO sequence-level RL for optimization, demonstrating consistent gains over RAG and agent baselines on E-VQA and InfoSeek.

## Key Facts
- **Authors**: 
- **Year**: 2026
- **arXiv**: [2606.27974](https://arxiv.org/abs/2606.27974)
- **Online Date**: 2026-06-26

## Key Contributions
- First progressive multimodal search agent for KB-VQA with iterative tool-call decision-making under explicit budgets
- TN-GSPO: sequence-level RL objective normalizing updates by generation length AND tool-interaction depth
- Rejection-sampling SFT for valid tool-use format learning before RL
- Consistent gains over strong RAG and agent baselines on E-VQA and InfoSeek benchmarks
- Deduplication mechanism to avoid redundant retrieval

## Related Papers
- [[calvert-augmenting-agents-with-calibrated-verifier-telemetry-improves-action-and-learning-in-knowledge-intensive-tasks-2606.21777]] — Calibrated verifier telemetry for knowledge-intensive agent tasks (sibling agent work)
- [[agents-last-exam-2606.05405]] — Agent evaluation benchmark (sibling agent evaluation work)
- [[emergent-concepts]] — Parent meta-page for emergent concept discoveries
