---
title: "MinGram: A Minimalist Unigram Tokenizer with High Compression and Competitive Morphological Fidelity"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [tokenizer, unigram, bpe, compression, morphology, multilingual, llm]
sources: ["https://arxiv.org/abs/2606.27019"]
---

# MinGram: A Minimalist Unigram Tokenizer with High Compression and Competitive Morphological Fidelity

## Overview
First paper in the wiki to introduce a **minimalist Unigram tokenizer** that keeps Unigram's elegant token-list representation but reduces training to a BPE-derived seed vocabulary + Hard-EM on a minimum-token path + a single flat score-pruning step. MinGram drops the suffix array, forward-backward pass, and iterative prune loop — leaving a procedure that requires little beyond tokenizer inference itself. Across six languages, MinGram compresses better than both BPE and standard Unigram, and a compression-oriented variant matches the strongest token-count compressors while retaining substantially higher morphological alignment.

## Key Facts
- **Authors**: MinGram authors (2026)
- **Year**: 2026
- **arXiv**: [2606.27019](https://arxiv.org/abs/2606.27019)
- **Online Date**: 2026-06-25
- **Domain**: tokenizer-design × morphological-alignment × compression × LLM-pretraining

## Key Contributions
- **BPE-seeded Unigram**: starts from a BPE-derived seed vocabulary and runs Hard-EM on a minimum-token path — collapsing the Unigram training pipeline from suffix-array + forward-backward + iterative-prune into a single flat score-pruning step
- **Token-count as primary objective, Unigram score as tiebreak**: makes MinGram compress better than both BPE and standard Unigram across six languages while retaining the morphological alignment that probabilistic tokenizers achieve
- **Controlled downstream comparison**: in matched language-model training runs, Unigram-family tokenizers (with MinGram among the best) consistently beat BPE in bits-per-byte — establishing the probabilistic-objective advantage as a downstream property, not just a training-time artifact
- **Compression-oriented variant**: matches the strongest token-count compressors while retaining substantially higher morphological alignment — splitting the long-standing trade-off between BPE-style compression and Unigram-style alignment
- **Tokenizer-design primitive**: provides a structural alternative to standard Unigram (heavy training), standard BPE (poor morphology), and hybrid approaches — establishing "training-pipeline simplicity + Unigram representation" as a competitive primitive
- **Cross-discipline primitive**: bridges tokenizer-engineering × empirical-morphology × LLM-pretraining-evaluation — surfaces the **compression-vs-morphology trade-off** as an empirically resolvable axis rather than a fixed constraint

## Related Papers
- [[taro-token-level-adaptive-routing-llm-test-time-alignment-2603.18411]] — Token-level alignment primitive for test-time routing; complements MinGram's token-list construction at the post-tokenization level
- [[beyond-tokens-concept-level-training-objectives-for-llms-2601.11791]] — Concept-level training objective; complements MinGram by treating the post-tokenization token stream as a learning target rather than a fixed substrate
- [[nitp-next-implicit-token-prediction-for-llm-pre-training-2605.24956]] — Next-implicit-token prediction; complements MinGram's token-list representation by replacing explicit tokens with implicit distributed prediction
- [[do-thinking-tokens-help-with-safety-2606.25013]] — Thinking-tokens-as-safety-marker; complements MinGram by showing token-level semantic role assignment as a downstream primitive
- [[beyond-multi-token-prediction-pretraining-llms-with-future-summaries-2510.14751]] — Future-summaries-as-multi-token-prediction-target; complements MinGram's compression objective by extending token-coverage past the immediate next-token surface