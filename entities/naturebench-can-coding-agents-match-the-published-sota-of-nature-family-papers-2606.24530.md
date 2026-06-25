---
title: "NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [benchmark, coding-agent, scientific-discovery, reproducibility, agent-evaluation]
sources: ["https://arxiv.org/abs/2606.24530"]
---

# NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?

## Overview
NatureBench is a cross-discipline benchmark of 90 tasks distilled from peer-reviewed Nature-family publications, paired with an automated NatureGym pipeline that builds a standardized containerized environment per task. Across ten frontier agent configurations evaluated under a strict web-search-disabled protocol, the strongest model surpasses published SOTA on only 17.8% of tasks under the g>0.1 criterion, with most successes coming from methodological translation into familiar supervised prediction rather than genuine scientific invention.

## Key Facts
- **Authors**: Wang, Yuru; Cheng, Lejun; Zuo, Yuxin; Zeng, Sihang; He, Bingxiang
- **Year**: 2026
- **arXiv**: [2606.24530](https://arxiv.org/abs/2606.24530)
- **Subjects**: cs.CL

## Key Contributions
- Constructs 90 reproducible research tasks from Nature-family papers via the NatureGym pipeline, which automatically generates per-task containerized environments and removes the environment-fragmentation problem that has undermined credibility of prior agent-on-research benchmarks.
- Holds out web search at evaluation time and shows the strongest frontier agent matches SOTA on only 17.8% of tasks under the g>0.1 criterion, with method choice and compute budget — not task misunderstanding — dominating the failure modes.
- Performs pathway analysis of successful runs to show agents mostly translate scientific problems into familiar supervised-prediction problems rather than inventing new methods, giving an empirical handle on the "reproduction vs discovery" distinction.
- Releases the benchmark, NatureGym pipeline, and a public leaderboard with maintainer-side reproduction; code at https://github.com/FrontisAI/NatureBench.

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this discovery is recorded; pairs with the agentic-benchmarking theme (EnterpriseClawBench, AGORA, Counsel).
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — EnterpriseClawBench evaluates agents on enterprise workflows; NatureBench pushes into scientific-replication territory with stricter web-search-disabled evaluation.
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Both works probe the upper bound of agent capability on long-horizon, multi-step tasks, with NatureBench isolating the scientific-discovery slice specifically.
- [[counsel-a-meta-evaluation-dataset-for-agentic-tasks-2606.21627]] — Both benchmarks (Counsel for RAG, NatureBench for scientific coding) frame evaluation as agent-mediated end-to-end task completion rather than component-level accuracy, contrasting with the component-level benchmarking that dominated earlier retrieval and code-generation work.