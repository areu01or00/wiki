---
title: "Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [evaluation, llm-as-judge, interpretability, in-context-learning]
sources: ["https://arxiv.org/abs/2606.28050"]
---

# Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA

## Overview
LLM-as-a-Judge and self-evaluation pipelines implicitly assume that evaluation is easier than generation. This paper tests that assumption in a controlled in-context QA setting where a context passage is the sole information source and each model judges the answer it generated — removing the parametric-knowledge confound of open-domain comparisons. Across four benchmarks (SQuAD 2.0, DROP, HotpotQA, MuSiQue), the authors find significant task-asymmetry: generation and evaluation rely on different internal representations, and mechanistic interpretability analysis reveals that models activate distinct circuits during judging vs. generating. Transferability of the judgment capability to unseen tasks is limited, challenging the assumption that good generators make good judges.

## Key Facts
- **Authors**: Bandyopadhyay, Sambaran
- **Year**: 2026
- **arXiv**: [2606.28050](https://arxiv.org/abs/2606.28050)

## Key Contributions
- First controlled study of task-asymmetry in LLM-as-Judge: generation and judgment activate different internal representations
- In-context QA setting that isolates evaluation capability from parametric knowledge
- Mechanistic interpretability analysis showing distinct circuits for judging vs. generating
- Empirical finding that judgment capability transfers poorly to unseen tasks — challenging the universality assumption of LLM-as-Judge
- Four-benchmark evaluation (SQuAD 2.0, DROP, HotpotQA, MuSiQue)

## Related Papers
- [[ask-dont-judge-binary-questions-for-interpretable-llm-evaluation-and-self-improvement-2606.27226]] — Binary question framing for interpretable LLM evaluation (alternative evaluation paradigm)
- [[benchmarking-llm-as-a-judge-for-long-form-output-evaluation-2606.01629]] — LLM-as-Judge benchmarking for long-form output evaluation
- [[aura-adaptive-uncertainty-aware-refinement-llm-judge-2606.19714]] — Adaptive uncertainty-aware refinement for LLM judges
