---
title: "When Correct Demonstrations Hurt: Rethinking the Role of Exemplars in In-Context Learning"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [in-context-learning, few-shot-prompting, exemplar-selection, prompting]
sources: ["https://arxiv.org/abs/2605.26350"]
---

# When Correct Demonstrations Hurt: Rethinking the Role of Exemplars in In-Context Learning

## Overview
This paper reveals a counterintuitive phenomenon in in-context learning (ICL): correctness of demonstrations does not guarantee exemplar utility, and in some cases correct demonstrations can actually reduce ICL accuracy. The work systematically characterizes when and why correct exemplars fail, identifying three distinct failure modes, and proposes an entropy-based selection criterion that filters demonstrations by model-perceived informativeness rather than ground-truth correctness.

## Key Facts
- **Authors**: Qiu, Chenghao; Peng, Chunli; Yang, Yufeng + 2
- **Year**: 2026
- **arXiv**: [2605.26350](https://arxiv.org/abs/2605.26350)

## Key Contributions
- Identified three failure modes of correct exemplars: distributional misalignment, label ambiguity, and spurious correlation amplification
- Demonstrated that incorrect demonstrations can outperform correct ones under specific conditions (entropy, ambiguity, distributional gap)
- Proposed entropy-based exemplar selection criterion that measures model-perceived informativeness
- Showed that selecting exemplars by model confidence (而非 ground-truth accuracy) improves ICL performance
- Introduced a framework for understanding ICL failure that decouples ground-truth correctness from demonstration utility

## Related Papers
- [[adaptive-evaluation-out-of-band-defenses-against-prompt-injection-in-llm-agents-2606.26479]] — Adaptive evaluation methodology for LLM agents
- [[categorical-prior-lock-in-why-in-context-learning-fails-for-structured-data-2606.11961]] — Categorical prior as failure mode for ICL on structured data
- [[decomposing-how-prompting-steers-behavior-2606.03093]] — How prompting strategies influence LLM behavior
