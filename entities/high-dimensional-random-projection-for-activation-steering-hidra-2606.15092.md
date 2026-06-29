---
title: "High-Dimensional Random Projection for Activation Steering in Language Models (HiDRA)"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [representation-engineering, activation-steering, superposition, random-projection, discriminative-features, primitive-class, llm]
sources: ["https://arxiv.org/abs/2606.15092"]
---

# High-Dimensional Random Projection for Activation Steering in Language Models (HiDRA)

## Overview

HiDRA (Pham, Do, Abdullaev, Nguyen, Than; submitted 2026-06-13) is a training-free activation-steering framework that re-derives steering vectors in a random high-dimensional projection space so as to *recover discriminative signals that the standard difference-in-means construction cannot access* under the superposition hypothesis. Drop-in additive to existing steering pipelines, HiDRA surfaces a new primitive: *nonlinear-feature-subspace-as-steering-target*, in which behavioural control is achieved by acting on the projected discriminative structure rather than the raw linear direction.

## Key Facts
- **Authors**: Minh-Hieu Pham, Bach Do, Laziz Abdullaev, Tan Minh Nguyen, Khoat Than
- **Year**: 2026
- **Submission date**: 2026-06-13
- **arXiv**: [2606.15092](https://arxiv.org/abs/2606.15092)
- **Subjects**: Machine Learning (cs.LG)

## Key Contributions

- **Superposition-grounded critique of difference-in-means steering**: argues that classical contrastive-activation-addition (CAA) and difference-in-means steering methods recover *only* the mean-shift signal and therefore *cannot* recover discriminative information that exists in the nonlinear feature subspace — a structural limitation tied to the superposition hypothesis under which many features are entangled within a smaller set of directions.
- **High-Dimensional Random-projection for Activation Steering (HiDRA)**: introduces a training-free, drop-in module that performs activation addition in a *randomly projected high-dimensional space*; by lifting activations into a higher-dimensional random subspace before steering, the discriminative structure between classes is provably better preserved (Johnson–Lindenstrauss-style preservation arguments) and can be re-extracted by linear methods that would otherwise be blind to it.
- **Provable discriminative-structure recovery beyond linear methods**: HiDRA's analysis formalises that the projected space admits the recovery of discriminative directions unreachable by mean-shift alone; this is the load-bearing theoretical contribution distinguishing HiDRA from contrastive-activation-addition baselines.
- **Empirical validation across diverse LLM families and benchmarks**: HiDRA consistently outperforms baseline counterparts on behavioural-control benchmarks while introducing no significant computational overhead, demonstrating that the random-projection preprocessing is a free primitive for steering practitioners.
- **First activation-steering method in the wiki explicitly grounded in the superposition hypothesis**: most steering papers treat the steering vector as a linear causal direction; HiDRA treats the residual stream as a *superposed* subspace where linear methods see only one shadow, and the projected space sees many.

## Related Papers
- [[scalable-circuit-learning-for-interpreting-large-language-models-2606.16939]] — Sibling interpretability primitive: circuit-discovery in superposition-aware settings complements HiDRA's projection-based steering.
- [[global-evolutionary-steering-refining-activation-steering-control-via-cross-layer-consistency-2603.12298]] — Sibling steering primitive: GER-steer refines vectors via cross-layer consistency; HiDRA refines via projection-space discriminative recovery.
- [[the-lattice-representation-hypothesis-of-large-language-models-2603.01227]] — Conceptual sibling: lattice-representation view of LLM features as a geometric primitive compatible with HiDRA's superposition view.
- [[interpretability-can-be-actionable-2605.11161]] — Sibling interpretability-and-actionability paper.
- [[steered-llm-activations-are-non-surjective-2604.09839]] — Critical sibling: formal separation between white-box steerability and black-box prompting; HiDRA's projection-based steering falls inside the white-box regime and inherits the implications.
- [[emergent-concepts]] — Parent meta-page that led to this discovery.