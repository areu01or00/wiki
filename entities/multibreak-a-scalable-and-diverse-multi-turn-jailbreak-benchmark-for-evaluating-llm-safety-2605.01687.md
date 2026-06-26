---
title: "MultiBreak: A Scalable and Diverse Multi-Turn Jailbreak Benchmark for Evaluating LLM Safety"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [safety, benchmark, jailbreak, multi-turn, red-teaming, adversarial]
sources: ["https://arxiv.org/abs/2605.01687"]
---

# MultiBreak: A Scalable and Diverse Multi-Turn Jailbreak Benchmark for Evaluating LLM Safety

## Overview
MultiBreak is a scalable and diverse multi-turn jailbreak benchmark of 10,389 adversarial prompts spanning 2,665 distinct harmful intents, designed to evaluate LLM safety under natural conversational attack settings where single-turn benchmarks systematically underestimate vulnerability. The benchmark uses an active-learning pipeline where a generator is iteratively fine-tuned to produce stronger attack candidates guided by uncertainty-based refinement — empirically achieving up to 54.0 and 34.6 higher attack success rate (ASR) than the second-best dataset on DeepSeek-R1-7B and GPT-4.1-mini respectively, and revealing that categories which appear benign under single-turn can exhibit substantially higher adversarial effectiveness in multi-turn scenarios.

## Key Facts
- **Authors**: Song, Jialin; Liu, Xiaodong; Yang, Weiwei; Chen, Wuyang; Feng, Mingqian; Zhu, Xuekai
- **Year**: 2026
- **arXiv**: [2605.01687](https://arxiv.org/abs/2605.01687)
- **Date**: 2026-05-03

## Key Contributions
- **Scale + diversity**: 10,389 multi-turn adversarial prompts spanning 2,665 distinct harmful intents — orders of magnitude larger and more topic-diverse than prior multi-turn benchmarks that were template-bounded.
- **Active-learning attack-pipeline**: A generator is iteratively fine-tuned to produce stronger attack candidates, guided by uncertainty-based refinement — turning benchmark construction into an adversarial-coevolution process rather than static prompt curation.
- **Empirical finding — multi-turn > single-turn**: Up to 54.0 / 34.6 percentage-point ASR gain over second-best dataset on DeepSeek-R1-7B / GPT-4.1-mini respectively. Critically, categories benign under single-turn exhibit substantially higher adversarial effectiveness in multi-turn — exposing a *systematic blind spot* in single-turn safety evaluation.
- **Fine-grained vulnerability surface**: Diverse attack categories uncover fine-grained LLM vulnerabilities that single-turn benchmarks miss — categories-appear-benign is a load-bearing risk indicator for multi-turn deployment.

## Key Insights
- Single-turn safety benchmarks systematically *underestimate* LLM vulnerability because natural conversational settings bypass single-turn guardrails in ways the benchmark surface cannot probe.
- Active-learning-based adversarial prompt generation (rather than static curation) is the structurally correct primitive for safety-benchmark construction because it co-evolves with model defenses — the benchmark stays hard as models harden.
- The categories-benign-under-single-turn result inverts a common assumption that "obvious attack categories = obvious defenses": safety-aligned LLMs can be structurally weaker on benign-looking multi-turn paths than on the canonical harmful-prompt paths single-turn benchmarks cover.

## Related Papers
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]] — Sibling jailbreak-detection work. MultiBreak is the *attack-side benchmark*; What-Intermediate-Layers-Know is the *defense-side detection* primitive. Together they bracket the jailbreak surface between attack-coverage and detection-via-entropy-dynamics.
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — Sibling refusal-mechanism work. Geometry-of-Refusal characterizes refusal as a linear-instability phenomenon in safety-aligned LLMs; MultiBreak probes where that instability manifests under multi-turn attacks.
- [[policyalign-direct-policy-based-safety-alignment-llms-2606.25442]] — Sibling safety-alignment work. PolicyAlign is a *training-time alignment* primitive; MultiBreak is the *evaluation-time coverage* primitive. Together they bracket the LLM-safety surface between alignment-recipe and benchmark-coverage.
- [[safety-paradox-how-enhanced-safety-awareness-leaves-llms-vulnerable-to-posterior-attack-2606.05614]] — Sibling safety-awareness paradox work. Safety-Paradox shows enhanced safety-awareness can leave LLMs *more* vulnerable; MultiBreak shows multi-turn paths expose vulnerabilities single-turn misses — together they surface the *non-monotonic* relationship between safety investment and vulnerability.
- [[emergent-concepts]] — Parent wiki page.