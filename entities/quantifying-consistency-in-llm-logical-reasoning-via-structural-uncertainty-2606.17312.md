---
title: "Quantifying Consistency in LLM Logical Reasoning via Structural Uncertainty"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, consistency, uncertainty, llm, evaluation]
sources: ["https://arxiv.org/abs/2606.17312"]
---

# Quantifying Consistency in LLM Logical Reasoning via Structural Uncertainty

## Overview
Large language models can arrive at the same answer through reasoning paths that are unstable, contradictory, or difficult to rank consistently — a failure mode especially prevalent in multi-step deductive reasoning. This paper proposes structural uncertainty as a consistency-aware framework derived from the stability of self-preference-induced rankings over sampled reasoning solutions. The authors report that combining structural signals with answer dispersion improves identification of unreliable instances on logical and mathematical reasoning tasks.

## Key Facts
- **Authors**: B. Chaudhury, M.F. Wang, H. Hayley Park, R. Ghosh, S. Hong, J.O. Woo
- **Year**: 2026
- **arXiv**: [2606.17312](https://arxiv.org/abs/2606.17312)
- **Published**: ICLR 2026 Workshop on Logical Reasoning of LLMs

## Key Contributions
- Introduces **structural uncertainty** as a consistency-aware reasoning evaluation framework for LLM logical reasoning — measures stability of self-preference rankings over sampled reasoning solutions rather than just answer frequency
- Demonstrates that reasoning paths can be unstable, contradictory, or difficult to rank consistently even when the final answer is stable — a distinct failure mode from accuracy-based evaluation
- Proposes combining structural signals (reasoning-path geometry, self-preference ranking stability) with answer dispersion (majority-vote consistency) to improve identification of unreliable reasoning instances
- Bridges the gap between consistency-based evaluation (majority voting, self-consistency) and uncertainty quantification (token-level probability distributions) by introducing structure-level uncertainty signals
- **First structural-uncertainty-as-reasoning-consistency-measure in the wiki** — orthogonal to majority-voting aggregation papers and to single-answer accuracy benchmarks

## Related Papers
- [[sequential-consensus-for-multi-agent-llm-debates-a-wald-sprt-compute-governor-with-calibration-based-failure-detection-2605.19193]] — sibling consensus work; Sequential Consensus studies calibration-based failure detection in multi-agent debates, while this paper studies structural uncertainty within individual model reasoning traces — together they bracket the consensus/consistency surface between multi-agent aggregation (Sequential Consensus) and intra-model reasoning stability (this paper)
- [[when-does-combining-language-models-help-a-co-failure-ceiling-on-routing-voting-and-mixture-of-agents-across-67-frontier-models-2606.27288]] — parent combination/mixture paper; this paper extends the Co-Failure Ceiling analysis from model combination to reasoning-path consistency within a single model
