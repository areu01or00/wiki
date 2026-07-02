---
title: "Test-Time Verification for Text-to-SQL via Outcome Reward Models"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [inference-efficiency, test-time-computation, verification, structured-reasoning, text-to-sql]
sources: ["https://arxiv.org/abs/2606.30851"]
---

# Test-Time Verification for Text-to-SQL via Outcome Reward Models

## Overview
GradeSQL introduces Outcome Reward Models (ORMs) as learned semantic scoring functions for test-time verification in Text-to-SQL generation. ORM-based selection consistently outperforms execution-based Best-of-N and Majority Voting, with gains of up to +4.33% on BIRD and +2.10% on Spider benchmarks. This is the first application of ORM-based test-time verification to structured query generation, replacing heuristic execution-success signals with semantic discrimination.

## Key Facts
- **Authors**: Tritto, Mattia; Farano, Giuseppe; Di Palma, Dario + 4
- **Year**: 2026
- **arXiv**: [2606.30851](https://arxiv.org/abs/2606.30851)
- **Date**: 2026-06-29

## Key Contributions
- First ORM-based test-time verification for Text-to-SQL (replacing heuristic signals like execution success)
- GradeSQL framework: automated candidate generation + execution-based labeling for task-specific ORM training without manual annotation
- ORM-based Best-of-N outperforms execution-based and majority voting across multiple LLM families
- Demonstrates effective scaling with larger candidate sets, stronger on complex queries
- Simple, effective, and scalable alternative to heuristic test-time selection strategies

## Related Papers
- [[a-specialized-reasoning-large-language-model-for-accelerating-rare-disease-diagn-2606.24510]] — RaDaR's test-time verification in clinical reasoning; complements GradeSQL's ORM verification pattern applied to high-stakes medical diagnosis workflows
- [[harnessing-generalist-agents-for-contextualized-time-series-2606.05404]] — TimeClaw's agentic harness with temporal tool integration; shares the tool-augmented agent reasoning pattern with GradeSQL's verification-driven pipeline
