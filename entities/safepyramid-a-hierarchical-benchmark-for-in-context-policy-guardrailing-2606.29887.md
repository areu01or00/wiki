---
title: "SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [safety, benchmark, guardrails, llm, policy]
sources: ["https://arxiv.org/abs/2606.29887"]
---

# SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing

## Overview
SafePyramid evaluates LLMs and guardrails on in-context policy guardrailing — predicting safety violations based on application-specific policies provided in context rather than predefined risk taxonomies. The benchmark covers 1,000 multi-turn conversations across 10 domains with 3,000 application-specific policies and 61,699 natural-language rules organized across three difficulty levels: L0 (individual-rule understanding), L1 (reasoning over rule dependencies), and L2 (adapting to novel policy frameworks).

## Key Facts
- **Authors**: Jiacheng Zhang, Haoyu He, Sen Zhang, Shen Wang, Xiaolei Xu, Yuhao Sun, Meng Shen, Feng Liu
- **Year**: 2026
- **arXiv**: [2606.29887](https://arxiv.org/abs/2606.29887)

## Key Contributions
- First systematic benchmark for in-context policy guardrailing — guards that predict violations from policy specs in context, not predefined taxonomies
- Three-tier difficulty structure (L0/L1/L2) probing individual-rule understanding, rule-dependency reasoning, and novel-framework adaptation
- 61,699 distinct natural-language rules across 10 domains covering diverse real-world safety policies
- Finds GPT-5.5 achieves only 54.0%, 35.3%, and 12.9% exact full-violation accuracy at L0/L1/L2 respectively — significant room for improvement
- Evaluates 10 frontier LLMs and 5 policy-configurable guardrails

## Related Papers
- [[capable-but-careless-do-computer-use-agents-follow-contextual-integrity-2606.23189]] — Computer-use agents and contextual integrity norms
- [[benchmarking-open-weight-foundation-models-for-global-ai-technical-governance-2606.26099]] — Open-weight model governance and safety benchmarking
