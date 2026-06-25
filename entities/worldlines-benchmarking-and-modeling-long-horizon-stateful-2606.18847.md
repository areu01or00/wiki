---
title: "WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [embodied-agent, long-horizon, memory, household-assistance, benchmark]
sources: ["https://arxiv.org/abs/2606.18847"]
---

# WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents

## Overview
Zhang, Su, Huang, Chang, Zhou, Xu, Xu, and Li introduce WorldLines, a project-driven benchmark for long-horizon embodied household assistance that constructs temporally extended household traces (dialogues, actions, execution feedback, object/device state changes) and converts them into evidence-linked samples for Memory QA and Embodied Task Planning — and propose ObsMem, an observer-grounded memory framework that maintains visibility-aware memories and action-native state trails for state-aware decisions.

## Key Facts
- **Authors**: Zhang, Yehang; Su, Jianchong; Huang, Haojian; Chang, Yifan; Zhou, Tianhao; Xu, Xinli; Xu, Yingjie; Li, Yinchuan
- **Year**: 2026
- **arXiv**: [2606.18847](https://arxiv.org/abs/2606.18847)
- **Date**: 2026-06-17

## Key Contributions
- Surfaces a structural gap in long-horizon embodied evaluation: existing long-term-memory benchmarks focus on language-centric retrieval/QA, while embodied benchmarks focus on short-horizon task execution — leaving the joint "long-horizon + embodied + memory-dependent" regime under-evaluated despite being the deployment regime for home-assistance agents.
- Releases WorldLines, a project-driven benchmark that constructs temporally extended household traces with dialogues, actions, execution feedback, and object/device state changes, then converts them into evidence-linked samples for both Memory QA (retrieval-and-recall evaluation) and Embodied Task Planning (action-conditioned plan generation evaluation).
- Proposes ObsMem, an observer-grounded memory framework that maintains two complementary memory streams — (1) visibility-aware memories (what the agent currently perceives) and (2) action-native state trails (what the agent has actually changed) — yielding state-aware decisions that respect partial observability and dynamic world-state overwrites.
- Diagnoses three persistent challenges in the regime via benchmark experiments: (1) partial observability causing memory-recall failures, (2) overwritten world states breaking plans, and (3) the difficulty of translating long-term memory into grounded embodied plans — and surfaces ObsMem as a stronger reference architecture that addresses all three.

## Related Papers
- [[emergent-concepts]] — Parent meta-page that aggregates this and other emergent-concept discoveries from the wiki-explore-agent pipeline.
- [[world-value-models-robotic-manipulation-2606.24742]] — Sibling robotics world-model value-estimation work; together they frame world-model-grounded architectures as the right foundation for embodied deployment — WVM grounds value estimation in temporal context, ObsMem grounds memory in observer visibility + action trails.
- [[ebench-elemental-diagnosis-of-generalist-mobile-manipulation-policies-2606.18239]] — Sibling multi-axis-diagnostic robotics benchmark; both argue that aggregate-success-rate evaluation masks capability-specific failures — EBench on atomic skill axes, WorldLines on long-horizon memory axes.
- [[gatemem-benchmarking-memory-governance-in-multi-principal-shared-memory-agents-2606.18829]] — Sibling agent-memory benchmark; GateMem isolates the access-control axis of shared-memory agents, WorldLines isolates the long-horizon-observability axis of embodied agents — complementary memory evaluation surfaces.
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Sibling agent-memory readiness survey; WorldLines provides an empirical benchmark grounding the survey's forward-looking questions about long-horizon memory in dynamic environments.