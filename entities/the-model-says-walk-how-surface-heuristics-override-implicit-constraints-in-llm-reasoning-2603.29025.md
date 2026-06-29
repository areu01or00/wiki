---
title: "The Model Says Walk: How Surface Heuristics Override Implicit Constraints in LLM Reasoning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, heuristic-override, minimal-pair, ablation, falsification, benchmark]
sources: ["https://arxiv.org/abs/2603.29025"]
---

# The Model Says Walk: How Surface Heuristics Override Implicit Constraints in LLM Reasoning

## Overview
Li, Zhang, Jiang, Krishnan, Padman introduce the Heuristic Override Benchmark (HOB) — 500 instances spanning 4 heuristic families and 5 constraint families with minimal pairs and explicitness gradients — and use it to characterize LLM reasoning as a sigmoid-driven salience-override process where distance cues outweigh goals by 8.7–38×, attributing failures to constraint-inference rather than knowledge. The paper pairs HOB with a falsifiable behavioral arc (diagnose-measure-bridge-treat), establishes that thinking-mode ablation drops Gemini 3.1 Pro from 74.6% to 58.4% while explicit goal decomposition recovers 71.2%, and isolates constraint enumeration as the active ingredient of goal-decomposition prompting (5.0 pp vs 3.1 pp for generic CoT).

## Key Facts
- **Authors**: Li, Yubo; Zhang, Lu; Jiang, Tianchong; Krishnan, Ramayya; Padman, Rema
- **Year**: 2026
- **arXiv**: [2603.29025](https://arxiv.org/abs/2603.29025)
- **Online Date**: 2026-06-09
- **Citation Date**: 2026-03-30

## Key Contributions
- **Heuristic Override Benchmark (HOB)**: 500 instances across 4 heuristic families and 5 constraint families with minimal pairs and explicitness gradients as the first systematic minimal-pair-anchored controlled-comparison benchmark for surface-heuristic-vs-implicit-constraint conflicts in LLM reasoning
- **Falsifiable behavioral characterization**: diagnose-measure-bridge-treat arc applied to the car-wash problem across 6 models, identifying a context-independent sigmoid heuristic where the distance cue has 8.7–38× more influence than the goal and attribution better matches keyword association than compositional inference
- **Strict-evaluation negative result across 14 models**: no model exceeds 75% on the 10/10 evaluation, with presence constraints hardest at 44%; thinking-mode ablation on Gemini 3.1 Pro drops from 74.6% (thinking on) to 58.4% (thinking off) and recovers to 71.2% with explicit goal decomposition
- **Constraint-inference failure localization**: 12 of 14 models perform worse when the constraint is removed (by up to 39 pp), revealing a conservative bias; minimal-hint gain of 15 pp and goal-decomposition gain of 5.0 pp (vs 3.1 pp for generic CoT) isolate constraint enumeration as the active ingredient — not generic reasoning
- **Reasoning-mode null result**: after controlling for capability rank, the residual reasoning-mode effect is 1.8 pp and is not significant, providing the first formal no-significant-reasoning-mode-effect null result in a controlled minimal-pair setting
- **Probe generalization**: the sigmoid pattern generalizes parametrically to cost, efficiency, and semantic-similarity heuristics beyond the original car-wash problem

## Related Papers
- [[local-causal-attribution-of-chain-of-thought-reasoning-2606.21821]] — Sibling discovery from Run 99 that probes local causal attribution in CoT; both papers use null-model-style behavioral decomposition to localize reasoning failures
- [[reasoning-models-struggle-to-control-their-chains-of-thought-2603.05706]] — Sibling CoT-control evaluation suite that surfaces a CoT-vs-output controllability asymmetry in reasoning models; complements HOB's strict-evaluation null result
- [[large-language-model-reasoning-failures-2602.06176]] — First embodied-vs-non-embodied × fundamental-vs-application reasoning-failure 2-axis taxonomy in the wiki; complements HOB's heuristic-override taxonomy with a different axis structure
- [[when-errors-become-narratives-a-longitudinal-taxonomy-of-silent-failures-in-a-production-llm-agent-runtime-2606.14589]] — Sibling production-runtime failure taxonomy; complements HOB's controlled-benchmark failure surface with real-world longitudinal data
- [[when-gradients-collide-failure-modes-of-multi-objective-prompt-optimization-for-llm-judges-2605.26046]] — Sibling failure-mode analysis for multi-objective prompt optimization; complements HOB's goal-decomposition 5.0 pp finding as a controlled prompt-failure-mode result
- [[causal-methods-for-llm-development-and-evaluation-2605.25998]] — Sibling causal-methods framework for LLM development/evaluation; both papers use control-variable reasoning to localize LLM behavior
- [[emergent-concepts]] — Parent page that led to this discovery
