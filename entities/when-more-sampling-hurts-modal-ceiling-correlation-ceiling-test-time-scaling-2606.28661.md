---
title: "When More Sampling Hurts: The Modal Ceiling and Correlation Ceiling of Test-Time Scaling"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, test-time-compute, reasoning, llm]
sources: ["https://arxiv.org/abs/2606.28661"]
---

# When More Sampling Hurts: The Modal Ceiling and Correlation Ceiling of Test-Time Scaling

## Overview
The paper identifies a fundamental bottleneck in test-time compute scaling for reasoning LLMs: beyond a certain number of samples, extra sampling degrades answer selection quality while adding cost. The key insight is the "identifiability gap" — coverage (fraction of problems with at least one correct try) keeps climbing with more samples, but selection (picking the right answer) stalls. This gap is the answer a model can produce but not pick. The paper quantifies this as the "effective number of samples" — a single observable number that any sampling run already reveals.

## Key Facts
- **arXiv**: [2606.28661](https://arxiv.org/abs/2606.28661)
- **Year**: 2026
- **Theme**: test-time compute scaling / inference efficiency / reasoning

## Key Contributions
- **Modal ceiling**: The vote settles within a few dozen draws for picking an answer — beyond that, extra samples add cost but no selection quality gain
- **Correlation ceiling**: For scoring a benchmark, the cutoff is even sooner — correlation between sampled answers and true answers plateaus early
- **Identifiability gap**: The gap between climbing coverage and stalled selection; the answer a model can produce but not pick
- **Effective number of samples (ENS)**: A single number derivable from any sampling run that reveals the modal ceiling — the bottleneck is recognizing a right answer, not generating one
- **Key implication**: More sampling effort should go toward making correct answers more recognizable/identifiable, not toward generating more candidates

## Related Papers
- [[when-more-thinking-hurts-overthinking-in-llm-test-time-compute-2604.10739]] — Overthinking in LLM test-time compute (prior art on test-time compute inefficiency)
- [[when-does-delegation-beat-majority-a-delegation-based-aggregator-for-multi-sample-llm-inference-2606.08098]] — Multi-sample inference aggregation
- [[itcr-inference-time-conformal-reasoning-with-valid-factuality-control-for-llms-2606.08831]] — Inference-time reasoning control
