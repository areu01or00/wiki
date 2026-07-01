---
title: "Training the Orchestrator: A Supervised Approach to End-to-End PDDL Planning with LLM Agents"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [llm-agent, planning, pddl, neurosymbolic, verifier]
sources: ["https://arxiv.org/abs/2606.21740"]
---

# Training the Orchestrator: A Supervised Approach to End-to-End PDDL Planning with LLM Agents

## Overview
HALO (Hybrid Agent-LEarning Orchestrator) addresses a core bottleneck in LLM-agent planning: the orchestrator itself is a prompted frontier LLM paying full API cost at every refinement step. The paper trains the orchestrator via supervised learning on annotated PDDL planning traces, replacing costly per-step frontier calls with a lightweight learned policy that still leverages classical planners for plan verification.

## Key Facts
- **Authors**: Mangannavar, Rajesh; Coalson, Zachary; Dugar, Pranay + 1
- **Year**: 2026
- **arXiv**: [2606.21740](https://arxiv.org/abs/2606.21740)
- **Date**: 2026-06-19

## Key Contributions
- Supervised learning pipeline for LLM-agent orchestrator using PDDL planning traces
- Reduces per-refinement-step frontier LLM cost by replacing with learned policy
- Retains classical planner for sound plan verification within verifier-checked loop
- Demonstrates that not every refinement step requires a full frontier LLM call

## Related Papers
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — PlanBench-XL: LLM tool-use agents in large-scale tool ecosystems with PDDL formalization
- [[calvert-augmenting-agents-with-calibrated-verifier-telemetry-improves-action-and-learning-in-knowledge-intensive-tasks-2606.21777]] — CalVerT: Verifier telemetry augments agent action and learning in knowledge-intensive tasks
- [[declarative-router-policy-compilation-from-inference-routing-to-agent-orchestration-cross-layer-verification-2603.27299]] — Declarative router: Cross-layer verification for agent orchestration
