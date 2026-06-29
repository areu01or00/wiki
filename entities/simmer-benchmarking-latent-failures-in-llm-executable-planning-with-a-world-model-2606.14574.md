---
title: "SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agent, planning, benchmark, llm]
sources: ["https://arxiv.org/abs/2606.14574"]
---

# SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model

## Overview
SIMMER introduces a benchmark specifically designed to diagnose *latent failures* in LLM-based planning systems — failures that emerge when the world model the agent relies on diverges from the actual environment dynamics. Unlike standard planning benchmarks that measure success rates on solvable tasks, SIMMER surfaces where LLM planners produce *executable* but *incorrect* plans due to incorrect world-state assumptions. The work reveals that frontier LLMs frequently generate plans that are logically coherent yet silently fail when executed because the underlying world model encodes wrong causal relationships or missing state variables.

## Key Facts
- **Authors**: Xiaoxin Lu et al.
- **Year**: 2026
- **arXiv**: [2606.14574](https://arxiv.org/abs/2606.14574)

## Key Contributions
- **Latent failure taxonomy**: Distinguishes between *overt failures* (plan doesn't achieve goal) and *latent failures* (plan achieves goal via incorrect mechanism, or succeeds in simulation but fails in real execution)
- **World-model-grounded benchmark**: SIMMER pairs each planning problem with an explicit world-model specification, enabling precise diagnosis of where the planner's internal model diverges
- **Frontier LLM evaluation**: Systematic evaluation of GPT-4o, Claude 3.5, Gemini 1.5 across latent failure categories reveals that even the strongest models exhibit systematic world-model blind spots in temporal-reasoning and counterfactual planning tasks
- **Failure mitigation strategies**: Proposes world-model verification layers and counterfactual probing as complementary diagnostics

## Related Papers
- [[agentic-world-modeling-foundations-capabilities-laws-and-beyond-2604.22748]] — Foundational world-model taxonomy (L1 Predictor / L2 Simulator / L3 Evolver) that SIMMER's failure taxonomy builds upon
- [[flowr2a-learning-reward-to-action-distribution-for-multimodal-driving-planning-2606.24231]] — Planning companion that addresses multimodal reward-to-action distribution; shares the world-model planning axis with SIMMER but focuses on continuous control rather than discrete executable planning
- [[grace-granularity-regulated-adaptive-computational-efficiency-for-optimal-verification-in-test-time-scaling-2606.19354]] — Verification layer design that could be extended to world-model consistency checking
