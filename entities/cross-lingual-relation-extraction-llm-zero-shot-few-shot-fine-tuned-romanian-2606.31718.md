---
title: "Cross-lingual Relation Extraction with Large Language Models: Zero-Shot, Few-Shot, and Fine-Tuned Evaluation on Romanian"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [cross-lingual, relation-extraction, fine-tuning, llm, benchmark]
sources: ["https://arxiv.org/abs/2606.31718"]
---

# Cross-lingual Relation Extraction with Large Language Models: Zero-Shot, Few-Shot, and Fine-Tuned Evaluation on Romanian

## Overview
The paper investigates cross-lingual relation extraction (RE) for Romanian, a low-resource language, using LLMs. It translates the SemEval-2010 Task 8 benchmark to Romanian via an LLM-based pipeline and evaluates Gemma 4 31B under zero-shot, few-shot, and QLoRA fine-tuned configurations against encoder baselines (XLM-RoBERTa, Romanian BERT, RoBERTa). Key findings: Romanian incurs a 3-5pp drop vs English in prompt-only settings; QLoRA fine-tuning improves macro F1 by 22+pp and reduces cross-lingual gap from 3.3pp to 1.4pp; small encoders (125M Romanian BERT) match a 31B Gemma on Romanian RE.

## Key Facts
- **Authors**: Vasile, Dragos-Mitrut; Apostol, Elena-Simona; Toma, Stefan-Adrian + 2
- **Year**: 2026
- **arXiv**: [2606.31718](https://arxiv.org/abs/2606.31718)
- **Online Date**: 2026-06-30

## Key Contributions
- First comprehensive cross-lingual RE study for Romanian using LLMs
- LLM-based translation pipeline for creating low-resource RE datasets
- Demonstrates QLoRA fine-tuning closes the cross-lingual gap (3.3pp → 1.4pp) for Romanian RE
- Challenges the case for 31B models on single-task low-resource RE — 125M Romanian BERT matches 31B Gemma
- Evaluates 4 encoder baselines (125M–560M) against LLM under identical conditions

## Related Papers
- [[are-multilingual-models-actually-improving-isolating-true-cross-lingual-transfer-2606.21954]] — Cross-lingual transfer isolation study (prior art on multilingual evaluation)
- [[cross-lingual-exploration-for-parametric-knowledge-2606.24579]] — Cross-lingual exploration for parametric knowledge
