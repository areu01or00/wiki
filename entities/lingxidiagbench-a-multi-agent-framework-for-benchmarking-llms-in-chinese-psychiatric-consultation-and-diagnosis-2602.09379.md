---
title: "LingxiDiagBench: A Multi-Agent Framework for Benchmarking LLMs in Chinese Psychiatric Consultation and Diagnosis"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [benchmark, multi-agent, llm, medical, psychiatric-diagnosis, chinese-nlp, evaluation]
sources: ["https://arxiv.org/abs/2602.09379"]
---

# LingxiDiagBench: A Multi-Agent Framework for Benchmarking LLMs in Chinese Psychiatric Consultation and Diagnosis

## Overview
LingxiDiagBench is a multi-agent benchmarking framework for evaluating LLMs on Chinese psychiatric consultation and diagnosis, addressing the shortage of psychiatrists and the subjectivity of interview-based diagnosis by simulating realistic patient-clinician interaction loops and scoring LLM outputs against clinician-verified diagnostic labels. It is built around a coordinated multi-agent setup (patient simulator, interviewer, diagnost) with clinician-verified ground truth, providing one of the first Chinese-language, end-to-end benchmarks for mental-health assessment.

## Key Facts
- **Authors**: Xu, Shihao, Zhou, Tiancheng, Ma, Jiatong et al.
- **Year**: 2026
- **Date**: 2026-02-10
- **arXiv**: [2602.09379](https://arxiv.org/abs/2602.09379)
- **Subjects**: Artificial Intelligence (cs.AI)

## Key Contributions
- A Chinese-language psychiatric consultation benchmark with multi-turn patient simulation and clinician-verified diagnostic labels, addressing the absence of realistic Chinese-language mental-health evaluation corpora
- A multi-agent framework that decomposes the diagnostic consultation pipeline into patient simulation, interview orchestration, and diagnostic reasoning agents, enabling modular evaluation of each stage
- Empirical benchmarking of contemporary LLMs on the framework, surfacing which model families best handle the long-context, empathy-sensitive, multi-turn dynamics characteristic of clinical psychiatric interviews
- Provides infrastructure for future research on culturally adapted, language-specific clinical LLM evaluation, distinct from English-centric medical LLM benchmarks

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — Companion agent-benchmark theme for real-world workplace agent evaluation
- [[agora-an-archive-grounded-benchmark-for-agentic-workplace-document-reasoning-2606.24526]] — Companion agent-benchmark theme for workplace document reasoning
