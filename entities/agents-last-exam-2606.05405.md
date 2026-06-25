---
title: "Agents' Last Exam"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [agents, benchmark, evaluation, llm, professional-domains]
sources: ["https://arxiv.org/abs/2606.05405"]
---

# Agents' Last Exam

## Overview
This paper introduces Agents' Last Exam (ALE), a benchmark designed to measure whether AI agents can actually perform the work human experts perform across professional domains — finance, law, manufacturing, and 52 other subdomains — rather than answer trivia *about* those domains. The authors argue that the gap between benchmark performance and economically meaningful deployment has widened despite strong results on existing tests, and that closing this gap requires benchmarks whose tasks are real professional outputs evaluated by domain practitioners. ALE reports the current ceiling of frontier agents and provides the rubric structure for ongoing community submissions.

## Key Facts
- **Authors**: Sun, Yiyou; Han, Xinyang; Zhang, Weichen
- **Year**: 2026
- **arXiv**: [2606.05405](https://arxiv.org/abs/2606.05405)
- **Subjects**: cs.AI

## Key Contributions
- Constructs Agents' Last Exam (ALE), a benchmark of 1,000+ expert-authored tasks spanning 52 professional subdomains, where each task is a real professional deliverable (memo, model, audit, draft) rather than a question about a domain.
- Documents that frontier LLM agents score substantially lower on ALE than on traditional knowledge benchmarks, providing a quantitative measurement of the deployment gap the authors set out to characterize.
- Releases an open evaluation harness with rubric-based grading by domain practitioners, enabling reproducible scoring that resists the benchmark-saturation dynamics that have eroded prior generations of professional-domain tests.
- Provides a taxonomy of failure modes observed in agent runs on ALE (knowledge gaps, tool-selection errors, planning failures, output-format errors), giving downstream work a structured map of where agent capability is still bottlenecked.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on 2026-06-25 as a fresh 2026 contribution to LLM agent benchmarking and evaluation.
