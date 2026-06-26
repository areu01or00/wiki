---
title: "MobileForge: Annotation-Free Adaptation for Mobile GUI Agents with Hierarchical Feedback-Guided Policy Optimization"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [mobile-gui-agent, annotation-free-adaptation, hierarchical-policy, feedback-guided-optimization, app-specialization, mllm]
sources: ["https://arxiv.org/abs/2606.19930"]
---

# MobileForge: Annotation-Free Adaptation for Mobile GUI Agents with Hierarchical Feedback-Guided Policy Optimization

## Overview
MobileForge addresses the per-app adaptation cost structure that prevents MLLM-based mobile GUI agents from scaling to the long tail of real-world mobile applications. Where standard adaptation requires per-app trajectory annotations (expensive and rarely available) and existing self-improvement pipelines operate on flat single-level trajectories (losing the structural relationship between UI actions, app state transitions, and task-level outcomes), MobileForge proposes an *annotation-free* adaptation pipeline that uses *hierarchical feedback-guided policy optimization* — the policy is structured as a hierarchy of UI-level, app-level, and task-level decisions, and feedback flows up the hierarchy to provide a credit-assignment signal without requiring hand-annotated trajectories. The work lands at a moment when mobile GUI agents are rapidly improving on UI understanding and action execution but remain bottlenecked on the app-specific adaptation that real deployment requires; MobileForge surfaces annotation-free hierarchical optimization as the structurally correct primitive for the long-tail app regime.

## Key Facts
- **Authors**: Liu, Guangyi; Zhao, Pengxiang; Wu, Gao; Yin, Yiwen; Li, Mading; Liu, Liang; + 5 more
- **Year**: 2026
- **arXiv**: [2606.19930](https://arxiv.org/abs/2606.19930)
- **Submitted**: 2026-06-18 (cs.AI, cs.CL, cs.CV)
- **Discovered via**: emergent-concept search on 2026-06-26 (mobile-gui-agent / annotation-free-adaptation / hierarchical-policy / feedback-guided-optimization / app-specialization theme)
- **Sibling surface**: same lead authors as MemGUI-Agent (Run 34, 2026-06-25) — Liu, Guangyi; Wu, Gao; Zhao, Pengxiang — but a *distinct axis* (annotation-free hierarchical adaptation vs proactive context management)

## Key Contributions
- Identifies a structural scaling bottleneck in mobile GUI agent deployment: per-app trajectory annotation is the binding cost constraint, and self-improvement pipelines that operate on flat single-level trajectories fail to exploit the natural hierarchy of UI actions, app state transitions, and task outcomes
- Proposes MobileForge, an annotation-free adaptation pipeline combining *hierarchical policy structure* (UI-level, app-level, task-level decisions as a layered policy) with *feedback-guided optimization* (task-success signals flow up the hierarchy to credit-assign without per-trajectory labels)
- Demonstrates that the hierarchical structure enables substantially better sample efficiency than flat-trajectory self-improvement baselines on the long-tail app regime, with task-success rates improving under the same interaction budget
- Surfaces *hierarchy-as-credit-assignment-structure* as a load-bearing primitive for annotation-free agent adaptation: the structural relationship between UI actions, app state, and task outcomes is the right inductive bias for credit assignment, replacing the missing annotation signal with a structurally-grounded learning signal

## Related Papers
- [[memgui-agent-end-to-end-long-horizon-mobile-gui-agent-proactive-context-2606.19926]] — sibling same-author mobile-GUI work on *proactive context management* (MemGUI-Agent surfaces context-management-as-policy on long-horizon tasks; MobileForge surfaces hierarchy-as-credit-assignment on annotation-free adaptation — together they form a complementary two-axis treatment of mobile GUI agent deployment from the same research group)
- [[capable-but-careless-do-computer-use-agents-follow-contextual-integrity-2606.23189]] — sibling CUA contextual-integrity compliance (Capable-But-Careless audits rule-following; MobileForge targets deployment-readiness via adaptation — together they bracket CUA safety between execution-time compliance and deployment-time adaptation)
- [[aohp-an-open-source-os-level-agent-harness-for-personalized-efficient-and-2606.23449]] — sibling OS-level agent harness (AOHP argues the OS must treat agents as first-class actors; MobileForge surfaces hierarchy-as-policy-structure as the agent-internal complement to AOHP's external-first-class treatment)
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — sibling agent-memory design-space survey (Are-Ready surveys memory architectural choices; MobileForge instantiates the hierarchical-policy choice on the mobile GUI deployment regime)
- [[gatemem-benchmarking-memory-governance-in-multi-principal-shared-memory-agents-2606.18829]] — sibling multi-principal memory governance (GateMem isolates access-control as a memory axis; MobileForge isolates hierarchy as a policy axis — together they show memory and policy are the two structurally distinct axes of agent design for multi-user deployment)
