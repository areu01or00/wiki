---
title: "Beyond Activation Alignment: The Geometry of Neural Sensitivity"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [representation, geometry, activation, alignment]
sources: ["https://arxiv.org/abs/2605.03222"]
---

# Beyond Activation Alignment: The Geometry of Neural Sensitivity

## Overview
Activation-alignment measures (RSA, CCA, CKA) are widely used to compare biological and artificial neural representations, but this paper provides a systematic theoretical reinterpretation showing that many of these methods primarily measure neural sensitivity rather than representational geometry. The paper reinterprets what these metrics actually capture and establishes geometric foundations for more precise representation comparison.

## Key Facts
- **Authors**: Yavari, Amirhossein; Esfahlani, Farnaz Zamani
- **Year**: 2026
- **arXiv**: [2605.03222](https://arxiv.org/abs/2605.03222)
- **Date**: 2026-05-04

## Key Contributions
- **Theoretical reinterpretation** of RSA/CCA/CKA: shows these measures primarily reflect neural sensitivity (directional variance) rather than geometric similarity between representations
- **Geometry of neural sensitivity**: Establishes formal connections between sensitivity-based and geometry-based representation analysis
- **Critique of activation steering alignment**: Activation steering methods may be exploiting sensitivity anisotropy rather than true geometric correspondence
- **First geometric-sensitivity unification framework** for neural representation analysis — opens new directions for interpreting activation steering and alignment methods
- **Relevant to SAE-guided methods**: The distinction between sensitivity and geometry is directly applicable to understanding SAE feature geometry

## Related Papers
- [[from-weights-to-features-sae-guided-activation-regularization-for-llm--2606.26629]] — SAE-guided activation regularization (shares geometric representation theme)
- [[high-dimensional-random-projection-for-activation-steering-hidra-2606.15092]] — Activation steering via random projection
- [[calibration-collapse-under-sycophancy-fine-tuning-reward-hacking-2604.10585]] — Activation collapse under fine-tuning
