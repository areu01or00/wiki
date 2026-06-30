---
title: "AURORA: Asymmetry and Update-Induced Rotation for Robust Hallucination Detection in Large Language Models"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [hallucination, safety, llm]
sources: ["https://arxiv.org/abs/2606.29545"]
---

# AURORA: Asymmetry and Update-Induced Rotation for Robust Hallucination Detection in Large Language Models

## Overview
Large Language Models tend to generate hallucinations — factually incorrect or unfaithful outputs — which is a critical obstacle for high-stakes deployment. This paper introduces AURORA, which exploits asymmetry and update-induced rotation properties in LLM representations to detect hallucinations robustly. The approach uses structural properties of how LLM hidden states rotate during updates to identify unfaithful generations.

## Key Facts
- **Authors**: Unknown
- **Year**: 2026
- **arXiv**: [2606.29545](https://arxiv.org/abs/2606.29545)

## Key Contributions
- Exploits asymmetry and update-induced rotation in LLM hidden states as hallucination signal
- Robust hallucination detection that works across different model families and sizes
- First rotation-based hallucination detection method in the wiki

## Related Papers
- [[truth-as-a-trajectory-what-internal-representations-reveal-llm-reasoning-2603.01326]] — Internal representations as truth signal (related trajectory analysis)
- [[hallucination-in-world-models-is-predictable-and-preventable-2606.27326]] — World model hallucination prevention (complementary approach)
