---
title: "Robusto-2: Benchmarking Humans & VLMs for Autonomous Driving in Lima & New York City"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [autonomous-driving, vlm, out-of-distribution, geographical-ood, benchmarking, edge-cases, multimodal-cognition]
sources: ["https://arxiv.org/abs/2606.20980"]
---

# Robusto-2: Benchmarking Humans & VLMs for Autonomous Driving in Lima & New York City

## Overview
Cespedes et al. address the structural out-of-distribution generalization gap in VLM-backed action models for autonomous driving — where Self-Driving Cars are expanding internationally and using multimodal systems such as VLMs as the cognitive backbone for their action models, but how well these systems generalize to OOD edge-case scenarios in new geographies has been underexplored despite being the deployment regime — and introduce Robusto-2, a full-factorial study comparing human drivers in Lima (Peru) and New York City against several VLM action models on identical driving scenarios spanning both cities, surfacing geographical-OD as a load-bearing axis of AV generalization that human drivers handle through cultural-context priors and VLM action models handle through statistical co-occurrence in their training distribution.

## Key Facts
- **Authors**: Adrian Cespedes, Marcelo Chincha, Dunant Cusipuma, Victor Flores-Benites, David Ortega, Arturo Deza
- **Year**: 2026
- **arXiv**: [2606.20980](https://arxiv.org/abs/2606.20980)
- **Subjects**: cs.CV, cs.AI, cs.RO
- **Submitted**: 2026-06-18

## Key Contributions
- Diagnoses geographical-OD as a structural generalization axis for VLM-backed AV action models — the field has been validating AV systems primarily on US/EU-centric driving distributions, leaving the deployment regime in geographies with different signage conventions, road-user behavior patterns, lane-marking conventions, and informal-driving rules under-evaluated even though this is the international-expansion regime that AV deployment is entering.
- Proposes Robusto-2, a full-factorial human-vs-VLM benchmark in Lima (Peru) and New York City, where the same set of driving scenarios is presented to (a) human drivers in each city, (b) human drivers cross-rated against the other city's scenarios, and (c) several state-of-the-art VLM action models, enabling decomposition of VLM underperformance into (1) cross-cultural scenario-recognition failures, (2) action-model reasoning failures, and (3) systematic geographical-prior mismatches between VLM training distribution and target geography.
- Surfaces the human-prior-to-VLM-prior gap as a structural axis — human drivers in each city carry cultural-context priors that inform action selection (e.g., informal-turn-taking patterns, pedestrian-behaviour expectations, signage conventions), while VLM action models rely on statistical co-occurrence in their training distribution; the human-VLM gap in OOD cities reveals which action-decision primitives are learnable from training data and which require explicit cultural-context grounding.
- Validates geographical-OD as a load-bearing primitive for AV generalization evaluation, arguing that single-geography benchmarks systematically overstate VLM action-model capability and that full-factorial cross-geography benchmarks are required to characterize deployment-relevant generalization — surfacing *benchmark-axis-decomposition* as the methodology-level contribution (rather than yet another single-geography benchmark).

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on 2026-06-26 (autonomous-driving / VLM-action-model / geographical-OD / cross-cultural-benchmarking theme).
- [[flowr2a-learning-reward-to-action-distribution-for-multimodal-driving-planning-2606.24231]] — Sibling entry on multimodal driving planning; both papers ground the AV research surface on VLM/multimodal cognition — FlowR2A learns reward-to-action distribution for driving planning, Robusto-2 evaluates how VLM action models generalize across geographies, together they bracket the VLM-for-driving surface between training-time planning (FlowR2A) and evaluation-time cross-geography generalization (Robusto-2).
- [[ebench-elemental-diagnosis-of-generalist-mobile-manipulation-policies-2606.18239]] — Sibling entry on multi-axis diagnostic; both papers replace aggregate-success-rate evaluation with multi-axis decomposition — EBench decomposes manipulation-policy capability into 5×4 dimensions, Robusto-2 decomposes VLM action-model capability into geographical/cultural/action-decision dimensions, together they establish the multi-axis-diagnostic wave as a load-bearing evaluation primitive across embodied-agent surfaces.
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — Sibling entry on real-workplace agent benchmarking; both papers surface *real-deployment-regime benchmarking* as a load-bearing primitive — EnterpriseClawBench evaluates agents on real workplace sessions, Robusto-2 evaluates VLM action models on real cross-cultural driving scenarios, together they extend the eval-as-discipline wave from workplace-document reasoning to geographical-OD driving cognition.
- [[naturebench-can-coding-agents-match-the-published-sota-of-nature-family-papers-2606.24530]] — Sibling entry on SOTA-replication benchmarking; both papers surface benchmark-design-disclosure as a load-bearing methodology primitive — NatureBench measures whether coding agents can replicate published Nature-family SOTA, Robusto-2 measures whether VLMs can match human drivers across geographies, together they extend the benchmark-as-deployment-diagnostic wave from coding-replication to AV cross-geography generalization.