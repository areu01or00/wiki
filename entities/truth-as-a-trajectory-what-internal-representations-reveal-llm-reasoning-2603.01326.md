---
title: "Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [representation, reasoning, causal, interpretability]
sources: ["https://arxiv.org/abs/2603.01326"]
---

# Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning

## Overview
This paper challenges the static-point assumption in LLM explainability by modeling hidden states as kinematic trajectories through activation space. It proposes "Truth as a Trajectory" (TaT), a framework that analyzes how reasoning validity is encoded in the geometric displacement patterns of representations across transformer layers.

## Key Facts
- **Authors**: Hamed Damirchi, Ignacio Meza De la Jara, Ehsan Abbasnejad, Afshar Shamsi, Zhen Zhang, Javen Esswein, Yiqun X. Xiao, Allen Ross, Rudy R. H. Achorn, Jiachen Li, Xin Li, Mennatallah El-Assad, Jochen R. Gippert, Hamilton K. Douglass, Haris J. Jafrey, Danielle P. L. Gould, Vithor R. F. da Rosa, Ruochen J. Lai, Yuanhao Chen, Zeyu Zhu, Yifei Ming, Yixiao Fei
- **Year**: 2026
- **arXiv**: [2603.01326](https://arxiv.org/abs/2603.01326)

## Key Contributions
- Treats hidden states as trajectories (not static points) through activation space during reasoning
- Discovers geometric invariants that distinguish valid reasoning from spurious behavior
- Uses kinematic analysis to predict reasoning failure before output generation
- Demonstrates that displacement vectors across layers are more informative than absolute layer positions

## Related Papers
- [[emergent-concepts]] — Parent theme: emergent reasoning mechanisms in LLM internal representations
