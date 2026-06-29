---
title: "Emergent Causal-Geometric Dynamics Across Depth in Large Language Models"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [causal-representations, geometry, depth-dynamics, llm, mechanistic-interpretability]
sources: ["https://arxiv.org/abs/2602.04931"]
---

# Emergent Causal-Geometric Dynamics Across Depth in Large Language Models

## Overview
Geometric analyses of LLM representations reveal structured variation across depth but remain correlational with respect to token prediction. The authors perform causal interventions to characterise how representational geometry changes with depth — finding that causal intervention efficacy varies by depth in a systematic way, with early layers showing more modular (discrete-causal) structure and later layers showing more continuous (geometric) structure. The paper links causal dynamics to geometric dynamics across the depth axis for the first time.

## Key Facts
- **Authors**: Shahar Haim, Daniel C McNamee
- **Year**: 2026
- **arXiv**: [2602.04931](https://arxiv.org/abs/2602.04931)

## Key Contributions
- **Depth-dependent causal efficacy profile**: causal interventions on hidden states are most impactful at specific depth ranges depending on the task
- **Links geometric structure to causal dynamics** — shows the geometric analyses are not merely correlational when causally grounded
- **Unifying account** bridging prior geometric (e.g., superposition) and causal (e.g., circuit-level) approaches
- **First depth-causality map for LLM representations** — shows how causal structure emerges across transformer layers
- **Application to Belief-or-Circuitry**: the depth axis may explain why graph-tracking succeeds in certain layers

## Related Papers
- [[belief-or-circuitry-causal-evidence-for-in-context-graph-learning-2605.08405]] — In-context graph tracking mechanism may concentrate in specific depth layers per this paper's depth map
- [[causality-is-key-for-interpretability-claims-to-generalise-2602.16698]] — This paper's causal geometry findings require causal validity grounding per that framework
