---
title: "Narration-of-Thought: Inference-Time Scaffolding for Defeasible Reasoning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-time-reasoning, defeasible-reasoning, chain-of-thought, llm-reasoning]
sources: ["https://arxiv.org/abs/2606.26366"]
---

# Narration-of-Thought: Inference-Time Scaffolding for Defeasible Reasoning

## Overview
Defeasible reasoning — the ability to revise conclusions when new evidence contradicts prior assumptions — is a known weakness in autoregressive LLMs. This paper proposes "Narration-of-Thought" (NoT), an inference-time scaffolding technique that generates explicit narrative chains expressing the model's assumptions and potential counterarguments as it reasons, enabling better belief revision before committing to an answer. NoT operates entirely at inference time without requiring fine-tuning.

## Key Facts
- **Authors**: Cooper, Patrick; Velasquez, Alvaro
- **Year**: 2026
- **arXiv**: [2606.26366](https://arxiv.org/abs/2606.26366)
- **Date**: 2026-06-24

## Key Contributions
- Introduces Narration-of-Thought (NoT), a prompting scaffold that generates explicit assumption-narration and potential counterargument tracks during inference
- Demonstrates significant improvement on established defeasible reasoning benchmarks (+23% absolute over standard chain-of-thought)
- Shows NoT generalizes across model families (GPT-4 class, Claude class, open-source models) without task-specific fine-tuning
- Analysis shows NoT's benefit is largest on tasks requiring belief revision after contradictory evidence — where standard CoT fails

## Related Papers
- [[a-verifiable-search-is-not-a-learnable-chain-of-thought-2606.21884]] — Demonstrates that search-verification and chain-of-thought learning interact differently; NoT provides a complementary reasoning-scaffold approach
- [[adaptive-test-time-compute-allocation-for-reasoning-llms-via-constrained-policy-optimization-2604.14853]] — Adaptive test-time compute as a complementary reasoning control mechanism
- [[bridging-the-gap-between-latent-and-explicit-reasoning-with-looped-transformers-2606.31779]] — Latent vs explicit reasoning bridging; NoT's explicit narration surfaces latent assumptions that would otherwise remain implicit
- [[agentic-chain-of-thought-steering-for-efficient-and-controllable-llm-reasoning-2606.03965]] — Agentic CoT steering; NoT extends the controllable reasoning scaffold paradigm to defeasible revision
