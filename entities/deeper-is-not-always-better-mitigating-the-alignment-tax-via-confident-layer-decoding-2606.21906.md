---
title: "Deeper is Not Always Better: Mitigating the Alignment Tax via Confident Layer Decoding"
created: 2026-06-20
updated: 2026-06-20
type: entity
tags: [architecture, alignment, inference, layer-decoding, training-free, alignment-tax]
sources: ["https://arxiv.org/abs/2606.21906"]
---

# Deeper is Not Always Better: Mitigating the Alignment Tax via Confident Layer Decoding

## Overview
Autoregressive generation in large language models (LLMs) conventionally decodes from the final layer, assuming that deeper representations yield more reliable next-token predictions. We revisit this assumption by revealing a recurring Guess-Refine-Perturb dynamic: early layers form coarse guesses, intermediate layers refine reasoning-relevant semantics, and final layers can perturb these refined predictions toward generic or alignment-preferred tokens. We introduce Confident Decoding, a training-free decoding strategy that dynamically selects the most reliable near-final layer through entropy-guided conservative backward search.

## Key Facts
- **Authors**: Zhang, Xuanming, Zhoubian, Sining, Chen, Yuxuan, et al.
- **Year**: 2026
- **Date**: 2026-06-20
- **arXiv**: [2606.21906](https://arxiv.org/abs/2606.21906)
- **Subjects**: Computation and Language (cs.CL)

## Key Contributions
- Identifies a recurring Guess-Refine-Perturb dynamic across LLM depth: early layers form coarse guesses, intermediate layers refine reasoning-relevant semantics, and final layers perturb the refined predictions toward generic or alignment-preferred tokens
- Reveals that final-layer decoding is not always optimal for autoregressive generation — challenging the universal assumption that deeper representations yield more reliable next-token predictions
- Introduces Confident Decoding, a training-free decoding strategy that selects intermediate-layer predictions when the model is more confident in them than in the final layer
- Demonstrates measurable alignment-tax mitigation: Confident Decoding recovers lost reasoning quality while preserving the alignment surface, with no additional training cost

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
