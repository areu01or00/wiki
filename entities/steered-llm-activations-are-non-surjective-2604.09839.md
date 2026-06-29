---
title: "Steered LLM Activations are Non-Surjective"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [representation-engineering, activation-steering, surjectivity-theorem, formal-separation, white-box-vs-black-box, primitive-class, llm]
sources: ["https://arxiv.org/abs/2604.09839"]
---

# Steered LLM Activations are Non-Surjective

## Overview

Mishra, Khashabi, Liu (submitted 2026-04-10; ICLR 2026 Workshops Sci4DL & Re-Align) prove a *formal separation theorem*: under practical assumptions, activation steering pushes the residual stream off the manifold of states reachable from discrete prompts, so that — almost surely — *no prompt can reproduce the same internal behaviour that steering induces*. The result establishes a load-bearing primitive: *white-box-steerability ≠ black-box-prompting*, and warns against interpreting the ease of activation steering as evidence of prompt-based interpretability or vulnerability.

## Key Facts
- **Authors**: Aayush Mishra, Daniel Khashabi, Anqi Liu
- **Year**: 2026
- **Submission date**: 2026-04-10; revised 2026-05-07 (v2)
- **Venue**: ICLR 2026 Workshops (Sci4DL, Re-Align)
- **arXiv**: [2604.09839](https://arxiv.org/abs/2604.09839)
- **Subjects**: Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

## Key Contributions

- **Surjectivity framing of the steering question**: casts the white-box-vs-black-box separation as a *surjectivity problem* — for a fixed model, does every steered activation admit a preimage under the model's natural forward pass from a textual prompt? The framing turns a folkloric observation into a well-defined mathematical question.
- **Non-surjectivity theorem for activation steering**: under practical assumptions on the residual-stream geometry, proves that activation steering pushes the residual stream *off the manifold of states reachable from discrete prompts* — i.e., the steered activation has *no textual preimage* — and the result holds *almost surely*.
- **First formal separation between white-box steerability and black-box prompting**: the theorem is a clean primitive that distinguishes two intervention classes that the literature has conflated under the "interpretability" and "safety" umbrellas — *white-box interventions (activation steering, probing, jailbreak-defence)* versus *black-box interventions (prompting, instruction tuning)*. The two are not interchangeable.
- **Empirical illustration across three widely used LLMs**: confirms the theoretical non-surjectivity finding empirically — steered activations lie on portions of the residual stream that no textual prompt can reach, demonstrating the result is not a theoretical artifact.
- **Decoupled-evaluation-protocol recommendation**: argues that the interpretability and safety communities should adopt evaluation protocols that *explicitly decouple white-box from black-box interventions* rather than treating them as substitutes — a methodological primitive with broad downstream impact on jailbreak-defence evaluation, activation-probing trust, and steering-vector deployment.

## Related Papers
- [[high-dimensional-random-projection-for-activation-steering-hidra-2606.15092]] — Sibling steering primitive: HiDRA's projection-based steering falls inside the white-box regime, with implications from this non-surjectivity theorem.
- [[global-evolutionary-steering-refining-activation-steering-control-via-cross-layer-consistency-2603.12298]] — Sibling steering primitive: GER-steer's refined white-box intervention inherits the same formal separation result.
- [[scalable-circuit-learning-for-interpreting-large-language-models-2606.16939]] — Sibling interpretability primitive: circuit-discovery evaluation must also decouple white-box from black-box per the protocol recommendation.
- [[interpretability-can-be-actionable-2605.11161]] — Sibling interpretability-and-actionability paper: actionability evaluation similarly must distinguish intervention classes.
- [[emergent-concepts]] — Parent meta-page that led to this discovery.