---
title: "SWE Atlas: Benchmarking Coding Agents Beyond Issue Resolution"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [code, software-engineering, agent, benchmark, llm, application-domain, refactoring]
sources: ["https://arxiv.org/abs/2605.08366"]
---

# SWE Atlas: Benchmarking Coding Agents Beyond Issue Resolution

## Overview
First benchmark suite in the wiki to systematically evaluate LLM coding agents across **three underrepresented but professionally important software-engineering workflows — Codebase Q&A, Test Writing, and Refactoring** — beyond the issue-resolution bottleneck that dominates prior SWE-bench-style evaluations, using comprehensive category-specific protocols and under-specified agentic task formulations that better reflect real-world usage.

## Key Facts
- **Authors**: (SWE Atlas team)
- **Year**: 2026
- **arXiv**: [2605.08366](https://arxiv.org/abs/2605.08366)
- **Online Date**: 2026-05-08
- **Domain**: software-engineering × LLM-coding-agent × professional-SE-workflow

## Key Contributions
- **Three-workflow coding-agent benchmark**: 124 Codebase-Q&A tasks + 90 Test-Writing tasks + 70 Refactoring tasks — total 284 SE tasks spanning underrepresented workflows that prior issue-resolution benchmarks miss
- **Under-specified agentic task formulations**: tasks are designed to require the agent to interpret ambiguous requirements and make professional SE judgments rather than execute unambiguous issue-resolution scripts, mirroring real-world SE work
- **Category-specific evaluation protocols**: programmatic checks + rubric-based assessment combined per task category — surfacing workflow-specific quality primitives rather than a single score
- **Beyond-issue-resolution framing**: positions coding-agent evaluation at the full SE surface rather than the well-trodden issue-resolution bottleneck, exposing limitations of current agents on real professional workloads
- **First under-specified-agentic SE benchmark suite in the wiki** covering Codebase-Q&A + Test-Writing + Refactoring as distinct professional SE workflows, verified via `ls entities/ | grep -iE "(swe.atlas|coding.agent.*workflow|test.writing.*llm|refactoring.*agent)"` returning empty

## Related Papers
- [[an-exploratory-case-study-of-llm-assisted-refactoring-and-gameplay-feature-generation-in-an-endless-runner-game-2606.21171]] — Sibling exploratory case study on LLM-assisted refactoring; SWE Atlas extends to a formal multi-workflow benchmark
- [[large-language-models-for-software-engineering-a-reproducibility-crisis-2512.00651]] — Sibling meta-research primitive on LLM-for-SE reproducibility; SWE Atlas is the application-domain complement targeting coding-agent evaluation
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — Sibling benchmark from real workplace sessions; SWE Atlas focuses on SE-specific workflows, EnterpriseClawBench on enterprise task families
- [[beyond-nl2code-a-structured-survey-of-multimodal-code-intelligence-2606.15932]] — Survey sibling on multimodal code intelligence; SWE Atlas adds the agentic-task-formulation layer missing from surveys
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — Application-domain sibling on enterprise workplace benchmarks; SWE Atlas targets professional SE workflows while EnterpriseClawBench targets enterprise office tasks
