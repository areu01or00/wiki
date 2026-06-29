---
title: "Distilling Linearized Behavior into Non-Linear Fine-Tuning for Effective Task Arithmetic"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [task-arithmetic, model-merging, distillation, linearization, fine-tuning, llm]
sources: ["https://arxiv.org/abs/2605.18993"]
---

# Distilling Linearized Behavior into Non-Linear Fine-Tuning for Effective Task Arithmetic

## Overview
Sommariva, Thomas; Morandi, Francesca; Calderara, Simone; Porrello, Angelo (2026) bridge the gap between linear and standard non-linear fine-tuning for effective task arithmetic by showing that *linearity with respect to weight perturbations* — a property defined in parameter space — can be enforced through constraints in activation space during training; concretely, hidden representations from a curvature-regularized linearized teacher are distilled into a non-linear student trained via conventional fine-tuning, producing models that inherit the key composition-friendly properties of linearized models for task arithmetic while paying no inference-time overhead — surfacing *activation-space-linearity-distillation-primitive* as the load-bearing primitive for merging-compatible fine-tuning at standard deployment cost.

## Key Facts
- **Authors**: Sommariva, Thomas; Morandi, Francesca; Calderara, Simone; Porrello, Angelo
- **Year**: 2026
- **arXiv**: [2605.18993](https://arxiv.org/abs/2605.18993)
- **Date**: 2026-05-18 (online 2026-05-22)

## Key Contributions
- **Activation-space enforcement of parameter-space linearity**: shows that linearity with respect to weight perturbations — a property defined in parameter space — can be enforced through constraints in activation space during training — surfacing *parameter-space-property-as-activation-space-objective-primitive* as the structurally correct translation primitive, distinct from parameter-regularization approaches (where the load-bearing axis is *hidden-representation-constraints-on-non-linear-student* rather than *weight-decay-on-the-student-itself*), and from linearization-via-tangent-space-only approaches (where the load-bearing axis is *linearization-property-via-distillation* rather than *linearization-by-restricting-the-training-trajectory*).
- **Curvature-regularized linearized teacher distillation**: hidden representations from a curvature-regularized linearized teacher are distilled into a non-linear student via conventional fine-tuning — surfacing *curvature-regularized-teacher-as-distillation-source-primitive* as the load-bearing teacher-design primitive controlling the inductive bias inherited by the student without forcing the student into the linearized regime.
- **Inheritance of linearized-model composition properties**: the resulting model inherits key properties of linearized models for task arithmetic — enabling effective composition of task vectors with strong performance across vision and language benchmarks — surfacing *linearization-property-inheritance-via-distillation-primitive* as the load-bearing *composition-portability-primitive* allowing task-vector composition to work on conventional non-linear fine-tuned models.
- **Zero inference-time overhead**: the approach achieves merging-compatibility without restricting the student to a linearized regime at inference time, paying no inference-cost penalty — surfacing *no-inference-time-overhead-merging-compatible-fine-tuning-primitive* as the load-bearing *deployment-cost-primitive* solving the practical limitation that linearized models have limited expressivity during training and higher computational costs at inference time.
- **Strong performance across vision and language benchmarks**: achieves effective task-vector composition across diverse domains — surfacing *cross-domain-task-arithmetic-validity-primitive* as the load-bearing *generalization-primitive* showing that activation-space-linearity constraints work for both vision and language merging tasks.

## Related Papers
- [[emergent-concepts]] — Parent wiki page that motivated this discovery
- [[a-survey-of-on-policy-distillation-for-large-language-models-2604.00626]] — Sibling distillation-survey primitive — On-Policy-Distillation-survey covers *capability-transfer-via-on-policy-rollouts*, Distilling-Linearized-Behavior covers *linearization-property-transfer-via-activation-distillation* — together they bracket distillation from rollout-aligned capability transfer to property-aligned property transfer
- [[dream-dense-retrieval-embeddings-via-autoregressive-modeling-2606.24667]] — Sibling dense-embedding primitive — Dream provides *autoregressive dense retrieval embeddings*, Distilling-Linearized-Behavior provides *autoregressive-friendly task-arithmetic via linearization* — together they bracket autoregressive modeling from dense-representation primitives to linearization-friendly training primitives
- [[energy-based-fine-tuning-of-language-models-2603.12248]] — Sibling training-free fine-tuning primitive — Energy-Based-Fine-Tuning explores *post-training energy landscapes* without inference overhead, Distilling-Linearized-Behavior explores *linearization-friendly fine-tuning* without inference overhead — together they bracket fine-tuning-time-free deployment-cost reduction across distinct mechanisms (energy objective vs linearization distillation)