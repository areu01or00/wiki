---
title: "Perfect Detection, Failed Control: The Geometry of Knowing vs. Steering in Language Models"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [interpretability, controllability, mechanistic-interpretability, geometry, safety, steering]
sources: ["https://arxiv.org/abs/2606.24952"]
---

# Perfect Detection, Failed Control: The Geometry of Knowing vs. Steering in Language Models

## Overview
This paper demonstrates a fundamental geometric mismatch in mechanistic interpretability: the direction in activation space that best *detects* a behavior (via linear classification) is often poorly aligned with the direction that best *controls* that behavior (via intervention). Across four behavior families (fact retrieval, refusal, sycophancy, activation P300), the authors measure the angle between detect-and-control directions and find systematic misalignment — explaining why controllability results from SAE/circuit interpretability often fail to transfer to steering interventions. The key insight is that detectability relies on the information geometry of the model's representations, while controllability requires a direction that causally influences the computation graph.

## Key Facts
- **Authors**: Galeone, Cosimo; Ettorre, Anna; Park, Minsu; Ettorre, Giuseppe; Ligorio, Daniele
- **Year**: 2026
- **arXiv**: [2606.24952](https://arxiv.org/abs/2606.24952)
- **Online date**: 2026/06/23

## Key Contributions
- **Detect-vs-control misalignment**: The first systematic measurement of angular distance between detection directions and control directions across four behavior families — finding systematic 30-90° misalignment that explains why detection-accurate interventions often fail to control.
- **Geometric account**: Models learn to respond to concepts in directions that are information-rich for read-out (detection), but the causal mechanism for generating that concept may be distributed across multiple computation paths — steering only the read-out direction does not redirect the underlying computation.
- **SAE probing comparison**: Probes trained to detect concepts via SAE features accurately identify where behaviors are represented, but steering those same SAE feature directions produces only weak behavioral changes — confirming the geometry mismatch is structural to SAE-based interpretability.
- **Implications for steering**: The paper argues that effective steering requires finding the *causal* direction (what computation actually produces the behavior) rather than the *readout* direction (what pattern in activations best predicts the behavior) — a fundamental reframing of the steering problem.

## Related Papers
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]] — Related mechanistic interpretability: both papers probe internal representations for safety-relevant behaviors; this paper's detect-vs-control geometry complements the entropy-dynamics probe approach.
- [[a-low-rank-subspace-analysis-of-llm-interventions-2606.14388]] — Related intervention theory: both diagnose why interventions fail to generalize across behaviors; this paper's geometric account (angular misalignment) extends the asymmetric-propagation finding from subspace analysis.
- [[interpretability-can-be-actionable-2605.11161]] — Related actionability: both probe when interpretability findings transfer to practical interventions.
