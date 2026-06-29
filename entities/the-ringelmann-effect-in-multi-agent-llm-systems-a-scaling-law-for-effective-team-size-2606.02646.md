---
title: "The Ringelmann Effect in Multi-Agent LLM Systems: A Scaling Law for Effective Team Size"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [multi-agent, scaling-law, llm, inference-time, evaluation]
sources: ["https://arxiv.org/abs/2606.02646"]
---

# The Ringelmann Effect in Multi-Agent LLM Systems: A Scaling Law for Effective Team Size

## Overview
Derives a quantitative scaling law for inference-time multi-agent LLM systems, showing that nominal team size N conflates cost with independent evidence; introduces effective team size N_eff and a regime exponent β that classifies any configuration into one of three asymptotic regimes — hard-ceiling, sublinear, or superlinear — bridging classical group-dynamics (Ringelmann's social-loafing effect) with contemporary multi-agent-LLM empirical evaluation.

## Key Facts
- **Authors**: (multi-agent LLM scaling group)
- **Year**: 2026
- **arXiv**: [2606.02646](https://arxiv.org/abs/2606.02646) (online 2026-05-31)

## Key Contributions
- Formalizes the unit problem in inference-time multi-agent LLM scaling — counting nominal agents conflates cost with independent evidence — and introduces effective team size N_eff as the operative quantity.
- Derives a two-parameter scaling law R(N) = N_eff/N = 1 / (1 + c(N-1)N^(-β)) where the regime exponent β classifies any configuration into hard-ceiling at 1/c (β=0), sublinear (0<β<1), or superlinear (β>1).
- Bridges classical Ringelmann-style social-loafing findings to multi-agent LLM systems by recognizing that correlated reasoning failures act like Ringelmann-effect losses on independent evidence.
- Provides a shared unit (effective team size) for inference-time multi-agent scaling analogous to FLOPs for pretraining — enabling principled cost-vs-accuracy comparisons across configurations.
- Surfaces *effective-team-size-as-Ringelmann-corrected-scaling-primitive* as a structurally new axis of multi-agent-LLM evaluation — distinct from majority-vote or mixture-of-agents because the load-bearing primitive is *correlated-failure-loss-via-regime-exponent-classification*.

## Related Papers
- [[emergent-concepts]] — Parent wiki page for emergent-concept discoveries.
- [[sequential-consensus-for-multi-agent-llm-debates-a-wald-sprt-compute-governor-with-calibration-based-failure-detection-2605.19193]] — Sibling Run 78 multi-agent-consensus-probe: Sequential Consensus is a *sequential-test-based compute governor* primitive that terminates multi-agent debate at calibration-driven stopping points; Ringelmann Effect provides the *effective-team-size scaling law* primitive that gives cost-vs-accuracy semantics to whatever compute budget Sequential Consensus allocates. Together they bracket multi-agent-consensus research between *compute-allocation primitives* (Sequential Consensus) and *effective-team-size semantics primitives* (Ringelmann Effect).
- [[coordination-as-an-architectural-layer-for-llm-based-multi-agent-systems-2605.03310]] — Sibling Run 78 multi-agent-consensus-probe: Coordination as an Architectural Layer is a *coordination-failure taxonomy* primitive that maps coordination configurations to predictable failure-mode signatures; Ringelmann Effect provides the *quantitative scaling law* primitive that predicts *how much* effective evidence N agents contribute given correlated-failure losses. Together they bracket multi-agent-consensus research between *qualitative-failure-taxonomy primitives* (Coordination Layer) and *quantitative-scaling-law primitives* (Ringelmann Effect).