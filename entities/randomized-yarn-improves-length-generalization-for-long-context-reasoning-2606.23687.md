---
title: "Randomized YaRN Improves Length Generalization for Long-Context Reasoning"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [long-context, length-generalization, positional-encoding, yarn, llm]
sources: ["https://arxiv.org/abs/2606.23687"]
---

# Randomized YaRN Improves Length Generalization for Long-Context Reasoning

## Overview
Randomized YaRN is a training method that improves length generalization of LLMs by combining YaRN-style positional extrapolation with randomized positional encoding parameters during continued training. The technique recovers reasoning performance at context lengths (16K-128K) where standard YaRN-extended models degrade, without requiring task-specific fine-tuning.

## Key Facts
- **Authors**: Mehta, Manas; Yin, Fangcong; Durrett, Greg
- **Year**: 2026
- **arXiv**: [2606.23687](https://arxiv.org/abs/2606.23687)
- **Date**: 2026/06/22

## Key Contributions
- Identifies a length-generalization gap in YaRN-extended LLMs: standard YaRN fine-tuning recovers perplexity at extension lengths but reasoning performance degrades sharply at lengths beyond the fine-tuning window.
- Proposes injecting randomization into the positional-encoding parameters during continued training, encouraging the model to be robust to encoding perturbations rather than overfitting to a single extension scheme.
- Demonstrates consistent reasoning improvements across 16K-128K context windows, outperforming standard fine-tuning on long-context reasoning evaluations.

## Related Papers
- [[beyond-reward-engineering-a-data-recipe-for-long-context-reinforcement-learning-2606.18831]] — sibling data-recipe surface for long-context RL
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — sibling long-context embedding surface for retrieval/agentic memory
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — sibling positional-encoding-aware KV-cache compression
- [[connect-the-dots-training-llms-for-long-lifecycle-agents-with-cross-domain-generalization-via-reinforcement-learning-2606.20002]] — sibling generalization-via-RL surface for long-lifecycle agents
