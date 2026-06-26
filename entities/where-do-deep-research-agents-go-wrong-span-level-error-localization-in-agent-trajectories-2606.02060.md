---
title: "Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [agent, llm, interpretability, evaluation, trajectory-analysis]
sources: ["https://arxiv.org/abs/2606.02060"]
---

# Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories

## Overview
Argues that final-answer evaluation shows whether an agent succeeds but NOT which parts of the trajectory make the answer unreliable. Introduces **span-level error localization** for deep-research agents: collects 2,790 real trajectories from 2 agent frameworks × 3 backbone models × 3 benchmarks, converts raw logs into semantic spans, and annotates harmful error spans through LLM-assisted expert review. Builds TELBench (1,000 instances) for the localization task.

## Key Facts
- **Authors**: Wang, Jiaming; Feng, Ziteng; Wu, Jiangtao; Li, Ruihao; Xie, Qianqian
- **Year**: 2026
- **arXiv**: [2606.02060](https://arxiv.org/abs/2606.02060)
- **Citation date**: 2026-06-01 (online: 2026-06-02)

## Key Contributions
- Reframes deep-research-agent evaluation from binary success/failure to span-level error localization
- Constructs 2,790-trajectory corpus spanning 2 frameworks × 3 backbones × 3 benchmarks with LLM-assisted expert span annotations
- Releases TELBench (1,000 instances) as the first benchmark targeting span-level localization rather than final-answer correctness
- Establishes **trajectory-as-semantic-span-decomposition** as a diagnostic primitive for agent reliability
- Bridges agent-failure analysis (the dominant surface in Runs 55-67) with mechanistic-style interpretability — localizing failure to specific trajectory spans rather than just measuring aggregate accuracy

## Related Papers
- [[the-illusion-of-multi-agent-advantage-2606.13003]] — automatic MAS fails despite 10× cost; sibling primitive showing system-level falsification of deployment assumptions
- [[where-llm-agents-fail-and-how-they-can-learn-from-failures-2509.25370]] — AgentErrorTaxonomy + AgentErrorBench + AgentDebug; sibling primitive establishing agent-failure taxonomy (Run 57)
- [[measuring-epistemic-resilience-of-llms-under-misleading-medical-context-2606.12291]] — epistemic robustness under adversarial context; sibling from Run 72 with orthogonal adversarial surface
