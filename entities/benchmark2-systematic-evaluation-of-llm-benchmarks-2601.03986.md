---
title: "Benchmark²: Systematic Evaluation of LLM Benchmarks"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [evaluation, benchmarking, meta-evaluation, llm]
sources: ["https://arxiv.org/abs/2601.03986"]
---

# Benchmark²: Systematic Evaluation of LLM Benchmarks

## Overview
Benchmark² proposes a meta-evaluation framework for LLM benchmarks — evaluating the evaluators themselves. It introduces three complementary metrics: Cross-Benchmark Ranking Consistency (do benchmark rankings align with peer benchmarks?), Discriminability Score (can the benchmark differentiate between model families?), and Capability Alignment Deviation (are there instances where stronger models fail but weaker ones succeed?). Analysis across 15 benchmarks reveals significant quality variation among existing LLM evaluation frameworks.

## Key Facts
- **Authors**: Qi Qian, Chengsong Huang, Jingwen Xu, Changze Lv, Muling Wu, Wenhao Liu, Xiaohua Wang, Zhenghua Wang, Zisu Huang, Muzhao Tian, Jianhan Xu, Kun Hu, He-Da Wang, Yao Hu, Xuanjing Huang, Xiaoqing Wang et al.
- **Year**: 2026
- **arXiv**: [2601.03986](https://arxiv.org/abs/2601.03986)

## Key Contributions
- First meta-evaluation framework for LLM benchmark quality assessment
- Three complementary metrics: Cross-Benchmark Ranking Consistency, Discriminability Score, Capability Alignment Deviation
- Reveals significant quality variation among 15 existing benchmarks
- Demonstrates that selective benchmark construction with these metrics achieves comparable evaluation with reduced test sets
- First paper in the wiki to evaluate the evaluators (meta-evaluation of benchmark design)

## Related Papers
- [[counsel-a-meta-evaluation-dataset-for-agentic-tasks-2606.21627]] — Meta-evaluation dataset for agentic tasks; orthogonal axis (Counsel focuses on agentic trajectory meta-evaluation, Benchmark² focuses on benchmark-to-benchmark consistency and discriminability across model families)
- [[tau-rec-a-verifiable-benchmark-for-agentic-recommender-systems-2606.10156]] — Domain-specific evaluation benchmark; orthogonal axis (Tau-Rec evaluates recommender systems, Benchmark² evaluates benchmark methodology across domains)
- [[persuasivetom-benchmark-evaluating-machine-theory-mind-in-persuasive-dialogues-2502.21017]] — Social-reasoning benchmark; orthogonal axis (PersuasiveToM evaluates social reasoning, Benchmark² evaluates benchmark design quality)
