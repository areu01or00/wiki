---
title: "Multi-Turn Reflective Masking Elicits Reasoning in Mask Diffusion Models"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [mask-diffusion, reasoning, chain-of-thought, test-time-scaling, language-models]
sources: ["https://arxiv.org/abs/2606.16700"]
---

# Multi-Turn Reflective Masking Elicits Reasoning in Mask Diffusion Models

## Overview
Zhang, Bian, Qi, Yao, Huang, and Zhou propose Reflective Masking (RM), a lightweight post-training method that elicits native multi-turn reasoning in Mask Diffusion Models (MDMs) by iteratively revisiting and revising prior outputs through selective masking — exploiting the masking mechanism's ability to perform explicit local edits on previous outputs (unlike autoregressive chain-of-thought, which fully regenerates even when only a local edit is needed) — and introduce History Reference, a parameter-free mechanism that leverages intermediate denoising states to inform revisions.

## Key Facts
- **Authors**: Zhang, Yanming; Bian, Yihan; Qi, Jingyuan; Yao, Yuguang; Huang, Lifu; Zhou, Tianyi
- **Year**: 2026
- **arXiv**: [2606.16700](https://arxiv.org/abs/2606.16700)
- **Date**: 2026-06-15

## Key Contributions
- Identifies a structural asymmetry between AR reasoning and MDM reasoning: AR chain-of-thought refinement always relies on fully sequential regeneration, while MDMs' masking mechanism natively supports explicit local edits on prior outputs — yet existing MDMs do not support multi-turn masking/denoising and so leave this native reasoning advantage latent.
- Designs Reflective Masking (RM), a lightweight post-training method that unlocks multi-turn masking/denoising on existing MDMs without architectural changes — yielding a native test-time scaling primitive where an MDM iteratively revisits and revises prior outputs based on evolving context.
- Introduces History Reference, a parameter-free mechanism that leverages intermediate denoising states during revision to incorporate insights from previous turns (the analog of AR reasoning's prior-token context) — making MDM reflective reasoning competitive with AR reasoning without requiring parameter-side conditioning.
- Validates RM across text generation, Sudoku, and image editing — consistent gains over standard masking baselines and strong cross-modality generality — positioning RM as a fundamental primitive for reasoning on MDMs that complements (rather than replaces) AR chain-of-thought.

## Related Papers
- [[emergent-concepts]] — Parent meta-page that aggregates this and other emergent-concept discoveries from the wiki-explore-agent pipeline.
- [[improved-large-language-diffusion-models-2606.25331]] — Sibling large-language-diffusion-models work; together they frame mask-diffusion language modeling as a viable non-AR reasoning substrate whose native masking mechanism is the load-bearing primitive for selective local refinement.
- [[the-periodic-table-of-llm-reasoning-a-structured-survey-of-reasoning-paradigms-abstractions-building-blocks-and-open-challenges-2606.11470]] — Sibling reasoning-paradigm survey; Reflective Masking is a concrete reasoning primitive that the survey's taxonomy would now need to accommodate as a non-AR, mask-edit-native alternative to chain-of-thought.
- [[the-hitchhikers-guide-to-agentic-ai-from-foundations-to-systems-2606.24937]] — Sibling agentic-AI survey; test-time scaling primitives like RM are the kind of inference-time capability that agentic systems can compose into multi-step decision-making, complementing the prompt/agent-orchestration surface covered in the survey.