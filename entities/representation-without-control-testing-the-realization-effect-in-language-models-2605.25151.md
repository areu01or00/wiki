---
title: "Representation Without Control: Testing the Realization Effect in Language Models"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [behavioral-simulation, realization-effect, minimal-pair, activation-steering, null-result, mechanistic-interpretability]
sources: ["https://arxiv.org/abs/2605.25151"]
---

# Representation Without Control: Testing the Realization Effect in Language Models

## Overview
Walsh and Barkett use the realization effect — a well-characterized finding in behavioral economics where risk-taking differs systematically after paper versus realized gains and losses — to test whether LLM behavioral simulation reflects human-like cognitive mechanisms or prompt-sensitive surface patterns, evaluating Gemma at three levels (prompt-only, linear readout, activation steering) and finding that **behavioral sensitivity, latent readout, and causal control are three distinct properties that do not automatically co-occur** — a clean null-model-comparison result that surfaces a representational-decoding-causal-control dissociation in LLMs.

## Key Facts
- **Authors**: Walsh, Ciarán; Barkett, Emilio
- **Year**: 2026
- **arXiv**: [2605.25151](https://arxiv.org/abs/2605.25151)
- **Online Date**: 2026-05-24
- **Citation Date**: 2026-05-24

## Key Contributions
- **Three-level dissociation framework**: prompt-only behavioral sensitivity, linear readout of internal representations, and causal control via activation steering evaluated jointly on the realization effect — the first explicit three-level representational-decoding-causal-control dissociation test in the wiki
- **Prompt-only directional mismatch**: prompt-only results show systematic condition sensitivity, but the directional pattern does not reproduce human realization-effect predictions — establishing a null result for surface-pattern reproduction of behavioral-economics findings
- **Latent-readout positive result**: Gemma's residual stream contains a linearly decodable realization-status signal at layer 18 that generalizes to held-out prompts, demonstrating that the realization concept is internally represented even when prompt-only behavior is directionally wrong
- **Causal-control null result**: steering along the realization-status direction does not reliably shift downstream risk choices, with the null result holding across positive scales and in a negative sign-symmetry run — establishing that latent readout is insufficient evidence of behavioral reliance on a representation during downstream decision-making
- **Representational-decoding-causal-control gap**: the paper formalizes the gap between *decoding* (linear readout succeeds) and *control* (steering fails) as a primitive distinction in mechanistic interpretability, going beyond the standard "is the feature present" question to ask "does the model behaviorally rely on the feature"
- **Behavioral-economics cross-discipline primitive**: applies a well-characterized finding from behavioral economics (paper vs realized gains/losses) as a controlled comparison test for LLM behavioral simulation, providing the first cross-discipline behavioral-economics null-model-comparison primitive in the wiki

## Related Papers
- [[local-causal-attribution-of-chain-of-thought-reasoning-2606.21821]] — Sibling local-causal-attribution CoT framework; complements the realization-effect paper's causal-control null result with an attribution-positive CoT case
- [[global-evolutionary-steering-refining-activation-steering-control-via-cross-layer-consistency-2603.12298]] — Sibling cross-layer-consistency steering refinement; both papers use steering as a controlled-comparison primitive, but the realization-effect paper surfaces a steering-failure null result vs the evolutionary refinement's positive steering-control result
- [[a-low-rank-subspace-analysis-of-llm-interventions-2606.14388]] — Sibling low-rank-subspace intervention-side-effect diagnostic; both papers surface the gap between representational readout and behavioral control
- [[interpretability-can-be-actionable-2605.11161]] — Sibling position paper arguing interpretability should be evaluated by concreteness × validation four-quadrant actionability grid; the realization-effect paper provides empirical evidence for the actionability gap
- [[agentic-chain-of-thought-steering-for-efficient-and-controllable-llm-reasoning-2606.03965]] — Sibling CoT-steering controllability framework; complements the realization-effect paper's steering-failure null result
- [[when-gradients-collide-failure-modes-of-multi-objective-prompt-optimization-for-llm-judges-2605.26046]] — Sibling failure-mode analysis; complements the realization-effect paper's directional-mismatch null result with a different failure mode
- [[emergent-concepts]] — Parent page that led to this discovery
