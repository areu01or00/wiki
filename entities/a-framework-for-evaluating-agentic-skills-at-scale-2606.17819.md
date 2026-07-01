---
title: "A Framework for Evaluating Agentic Skills at Scale"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agent, benchmark, skill-reuse, evaluation]
sources: ["https://arxiv.org/abs/2606.17819"]
---

# A Framework for Evaluating Agentic Skills at Scale

## Overview
Agent skills — structured, reusable knowledge artifacts that augment LLM agent capabilities — have been rapidly adopted in industry, yet their cross-domain impact remains under-studied and no reusable methodology exists for evaluating an individual skill. This work presents an evaluation framework where a skill author constructs realistic tasks to rigorously assess skill utility, then applies it at scale to 500 real-world skills generating 1,000 tasks, evaluating 19 agent-model configurations. Results show substantial performance variation across models in how closely they adhere to skill instructions, and that access to a skill significantly changes model behavior compared to no-skill setup.

## Key Facts
- **Authors**: Shaposhnikov, Maksim; Fortuin, Nicolas; Stipcich, Simon + 3
- **Year**: 2026
- **arXiv**: [2606.17819](https://arxiv.org/abs/2606.17819)

## Key Contributions
- First reusable methodology for evaluating individual agent skills independently of specific agent backbones
- Applied at scale: 500 real-world skills, 1,000 generated tasks, 19 agent-model configurations
- Reveals that model performance gains from skills vary substantially — encoding opinionated workflows matters critically
- Opensourced evaluation dataset for future skill evaluation research

## Related Papers
- [[agents-last-exam-2606.05405]] — LLM agent benchmark evaluation
- [[counsel-a-meta-evaluation-dataset-for-agentic-tasks-2606.21627]] — Meta-evaluation dataset for agentic tasks
