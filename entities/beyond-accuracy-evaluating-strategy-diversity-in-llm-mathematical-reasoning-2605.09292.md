---
title: "Beyond Accuracy: Evaluating Strategy Diversity in LLM Mathematical Reasoning"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [evaluation, llm-benchmarking, mathematical-reasoning, strategy-taxonomy]
sources: ["https://arxiv.org/abs/2605.09292"]
---

# Beyond Accuracy: Evaluating Strategy Diversity in LLM Mathematical Reasoning

## Overview
Large language models now achieve high final-answer accuracy on mathematical reasoning benchmarks, but accuracy alone does not capture reasoning flexibility. This paper introduces a strategy-level evaluation framework instantiated on 80 AMC 10/12 and AIME problems with 217 AoPS-derived reference strategy families. Model outputs are annotated for strategy identity, validity, and correctness using dual-AI coding with human adjudication. The key finding: frontier models show a pronounced decoupling between accuracy and strategy diversity — models can achieve high accuracy through narrow repertoires of strategies.

## Key Facts
- **Authors**: Xia Yang, Xuanyi Zhang, Hao Hu, Feng Ji
- **Year**: 2026
- **arXiv**: [2605.09292](https://arxiv.org/abs/2605.09292)

## Key Contributions
- **Strategy taxonomy**: 217 AoPS-derived strategy families covering problem decomposition, analogy, pattern recognition, verification, and backtracking
- **Strategy-identity annotation**: Dual-AI coding with human adjudication to label each model output with its strategy identity
- **Accuracy-strategy decoupling**: Demonstrates that high accuracy does not imply diverse reasoning strategies — models may over-rely on narrow heuristics
- **Strategy validity vs correctness**: A valid strategy (sound reasoning path) can still lead to an incorrect answer; CR-Bench distinguishes these

## Related Papers
- [[the-periodic-table-of-llm-reasoning-a-structured-survey-of-reasoning-paradigms-abstractions-building-blocks-and-open-challenges-2606.11470]] — Structured taxonomy of LLM reasoning paradigms
- [[look-light-think-heavy-what-multimodal-chain-of-thought-reasoning-can-and-cannot-do-2606.22565]] — Chain-of-thought evaluation for multimodal reasoning
- [[verievol-scaling-multimodal-mathematical-reasoning-via-verifiable-evol-instruct-2606.23543]] — Verifiable Evol-Instruct for mathematical reasoning
- [[when-the-chain-of-thought-knows-better-failure-modes-in-multi-turn-reasoning-models-2606.10740]] — Multi-turn reasoning model failure modes
