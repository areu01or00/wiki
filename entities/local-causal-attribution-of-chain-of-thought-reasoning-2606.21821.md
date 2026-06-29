---
title: "Local Causal Attribution of Chain-of-Thought Reasoning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [causal-inference, reasoning, interpretability, attribution, structural-causal-model, chain-of-thought]
sources: ["https://arxiv.org/abs/2606.21821"]
---

# Local Causal Attribution of Chain-of-Thought Reasoning

## Overview
AttriCoT, a black-box causal-attribution algorithm for LLM chain-of-thought reasoning. The paper constructs a structural causal model (SCM) on the individual "units" of a specific CoT trace, relates each unit to the log probability of generating subsequent output units, and estimates importance parameters via O(U) forward passes. Evaluated on 5 datasets across 4 reasoning models, AttriCoT produces attributions more faithful to the model's behavior than alternative methods and reveals notable differences in thought structure between models and domains.

## Key Facts
- **Authors**: Dennis Wei, Yannis Belkhiter, Erik Miehling, Radu Marinescu
- **Year**: 2026
- **arXiv**: [2606.21821](https://arxiv.org/abs/2606.21821)
- **Online Date**: 2026-06-20

## Key Contributions
- Local causal-attribution algorithm (AttriCoT) operating on individual "units" of a single CoT trace — distinct from global feature-attribution methods
- Structural causal model (SCM) on CoT units where each unit is causally related to the log probability of generating subsequent output units
- O(U) forward-pass complexity — linear in the number of CoT units, making per-trace attribution tractable
- Black-box compatible — requires only log-probability access, no internal activations or gradients
- Empirical demonstration that CoT thought structure differs significantly between reasoning models and domains

## Related Papers
- [[reasoning-models-struggle-to-control-their-chains-of-thought-2603.05706]] — Sibling discovery from prior run on CoT-controllability asymmetry that surfaces the *verbalization*-side of CoT monitoring
- [[reasoninglens-hierarchical-visualization-and-diagnostic-auditing-for-large-reasoning-models-2606.23404]] — Sibling run-60 pick on hierarchical CoT-trace auditing; AttriCoT complements via per-unit causal attribution
- [[a-latent-computational-mode-in-large-language-models-2601.08058]] — Sibling discovery showing SAE-isolated latent-reasoning features; AttriCoT probes the verbalized side while Latent-Computational-Mode probes the latent side
- [[interpretability-can-be-actionable-2605.11161]] — Sibling run-58 pick arguing interpretability should be evaluated by concreteness × validation; AttriCoT operationalizes the concreteness axis for CoT traces
- [[when-the-chain-of-thought-knows-better-failure-modes-in-multi-turn-reasoning-models-2606.10740]] — Sibling run-60 pick on CoT-Output 2×2 matrix; AttriCoT provides the causal-attribution primitive underlying the "cot-knows-better" detection
- [[agentic-chain-of-thought-steering-for-efficient-and-controllable-llm-reasoning-2606.03965]] — Sibling paper on agentic CoT steering; AttriCoT could supply per-step causal-importance signals for the steering controller
- [[large-language-model-reasoning-failures-2602.06176]] — Sibling survey on embodied-vs-non-embodied reasoning failure modes; AttriCoT's per-unit attribution could localize failure within a trace