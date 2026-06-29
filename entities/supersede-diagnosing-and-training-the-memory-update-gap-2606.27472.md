---
title: "Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents"
created: "2026-06-29"
updated: "2026-06-29"
type: entity
tags: [agent-memory, memory-update, multi-session-agents, llm-agents]
sources: ["https://arxiv.org/abs/2606.27472"]
---

# Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents

## Overview
LLM agents operate over long multi-session interactions where facts change — users relocate, prices shift, plans are revised. Correct behavior requires overwriting stale facts with current ones, but agents systematically fail to do this. Supersede diagnoses the memory-update gap: the failure to overwrite outdated information with current context, and proposes training interventions to close it. The diagnosis reveals systematic failure modes in how agents weight historical vs. current context during decision-making.

## Key Facts
- **Authors**: Vedant Patel
- **Year**: 2026
- **arXiv**: [2606.27472](https://arxiv.org/abs/2606.27472)
- **Theme**: agent memory diagnosis / memory-update gap / multi-session fact drift

## Key Contributions
- **Memory-update gap diagnosis**: Systematic characterization of when and why LLM agents retain stale facts over current ones in multi-session settings
- **Training intervention**: Proposed methods to strengthen the signal for updating to new facts, closing the gap between historical context and current reality
- **Taxonomy of failure modes**: Categorizes the specific contexts in which the memory-update gap manifests most severely (factual drift, preference drift, spatial/temporal updates)
- **Contrast with prior memory work**: Extends MemProbe (hidden user-state recovery) and ZenBrain (7-layer memory architecture) by identifying the update mechanism itself as the failure point, not storage or retrieval

## Related Papers
- [[emergent-concepts]] — Parent emergent concept discovery
- [[memprobe-probing-longterm-agent-memory-via-hidden-userstate-recovery-2606.24595]] — MemProbe probes what agents remember; Supersede diagnoses why they fail to update what they remember
- [[zenbrain-a-neuroscience-inspired-7-layer-memory-architecture-for-autonomous-ai-s-2604.23878]] — ZenBrain's 7-layer memory architecture; Supersede identifies the update/overwrite layer as the specific failure point
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Plans Don't Persist studies context eviction; Supersede studies context staleness after fact changes — complementary failure modes
