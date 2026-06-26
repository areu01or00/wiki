---
title: "EndPrompt: Efficient Long-Context Extension via Terminal Anchoring"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [long-context, position-embedding, rope, context-extension, llm, terminal-anchoring, sparse-supervision, llama, efficient-finetuning]
sources: ["https://arxiv.org/abs/2605.14589"]
---

# EndPrompt: Efficient Long-Context Extension via Terminal Anchoring

## Overview
Introduces **EndPrompt**, a method for extending LLM context windows that achieves effective long-context adaptation using only short training sequences. The core insight is that exposing a model to long-range relative positional distances does not require constructing full-length inputs: EndPrompt preserves the original short context as an intact first segment and appends a brief terminal prompt as a second segment, assigning it positional indices *near the target context length*. This two-segment construction introduces both local and long-range relative distances within a short physical sequence while maintaining semantic continuity of the training text — a property absent in chunk-based simulation approaches that split contiguous context. A theoretical analysis grounded in Rotary Position Embedding (RoPE) and the Bernstein inequality shows that position interpolation induces a rigorous smoothness constraint over the attention function, with shared Transformer parameters further suppressing unstable extrapolation to unobserved intermediate distances.

## Key Facts
- **Authors**: Tian, Han; Chen, Luxuan; Chen, Xinran; Kong, Rui; Wang, Fang; Chen, Jiamin; Zhao, Jinman; Li, Yuchen; Zhao, Jiashu; Wang, Shuaiqiang; Xiong, Haoyi; Kong, Linghe; Yin, Dawei
- **Year**: 2026
- **arXiv**: [2605.14589](https://arxiv.org/abs/2605.14589)
- **Submission Date**: 2026-05-14 (cs.CL / cs.LG)

## Key Contributions
- **Surfaces sparse-positional-supervision as the load-bearing primitive** for long-context extension: rather than training on dense full-length sequences, EndPrompt induces long-range relative-position exposure via a two-segment construction (intact short context + brief terminal prompt at target-length positions).
- **Terminal-anchoring as a semantic-continuity-preserving positional-probe primitive** that avoids the chunk-splitting pathology of prior simulation approaches — chunk-based methods sacrifice the contiguous-document semantics needed for stable extrapolation, while EndPrompt's two-segment design retains it.
- **Theoretical grounding** in RoPE + Bernstein inequality: position interpolation induces a smoothness constraint over the attention function, and shared Transformer parameters further suppress unstable extrapolation to unobserved intermediate distances — providing a non-empirical justification for why short-sequence training suffices.
- **Empirical demonstration** on LLaMA-family models extending the context window from 8K to 64K: achieves average RULER score of 76.03 and highest average on LongBench, surpassing LCEG (72.24), LongLoRA (72.95), and full-length fine-tuning (69.23) while requiring substantially less computation.
- **Challenges the prevailing assumption** that dense long-sequence training is necessary for reliable context-window extension — long-context generalization can be induced from sparse positional supervision, inverting the long-context-pretraining-cost assumption.

## Related Papers
- [[query-conditioned-test-time-self-training-quest-per-query-adaptation-2605.13369]] — Run 67 inverse-axis sibling — QueST adapts *parameters at test time* using query-derived supervision, EndPrompt extends *context at training time* using sparse positional supervision — together they bracket the parameter-adaptation surface between *test-time-parameter-adaptation-via-query-supervision* and *training-time-context-extension-via-sparse-positional-supervision* primitives, where QueST exploits *latent signal content of natural-language inputs* and EndPrompt exploits *latent geometric signal of long-range positional distances*.
- [[vericache-turning-lossy-kv-cache-into-lossless-llm-inference-2605.17613]] — Run 59 long-context-deployment sibling — VeriCache targets the *KV-cache-compression-lossless-recovery* dimension of long-context deployment, EndPrompt targets the *context-window-extension* dimension — together they bracket the long-context-deployment surface between compression-with-lossless-recovery and sparse-supervision-based-extension primitives.
- [[efficient-and-trainable-language-model-test-time-scaling-via-local-branch-routing-2606.25354]] — Run 65 sibling test-time-scaling paper — LBR scales inference compute via branch routing at the token level, EndPrompt extends training efficiency via terminal-anchoring positional probes — together they bracket the *token-vs-position* symmetry of test-time-vs-training-time efficiency primitives.
- [[off-the-shelf-llms-as-process-scorers-training-free-prm-alternative-chunk-level-guided-generation-2606.01682]] — Run 67 sibling — Off-the-Shelf-LLMs-as-Process-Scorers exploits *fixed-length chunking* as a length-bias mitigation primitive at inference time, EndPrompt exploits *fixed-length short-context + brief terminal anchor* as a sparse-supervision primitive at training time — together they bracket the *fixed-length-segmentation-as-primitive* surface between inference-time-length-bias-mitigation and training-time-sparse-supervision primitives.
- [[emergent-concepts]] — parent wiki page