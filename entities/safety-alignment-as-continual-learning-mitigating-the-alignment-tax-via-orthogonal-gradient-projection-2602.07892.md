---
title: "Safety Alignment as Continual Learning: Mitigating the Alignment Tax via Orthogonal Gradient Projection"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [safety-alignment, alignment-tax, continual-learning, catastrophic-forgetting, orthogonal-gradient]
sources: ["https://arxiv.org/abs/2602.07892"]
---

# Safety Alignment as Continual Learning: Mitigating the Alignment Tax via Orthogonal Gradient Projection

## Overview
Reframes the alignment tax (safety post-training reducing general utility) as a continual-learning problem of gradient interference between shifted data distributions, and proposes OGPSA — Orthogonal Gradient Projection for Safety Alignment — which estimates a low-rank reference subspace from gradients on general-capability data and removes the in-subspace component from each safety gradient. Lightweight update rule compatible with SFT, DPO, and sequential SFT→DPO pipelines; improves safety-utility trade-off without large-scale replay.

## Key Facts
- **Authors**: Guanglong Sun, Siyuan Zhang, Liyuan Wang, Jun Zhu, Hang Su, Yi Zhong
- **Year**: 2026
- **arXiv**: [2602.07892](https://arxiv.org/abs/2602.07892)
- **Submitted**: 8 Feb 2026 (v1), revised 12 May 2026 (v2)
- **Subjects**: cs.LG, cs.CL

## Key Contributions
- **Continual-learning reframing of the alignment tax** — sequential alignment stages expose the model to shifted data distributions and objectives whose gradients interfere with directions that support previously acquired general capabilities; first-order mechanism for mitigating capability regression.
- **OGPSA update rule** — estimates a low-rank reference subspace from gradients on a small set of general-capability data, removes the in-subspace component from each safety gradient; the resulting update is the steepest local safety-descent direction subject to first-order preservation constraints on the reference objectives.
- **Pipeline compatibility** across SFT, DPO, and sequential SFT→DPO; avoids large-scale replay (only requires periodic reference-gradient computation).
- **Empirical improvements** on the safety-utility trade-off: average performance gain under sequential SFT→DPO increases from 33.98% to 42.74% on Qwen2.5-7B-Instruct and from 19.74% to 32.98% on Llama3.1-8B-Instruct.

## Related Papers
- [[value-alignment-tax-measuring-value-trade-offs-in-llm-alignment-2602.12134]] — Sibling empirical alignment-tax measurement (also 2026-02)
- [[deeper-is-not-always-better-mitigating-the-alignment-tax-via-confident-layer-decoding-2606.21906]] — Alternative alignment-tax mitigation via confident-layer decoding (Run 71 pick)
- [[attribution-guided-continual-learning-for-llms-2605.05285]] — Continual-learning sibling via gradient-modulation-by-element-wise-parameter-importance (Run 63 pick)
