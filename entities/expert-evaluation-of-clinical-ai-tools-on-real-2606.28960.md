---
title: "Expert Evaluation of Clinical AI Tools on Real Point-of-Care Clinical Queries"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [llm-evaluation, clinical-ai, benchmark, expert-evaluation]
sources: ["https://arxiv.org/abs/2606.28960"]
---

# Expert Evaluation of Clinical AI Tools on Real Point-of-Care Clinical Queries

## Overview
Physicians now pose millions of clinical questions to AI tools each week, yet existing evaluations rely on hypothetical or exam-style questions rather than real practice queries. This paper reports a blinded evaluation on 620 Real-world Point-Of-Care Queries (Real-POCQi) submitted to the OpenEvidence platform by physicians across 30 specialties. Using 149 practicing physicians as graders across 36 states, the study finds that a specialized clinical tool consistently outperforms frontier general-purpose models (Claude Opus 4.8, Gemini 3.1 Pro, GPT-5.5) by 25-39 percentage points on accuracy, clinical utility, source quality, verifiability, and completeness. First systematic real-world clinical query benchmark for AI tools.

## Key Facts
- **arXiv**: [2606.28960](https://arxiv.org/abs/2606.28960)
- **Date**: 2026-06-01

## Key Contributions
- Real-POCQi benchmark: 620 real-world clinical queries from practicing physicians across 30 specialties
- First blinded head-to-head comparison of frontier general-purpose LLMs vs specialized clinical AI tool using expert physician graders
- Frontier general-purpose models consistently outperformed by specialized tool by 25-39 percentage points
- LLM judges found to systematically differ from expert judges — both generally agree on best model but LLM judges flatter weaker models
- Findings: AI tool evaluations should reflect real-world query distributions and use expert judges matched to specialty

## Related Papers
- [[agents-last-exam-2606.05405]] — Agents' Last Exam: Related via LLM benchmarking — both evaluate LLMs on domain-specific professional tasks
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — EnterpriseClawBench: Related via real-world session benchmarking — both use real-world agent evaluation frameworks
- [[nrt-bench-benchmarking-multi-turn-red-teaming-of-llm-operator-agents-in-safety-critical-control-rooms-2606.20408]] — NRT-Bench: Related via benchmark methodology — both address LLM evaluation in safety-critical domains
