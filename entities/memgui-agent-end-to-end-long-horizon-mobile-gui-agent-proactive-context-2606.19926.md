---
title: "MemGUI-Agent: An End-to-End Long-Horizon Mobile GUI Agent with Proactive Context Management"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [mobile-gui-agent, long-horizon, context-management, memory, agent, qwen3-vl]
sources: ["https://arxiv.org/abs/2606.19926"]
---

# MemGUI-Agent: An End-to-End Long-Horizon Mobile GUI Agent with Proactive Context Management

## Overview
Liu et al. introduce MemGUI-Agent, an end-to-end mobile GUI agent for long-horizon tasks that require remembering progress, preserving UI facts, and controlling prompt growth — built on Context-as-Action (ConAct), which casts context management as first-class actions emitted by the same policy that selects UI actions, so the agent decides *when* to compress, evict, persist, or restore context as part of the action sequence rather than via a separate external memory module. The release includes MemGUI-3K, a memory-intensive trajectory dataset of teacher rollouts from MemGUI-Agent using ConAct, and MemGUI-8B-SFT, an 8B model fine-tuned from Qwen3-VL-8B-Instruct on the trajectory set, both shipped open-source to support reproducibility on the long-horizon mobile GUI axis.

## Key Facts
- **Authors**: Guangyi Liu, Gao Wu, Congxiao Liu, Pengxiang Zhao, Liang Liu, Mading Li, Qi Zhang, Mengyan Wang
- **Year**: 2026
- **arXiv**: [2606.19926](https://arxiv.org/abs/2606.19926)
- **Subjects**: cs.CL, cs.AI, cs.HC
- **Submitted**: 2026-06-18
- **Code**: github.com/kwai/MemGUI-Agent

## Key Contributions
- Proposes Context-as-Action (ConAct), which folds context-management operations (compress, evict, persist, restore) into the same policy that selects UI actions — replacing the standard external-memory-controller pattern where memory is managed outside the action loop — and surfaces *context-management-as-policy* as a load-bearing primitive for long-horizon mobile agents.
- Releases MemGUI-3K, a memory-intensive mobile GUI agent trajectory dataset with teacher rollouts demonstrating proactive context management, enabling reproducible training and evaluation of memory-aware mobile GUI agents at the long-horizon regime where existing trajectory corpora saturate.
- Releases MemGUI-8B-SFT, an 8B Qwen3-VL-based model fine-tuned on MemGUI-3K that serves as a reproducible reference for the long-horizon mobile GUI task surface — filling a deployment-relevant gap where the field has had desktop GUI agents but few reproducible mobile GUI agents designed for the memory-axis specifically.
- Validates ConAct on a long-horizon mobile GUI benchmark suite, showing that proactive context management reduces prompt growth without sacrificing task completion and outperforms reactive-context-management baselines that trigger compression only when the context window is exceeded — surfacing *when* to manage context (proactively within the policy) as a structural choice rather than an implementation detail.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on 2026-06-25 (mobile GUI agents / long-horizon / proactive-memory theme).
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Sibling entry on agent-native memory system design; both papers push the memory-as-first-class-primitive axis for LLM agents but from different angles — Are-Ready surveys the design space, MemGUI-Agent instantiates a specific policy-level design (ConAct) for the mobile GUI surface.
- [[gatemem-benchmarking-memory-governance-in-multi-principal-shared-memory-agents-2606.18829]] — Sibling entry on multi-principal shared-memory governance; MemGUI-Agent is single-user mobile, GateMem is multi-principal access-control — together they bracket the agent-memory research surface between proactive context management (MemGUI) and access-control governance (GateMem).
- [[aohp-an-open-source-os-level-agent-harness-for-personalized-efficient-and-2606.23449]] — Sibling entry on OS-level agent harness design; both are open-source agent-harness releases targeting long-horizon deployment regimes, complementary on desktop-OS (AOHP) vs mobile-GUI (MemGUI) axes.
- [[worldlines-benchmarking-and-modeling-long-horizon-stateful-2606.18847]] — Sibling entry on long-horizon stateful embodied agents; both papers target the long-horizon-memory deployment regime but WorldLines is household-robotics simulation and MemGUI-Agent is real mobile device control — together they establish that long-horizon-memory evaluation is a deployment-axis-spanning primitive.