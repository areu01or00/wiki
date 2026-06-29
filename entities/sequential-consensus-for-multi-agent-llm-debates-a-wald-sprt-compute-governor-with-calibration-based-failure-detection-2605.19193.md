---
title: "Sequential Consensus for Multi-Agent LLM Debates: A Wald-SPRT compute governor with calibration-based failure detection"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [multi-agent, debate, sequential-test, llm, compute-allocation]
sources: ["https://arxiv.org/abs/2605.19193"]
---

# Sequential Consensus for Multi-Agent LLM Debates: A Wald-SPRT compute governor with calibration-based failure detection

## Overview
Adapts Wald's Sequential Probability Ratio Test (SPRT) as a plug-in compute governor for LLM multi-agent debate, replacing fixed-round-count recipes with a numerically-grounded termination rule — after each round an LLM judge emits a [0,1] consensus score, a Wald monitor accumulates log-likelihood evidence, and debate stops when evidence crosses an upper/lower threshold, with a clean negative result on MMLU establishing the calibration diagnostic as the headline empirical contribution.

## Key Facts
- **Authors**: (multi-agent debate sequential testing group)
- **Year**: 2026
- **arXiv**: [2605.19193](https://arxiv.org/abs/2605.19193) (online 2026-05-18)

## Key Contributions
- Formalizes the unit problem in multi-agent debate — fixed round-count recipes over-spend on easy items and under-spend on hard ones — and introduces Wald-SPRT as a numerically-grounded compute governor that allocates rounds adaptively.
- Implements a plug-in LLM-judge consensus score [0,1] emitted after each round, accumulated as log-likelihood evidence in a Wald monitor, with explicit upper/lower threshold crossings that trigger stop or escalate decisions.
- Demonstrates substantial compute savings on GSM8K while maintaining accuracy, and surfaces a clean negative result on MMLU — the calibration diagnostic (evidence trail at termination) emerges as the load-bearing empirical contribution rather than raw accuracy gains.
- Surfaces *Wald-SPRT-as-adaptive-round-allocation-primitive* as a structurally new axis of multi-agent-debate compute governance — distinct from majority-vote or mixture-of-agents because the load-bearing primitive is *sequential-evidence-accumulation-with-explicit-thresholds*, plus *calibration-diagnostic-as-debate-output-primitive* as the load-bearing *interpretation primitive* surfacing the evidence trail (rather than only the final answer) as a first-class output.
- Establishes classical sequential hypothesis testing (Wald 1945) as the structurally correct foundation for compute-governed LLM debate, bridging control theory with multi-agent LLM research.

## Related Papers
- [[emergent-concepts]] — Parent wiki page for emergent-concept discoveries.
- [[the-ringelmann-effect-in-multi-agent-llm-systems-a-scaling-law-for-effective-team-size-2606.02646]] — Sibling Run 78 multi-agent-consensus-probe: Ringelmann Effect provides the *effective-team-size scaling law* primitive that gives cost-vs-accuracy semantics to whatever compute budget Sequential Consensus allocates; Sequential Consensus is a *sequential-test-based compute governor* primitive that terminates multi-agent debate at calibration-driven stopping points. Together they bracket multi-agent-consensus research between *compute-allocation primitives* (Sequential Consensus) and *effective-team-size semantics primitives* (Ringelmann Effect).
- [[coordination-as-an-architectural-layer-for-llm-based-multi-agent-systems-2605.03310]] — Sibling Run 78 multi-agent-consensus-probe: Coordination as an Architectural Layer is a *coordination-failure taxonomy* primitive that maps coordination configurations to predictable failure-mode signatures; Sequential Consensus provides the *compute-governance primitive* that addresses the *failure-mode of fixed-round-allocation* specifically. Together they bracket multi-agent-consensus research between *qualitative-failure-taxonomy primitives* (Coordination Layer) and *compute-governance primitives* (Sequential Consensus).