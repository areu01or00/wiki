---
title: "When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [model-combination, ensemble, co-failure, mixture-of-agents, routing, voting, multi-model, llm]
sources: ["https://arxiv.org/abs/2606.27288"]
---

# When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models

## Overview
Chen, Josef (2026) introduces the **co-failure ceiling** as a structural diagnostic for multi-model LLM systems — proving that for any policy whose output is one member-model answer, accuracy cannot exceed 1 − β, where β is the rate at which every model in the pool is simultaneously wrong on the same query; across 67 frontier models from 21 providers, the empirically observed all-wrong rate β is *underpriced* by standard pairwise-error-correlation ρ — even tetrachoric-calibrated single-factor models miss the tail by ~2.5× on open-ended mathematics (observed β = 0.052 vs. 0.023 under the full 67-model Gaussian copula, 90% CI 1.7–3.4) and β = 0.079 on execution-graded code. The work exposes that gains come from models failing on *different* questions, not from adding more models — surfacing *co-failure-rate-as-system-ceiling-primitive* as the load-bearing primitive for evaluating multi-model LLM systems.

## Key Facts
- **Authors**: Chen, Josef
- **Year**: 2026
- **arXiv**: [2606.27288](https://arxiv.org/abs/2606.27288)
- **Date**: 2026-06-25

## Key Contributions
- **Co-failure ceiling theorem**: for any policy whose output is one member-model answer, accuracy cannot exceed 1 − β, where β is the rate at which every model is wrong on the same query — surfacing *co-failure-rate-as-architectural-ceiling-primitive* as the structurally correct bound for multi-model LLM systems, distinct from average-pairwise-error-correlation ρ (where the load-bearing axis is *joint-failure-tail-rate* rather than *marginal-pairwise-correlation*), and from oracle upper-bound estimation (where the load-bearing axis is *finite-sample-Clopper-Pearson-certificate-on-largest-gain* rather than *infinite-data-best-case*).
- **Empirical β underpricing of standard diagnostics**: across 67 models from 21 providers, even a tetrachoric-calibrated single-factor Gaussian-copula model underprices β by ~2.5× on open-ended mathematics (observed β = 0.052 vs. copula-implied 0.023, 90% CI 1.7–3.4, k = 17) and β = 0.079 on execution-graded code — surfacing *pairwise-correlation-insufficient-for-tail-identification-primitive* as the load-bearing empirical-validity primitive showing that error laws with identical marginals and pairwise correlations can have different all-wrong rates, contravening the field's standard diagnostic.
- **Re-asking GPQA-Diamond in free-response form reopens the tail**: when the same GPQA-Diamond questions are reformulated from multiple-choice to free-response form, β rises to 0.127 with a five-judge panel κ = 0.73–0.92, locating co-failure in *answer format* rather than subject matter — surfacing *format-induced-co-failure-primitive* as the load-bearing question-design primitive showing that format constraints (multiple-choice vs free-response) systematically shift the all-wrong tail.
- **Low-ρ heterogeneous ensembles beat high-ρ Self-MoA only at matched quality**: at matched single-model quality, low-ρ heterogeneous ensembles beat high-ρ Self-MoA, but on checkable tasks in the pool, combining models rarely beats the single best model without a strong query-level routing signal — surfacing *routing-signal-as-multi-model-gatekeeper-primitive* as the load-bearing practical-condition primitive and *gains-come-from-complementary-failure-not-model-count-primitive* as the load-bearing design principle distinguishing effective multi-model systems from naïve ensembling.
- **Clopper-Pearson finite-sample β certificate**: gives a finite-sample upper bound on the largest gain any router/vote/cascade could deliver *before training the router* — surfacing *pre-training-gain-certificate-primitive* as the load-bearing engineering primitive making it possible to evaluate multi-model deployment decisions without building the routing system first.

## Related Papers
- [[emergent-concepts]] — Parent wiki page that motivated this discovery
- [[efficient-and-trainable-language-model-test-time-scaling-via-local-branch-routing-2606.25354]] — Sibling routing primitive — local-branch routing routes between *local model variants*, Co-Failure Ceiling diagnoses *multi-frontier-model combination* — together they bracket the routing primitive between per-query model-internal routing and pool-level model-combination ceiling
- [[a-theoretical-model-for-task-routing-in-mixture-of-expert-transformers-2606.14398]] — Sibling theoretical-routing primitive — task-routing-theory provides *theoretical support for localized knowledge circuits*, Co-Failure Ceiling provides *empirical-theoretical diagnostic of multi-model combination limits* — together they bracket routing from intra-model MoE theory to inter-model combination diagnostics
- [[odar-principled-adaptive-routing-for-llm-reasoning-via-active-inference-2602.23681]] — Sibling active-inference routing primitive — ODAR routes between *Fast/Slow reasoning models* via free-energy fusion, Co-Failure Ceiling exposes *when such routing cannot help* via the β bound — together they bracket routing between constructive routing-policy and structural ceiling diagnosis