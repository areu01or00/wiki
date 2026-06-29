---
title: "CollabSim: A CSCW-Grounded Methodology for Investigating Collaborative Competence of LLM Agents through Controlled Multi-Agent Experiments"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [multi-agent, evaluation, cscw, collaborative-competence, llm]
sources: ["https://arxiv.org/abs/2606.06399"]
---

# CollabSim: A CSCW-Grounded Methodology for Investigating Collaborative Competence of LLM Agents through Controlled Multi-Agent Experiments

## Overview
(2026) introduces **CollabSim** — a configurable simulation framework that combines a theory-grounded definition of collaborative capabilities (lifted from decades of Computer-Supported Cooperative Work research), controlled manipulation of interaction conditions, and action-level probing of agents' internal states — addressing the structural gap in MAS evaluation where studies find collaboration failure happens not because agents lack individual task-solving ability, but because they lack *collaborative competence* (the capacity to establish common ground, maintain shared task understanding, balance individual/collective incentives, and repair misalignment).

## Key Facts
- **Authors**: (see arXiv listing)
- **Year**: 2026
- **arXiv**: [2606.06399](https://arxiv.org/abs/2606.06399)
- **Date**: 2026-06-06

## Key Contributions
- **Theory-grounded definition of collaborative competence**: lifts and operationalizes four CSCW primitives — *common ground establishment*, *shared task understanding maintenance*, *individual–collective incentive balancing*, *misalignment repair as interaction unfolds* — surfacing *CSCW-imported-collaborative-competence-primitive* as the load-bearing primitive for diagnosing MAS failures beyond individual task competence, distinct from capability-evaluation primitives (where the load-bearing axis is *interaction-level-conditions-controlled-systematically* rather than *single-agent-task-completion*), and from coordination-benchmark primitives (where the load-bearing axis is *capability-as-separate-from-task-outcome* rather than *coordination-as-task-completion*).
- **Configurable interaction-condition manipulation**: experiments across 4 LLMs show that CollabSim captures condition effects, separates model performance patterns, and reveals task-dependent effects of agent design — surfacing *interaction-condition-as-controlled-variable-primitive* and *model-design-effect-isolation-primitive* as the load-bearing measurement primitives enabling reproducible collaboration research.
- **Action-level probing of agents' internal states**: surfaces *internal-state-probing-during-collaborative-interaction-primitive* as the load-bearing methodological primitive for understanding why collaboration succeeds or fails at each dialogue turn — distinct from outcome-only benchmarks because the load-bearing axis is *per-action-probing-of-internal-state-under-controlled-conditions* rather than *final-task-outcome-only*.

## Related Papers
- [[emergent-concepts]] — Parent wiki page that motivated this discovery
- [[benchmarking-open-ended-multi-agent-coordination-in-language-agents-2606.08340]] — Sibling multi-agent coordination benchmark — alem evaluates *coordination competence in open-ended survival tasks*, CollabSim evaluates *collaborative competence under controlled interaction conditions* — together they bracket the multi-agent evaluation surface between open-ended ecological validity and controlled condition manipulation
