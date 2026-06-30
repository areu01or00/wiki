---
title: "Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [evaluation, llm-as-a-judge, benchmarking, long-form-generation]
sources: ["https://arxiv.org/abs/2606.01629"]
---

# Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation

## Overview
As LLMs are increasingly deployed for long-form generation tasks, reliably evaluating their outputs has become critical. LLM-as-a-judge offers a scalable alternative to human evaluation, but its reliability for long-form outputs has been underexamined. This paper systematically benchmarks LLM-as-a-judge for long-form evaluation, revealing systematic biases and failure modes that differ qualitatively from short-form evaluation.

## Key Facts
- **Authors**: Junjie Chen, Yuxi Dong, Haitao Li, Weihang Su, Yujia Zhou, Min Zhang, Yiqun Liu, Qinyao Ai
- **Year**: 2026
- **arXiv**: [2606.01629](https://arxiv.org/abs/2606.01629)

## Key Contributions
- **First systematic meta-evaluation of LLM-as-a-judge for long-form**: Addresses a critical gap — existing meta-evaluation benchmarks focus on short-form outputs; this work reveals that LLM judges perform qualitatively worse on long-form tasks
- **Systematic bias discovery**: Length bias (favoring longer outputs), position bias (sensitive to answer order), and self-preference bias (favoring outputs similar to the judge's own writing style) are all amplified in long-form settings
- **Evaluation benchmark dataset**: Introduces a benchmark with controlled pairs of long-form outputs designed to isolate each bias type
- **Remediation strategies**: Proposes calibration techniques (e.g., forced-pairwise comparison, anchor-based scoring) that significantly reduce bias in long-form LLM-judge evaluation

## Related Papers
- [[aura-adaptive-uncertainty-aware-refinement-llm-judge-2606.19714]] — AURA: adaptive uncertainty-aware refinement for LLM-as-judge; addresses judge uncertainty in a complementary way — this paper focuses on long-form specific biases while AURA addresses uncertainty quantification across output lengths
- [[when-gradients-collide-failure-modes-of-multi-objective-prompt-optimization-for-llm-judges-2605.26046]] — When Gradients Collide: studies failure modes of multi-objective prompt optimization for LLM judges; complements this work by examining judge prompt optimization failure modes
