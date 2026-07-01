---
title: "How Do Language Models Process Ethical Instructions? Deliberation, Consistency, and Other-Recognition Across Four Models"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [alignment, safety, multi-agent, evaluation]
sources: ["https://arxiv.org/abs/2604.00021"]
---

# How Do Language Models Process Ethical Instructions? Deliberation, Consistency, and Other-Recognition Across Four Models

## Overview
This paper investigates how language models internally process ethical instructions—a foundational assumption of alignment safety research that has never been directly verified. Through 600+ multi-agent simulations across four models (Llama 3.3 70B, GPT-4o mini, Qwen3-Next-80B-A3B, Sonnet 4.5) with four instruction formats across two languages, the authors identify four distinct processing types: Output Filter (GPT), Defensive Repetition (Llama), Critical Internalization (Qwen), and Principled Consistency (Sonnet). The central finding is that safety, compliance, and ethical internalization are largely dissociable—models can produce safe outputs without any ethical processing.

## Key Facts
- **arXiv**: [2604.00021](https://arxiv.org/abs/2604.00021)
- **Theme**: alignment safety / ethical instruction processing / multi-agent simulation / compliance vs internalization dissociation

## Key Contributions
- Four distinct ethical processing types identified via Deliberation Depth (DD), Value Consistency Across Dilemmas (VCAD), and Other-Recognition Index (ORI) metrics
- First empirical evidence that safety, compliance, and ethical internalization are largely dissociable in LLMs
- Interaction effect: instruction format only affects internal processing in high-deliberation models; in low-deliberation models format has no effect
- Structural correspondence between model processing types and clinical offender treatment patterns (formal compliance without internal processing as risk signal)
- Model-specific processing patterns (Llama Japanese dissociation not reproduced in other three models)

## Related Papers
- [[be-your-own-red-teamer-safety-alignment-via-self-play-and-reflective-experience-replay-2601.10589]] — Self-play red-teaming for behavioral safety alignment, orthogonal to internal ethical processing framing
- [[est-prm-stress-testing-process-reward-models-before-they-become-load-bearing-2606.00437]] — Process reward model stress-testing, complementary to ethical instruction internalization analysis
- [[ask-dont-judge-binary-questions-for-interpretable-llm-evaluation-and-self-improvement-2606.27226]] — Interpretable eval methodology, orthogonal measurement approach
