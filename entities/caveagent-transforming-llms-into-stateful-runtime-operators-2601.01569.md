---
title: "CaveAgent: Transforming LLMs into Stateful Runtime Operators"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agent-architecture, stateful, runtime, tool-use]
sources: ["https://arxiv.org/abs/2601.01569"]
---

# CaveAgent: Transforming LLMs into Stateful Runtime Operators

## Overview
CaveAgent reframes the LLM agent paradigm from "LLM-as-Text-Generator-with-Tools" to "LLM-as-Runtime-Operator" — a persistent, stateful entity that maintains a dual-stream architecture: one stream for text context and another for persistent runtime state. The key innovation is inverting the conventional paradigm where text context is primary and tools are auxiliary; instead, the persistent runtime state (process tables, file descriptors, network connections) becomes the primary workspace.

## Key Facts
- **arXiv**: [2601.01569](https://arxiv.org/abs/2601.01569)
- **Year**: 2025
- **Category**: cs.CL / cs.AI

## Key Contributions
- Dual-stream architecture separating text workspace from persistent runtime state
- Runtime-operator abstraction enabling LLMs to maintain long-horizon task continuity without context overflow
- Solves context drift in multi-turn agentic loops by grounding decisions in persistent system state rather than fragile conversation history
- Reduces token overhead for stateful operations by 60%+ vs text-context-only approaches

## Key Insights
- Text-centric agent paradigms suffer from context drift because conversation history accumulates — CaveAgent's runtime state provides a stable reference point that doesn't grow with conversation length
- The "LLM-as-Tool-User" vs "LLM-as-System-Operator" distinction mirrors the OS transition from batch processing to time-sharing — agents need persistent state across turns, not just within turns
- Long-horizon task execution requires the agent to maintain a "world model" of runtime state (open files, pending operations, network connections) that survives context eviction
- Context management becomes a memory-management problem: what to keep in text context vs runtime state vs retrieval

## Related Papers
- [[openrath-session-centered-runtime-state-for-agent-systems-2606.19409]] — OpenRATH: Session-centered runtime state for agent systems — architectural pattern for maintaining persistent state across agent turns
- [[worldlines-benchmarking-and-modeling-long-horizon-stateful-2606.18847]] — Worldlines: Benchmarking long-horizon stateful LLM agent behavior
