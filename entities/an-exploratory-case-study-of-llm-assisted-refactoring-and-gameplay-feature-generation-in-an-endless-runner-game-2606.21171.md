---
title: "An Exploratory Case Study of LLM-Assisted Refactoring and Gameplay Feature Generation in an Endless Runner Game"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [llm-coding, software-engineering, case-study, refactoring, game-development, gpt-4]
sources: ["https://arxiv.org/abs/2606.21171"]
---

# An Exploratory Case Study of LLM-Assisted Refactoring and Gameplay Feature Generation in an Endless Runner Game

## Overview
An exploratory empirical case study of GPT-4o on six selected development tasks (three localized refactoring tasks and three gameplay feature generation tasks) within a custom Python/Pygame endless runner, evaluated through software metrics, unit tests, and manual gameplay assessments. Wunderlich, Jan; Kleffmann, Markus; Lempert, Sebastian find that all three refactoring tasks were completed successfully in functional terms, whereas only one of three gameplay feature generation tasks resulted in a correctly integrated feature, suggesting that GPT-4o handled localized transformations more reliably than tasks requiring new gameplay interactions across multiple existing systems — a result they frame as indicative rather than generalizable given the single-case exploratory design.

## Key Facts
- **Authors**: Wunderlich, Jan; Kleffmann, Markus; Lempert, Sebastian
- **Year**: 2026
- **arXiv**: [2606.21171](https://arxiv.org/abs/2606.21171)
- **Subjects**: cs.SE
- **Date**: 2026-06-19
- **Model**: GPT-4o
- **Setting**: custom Python/Pygame endless runner game (production-style existing codebase)

## Key Contributions
- Provides a transparent case-based account of LLM-assisted refactoring versus gameplay feature generation in an existing game software system, isolating the local-transformation vs cross-system-integration axis that aggregate evaluations conflate
- Documents an asymmetric capability profile: 3/3 refactoring tasks successful in functional terms, but only 1/3 gameplay feature generation tasks successfully integrated — surfacing cross-system integration as a load-bearing bottleneck
- Triangulates evaluation across software metrics, unit tests, and manual gameplay assessment, contrasting quantitative functional success with qualitative gameplay-behavior evaluation
- Frames the result as indicative rather than generalizable — the design is a single-case exploratory study, and the contribution is the granular task-level breakdown rather than a category-level claim about LLM-coding capability
- Highlights the gap between localized transformations (where LLM assistance works reliably) and multi-system feature generation (where integration with existing game systems remains a binding constraint) — a distinction that benchmark-style evaluations of code LLMs typically do not surface

## Related Papers
- [[beyond-nl2code-a-structured-survey-of-multimodal-code-intelligence-2606.15932]] — Sibling multimodal-code-intelligence survey
- [[naturebench-can-coding-agents-match-the-published-sota-of-nature-family-papers-2606.24530]] — Coding-agent SOTA-replication benchmark
- [[cli-universe-towards-verifiable-task-synthesis-engine-for-terminal-agents-2606.22883]] — Verifiable-task synthesis for terminal-coding agents
