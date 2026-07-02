---
title: "RepoRescue: An Empirical Study of LLM Agents on Whole-Repository Compatibility Rescue"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [LLM-agents, code-intelligence, benchmark, repository-maintenance]
sources: ["https://arxiv.org/abs/2607.01213"]
---

# RepoRescue: An Empirical Study of LLM Agents on Whole-Repository Compatibility Rescue

## Overview
Open-source libraries and tools are widely reused, but compatibility maintenance is expensive. Once maintainers leave, useful repositories can stop working as runtimes and dependencies evolve. This paper studies whether LLM agents can adapt old repositories to modern environments — a task called *compatibility rescue* — which differs fundamentally from bug repair: the repository worked before, it just no longer runs in updated environments.

## Key Facts
- **Authors**: Lin, Zhihao; Zhou, Mingyi; Sun, Zhensu + 4 others
- **Year**: 2026
- **arXiv**: [2607.01213](https://arxiv.org/abs/2607.01213)

## Key Contributions
- Defines *compatibility rescue* as a distinct LLM-agent task from bug fixing — requires reasoning about evolving runtime/dependency constraints rather than correcting logical errors
- Introduces a benchmark evaluating LLM agents on adapting whole repositories (not individual files) to updated Python environments and dependency constraints
- Shows that frontier LLMs struggle with cross-file dependency reasoning needed for compatibility updates

## Related Papers
- [[a-framework-for-evaluating-agentic-skills-at-scale-2606.17819]] — Evaluating LLM agent skills at scale on realistic benchmarks
- [[agents-last-exam-2606.05405]] — LLM agent benchmarking on realistic software tasks
