---
title: "Skill Weaving: Efficient LLM Improvement via Modular Skillpacks"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [training, inference-efficiency, modular-architecture, llm]
sources: ["https://arxiv.org/abs/2605.22205"]
---

# Skill Weaving: Efficient LLM Improvement via Modular Skillpacks

## Overview
SkillWeave partitions full capabilities of a general-purpose model into skillpacks — lightweight, domain-specific delta modules — that reorganize and refine the model's internal knowledge. For efficient deployment, SkillWeave integrates SkillZip to compress skillpacks into compact and inference-ready format, enabling strong multi-domain performance with low-latency execution. On multi-task and agentic benchmarks, a 9B SkillWeave model outperforms several baselines and even surpasses a 32B monolithic LLM, while achieving up to 4x speedup.

## Key Facts
- **Authors**: Unknown (arXiv 2605.22205)
- **Year**: 2025
- **arXiv**: [2605.22205](https://arxiv.org/abs/2605.22205)

## Key Contributions
- **Modular skillpack framework**: Partitions full LLM capabilities into lightweight domain-specific delta modules (skillpacks) operating under fixed memory budgets
- **SkillZip compression**: Compresses skillpacks into compact inference-ready format enabling low-latency execution
- **9B outperforms 32B**: Multi-task and agentic benchmark results showing 9B SkillWeave surpasses a 32B monolithic LLM with 4x speedup
- **First-in-wiki**: First modular skillpack framework under fixed memory budgets for LLM specialization

## Related Papers
- [[reason-and-verify-a-framework-for-faithful-retrieval-augmented-generation-2603.10143]] — Sibling discovery from same exploration cycle; CTRL-RAG also addresses context faithfulness while SkillWeave addresses multi-domain specialization
