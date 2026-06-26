---
title: "Where LLM Agents Fail and How They Can Learn From Failures"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [llm, agents, reliability, error-taxonomy, debugging, agent-debug, agent-error-bench]
sources: ["https://arxiv.org/abs/2509.25370"]
---

# Where LLM Agents Fail and How They Can Learn From Failures

## Overview
Introduces AgentErrorTaxonomy — a modular classification of failure modes spanning memory, reflection, planning, action, and system-level operations — together with AgentErrorBench (the first systematically annotated failure-trajectory dataset from ALFWorld, GAIA, and WebShop) and AgentDebug (a debugging framework that isolates root-cause failures and provides corrective feedback). AgentDebug achieves 24% higher all-correct accuracy and 17% higher step accuracy on AgentErrorBench.

## Key Facts
- **Authors**: Zhu, Kunlun; Liu, Zijia; Li, Bingxuan; Tian, Muxin; Yang, Yingxuan
- **Year**: 2025
- **arXiv**: [2509.25370](https://arxiv.org/abs/2509.25370)

## Key Contributions
- AgentErrorTaxonomy: modular classification spanning memory, reflection, planning, action, and system-level operations — a peer to the mechanism-level silent-failure taxonomies that surfaced in 2026
- AgentErrorBench: first systematically annotated failure-trajectory dataset grounding error analysis in real-world agent rollouts (ALFWorld, GAIA, WebShop)
- AgentDebug: debugging framework that isolates root-cause failures and provides corrective feedback, enabling iterative recovery
- 24% all-correct accuracy gain and 17% step-accuracy gain over baselines
- **First paper in the wiki** to combine a modular agent-error taxonomy with an annotated failure-trajectory dataset and an empirically validated recovery framework

## Related Papers
- [[silent-failure-in-llm-agent-systems-the-entropy-principle-2606.08162]] — Sibling discovery from same run: mechanism-level entropy lens that formalizes silent failures as monotonically growing entropy across 6 lifecycle layers
- [[when-errors-become-narratives-a-longitudinal-taxonomy-of-silent-failures-in-a-production-llm-agent-runtime-2606.14589]] — Sibling discovery from same run: 5-class production taxonomy including the LLM-unique "fail-plausible" Class D
- [[a-technical-taxonomy-of-llm-agent-communication-protocols-2606.19135]] — sibling taxonomy paper for agent communication protocols; complements this paper's failure-mode taxonomy
- [[why-multi-step-tool-use-reinforcement-learning-collapses-and-how-supervisory-signals-fix-it-2606.26027]] — training-side failure-mode recovery paper for multi-step tool-use RL