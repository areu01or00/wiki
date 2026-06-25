---
title: "A Verifiable Search Is Not a Learnable Chain-of-Thought"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [reasoning, chain-of-thought, distillation, fine-tuning, reasoning-theory, evaluation]
sources: ["https://arxiv.org/abs/2606.21884"]
---

# A Verifiable Search Is Not a Learnable Chain-of-Thought

## Overview
This paper isolates a class of tasks — verifiable search problems solvable by short programs — for which chain-of-thought (CoT) distillation provably fails. Across nine reasoning tasks with deterministic generators, forward-computable tasks (lookup, arithmetic, an 8-bit boolean task) install readily via LoRA distillation, but cryptarithm does not: distilling its backtracking search holds at 0.01-0.07 across eleven CoT designs, RL from verifiable rewards, and self-training — even though a search solver answers 71% of instances. The work provides a mechanistic account of why: the model does the arithmetic on 97-100% of lines and ranks the correct cipher in its top eight on 71%, but cannot carry the search forward as a left-to-right derivation; fine-tuning learns the shape of a verifiable elimination step while its verdicts become unconditional templates, correct only 16-57% of the time.

## Key Facts
- **Authors**: Harsh Patel
- **Year**: 2026
- **arXiv**: [2606.21884](https://arxiv.org/abs/2606.21884) ([pdf](https://arxiv.org/pdf/2606.21884))
- **Date published**: 2026-06-20
- **Subjects**: cs.LG
- **Methodology**: Nine deterministic-generator reasoning tasks, public and hidden splits share generators; rank-≤32 LoRA distillation over a 30B (3.5B-active) Nemotron model; controlled intervention with key reveal; cross-backbone sweep from 3B to 671B.

## Key Contributions
- **A class of CoT-distillable vs CoT-undistillable tasks**: forward-computable tasks (lookup, arithmetic, 8-bit boolean) transfer (≥0.99, 0.68); search-style tasks like cryptarithm do not, even with explicit search traces.
- **Mechanistic account of the gap**: the model exhibits the right sub-skills (97-100% line-level arithmetic, 71% top-8 cipher ranking) but cannot execute the backtracking structure as a left-to-right derivation; verdict-as-token patterns become unconditional templates at 16-57% correctness.
- **Cross-backbone invariance**: the ceiling holds from 3B to 671B, across fine-tuning and prompting, isolating the failure to CoT-distillation-as-mechanism rather than model scale.
- **Controlled intervention**: revealing the cipher key turns the derivation forward and lifts the same instance — proving the gap is structural (search vs derivation) and not capability.
- **Implication for RLVR**: RL from verifiable rewards, self-training, and eleven CoT designs all hit the same ceiling — verifiable answer ≠ learnable derivation.

## Related Papers
- [[openthoughts-agent-data-recipes-for-agentic-models-2606.24855]] — sibling agentic-RL data-recipe work; shares the verifiable-rewards framing but on agent trajectories rather than CoT distillation.
- [[improved-large-language-diffusion-models-2606.25331]] — alternative factorization direction (masked diffusion); orthogonal to this paper's autoregressive CoT-distillation critique but suggests non-CoT factorization routes around the verdict-as-template failure.
- [[emergent-concepts]] — parent meta-page that catalogued this paper as part of the LLM reasoning-theory / chain-of-thought-learning theme.