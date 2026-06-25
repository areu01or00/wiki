---
title: "OpenThoughts-Agent: Data Recipes for Agentic Models"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [agentic-llm, data-centric, training-recipes, open-source, llm-training, llm-research, supervised-fine-tuning]
sources: ["https://arxiv.org/abs/2606.24855"]
---

# OpenThoughts-Agent: Data Recipes for Agentic Models

## Overview
This paper introduces OpenThoughts-Agent (OT-Agent), a fully open data curation pipeline for training broadly capable agentic language models, built from more than 100 controlled ablation experiments that systematically isolate the effect of task sources and diversity at each pipeline stage. Fine-tuning Qwen3-32B on the resulting 100K-example dataset yields 44.8% average accuracy across seven agentic benchmarks — a 3.9 percentage-point gain over the strongest existing open-data agentic model (Nemotron-Terminal-32B at 40.9%) — and the training data exhibits strong scaling properties, beating alternative open datasets at every compute-controlled training-set size.

## Key Facts
- **Authors**: Raoof, Negin; Zhuang, Richard; Nezhurina, Marianna; Guha, Etash; Tejaswi, Atula
- **Year**: 2026
- **Date**: 2026-06-23
- **arXiv**: [2606.24855](https://arxiv.org/abs/2606.24855)
- **Subjects**: Artificial Intelligence (cs.AI)

## Key Contributions
- First fully open end-to-end data curation pipeline for training agentic language models — fills the gap left by single-benchmark efforts like SWE-Smith, SERA, and Nemotron-Terminal
- Runs 100+ controlled ablation experiments to systematically isolate the contribution of each pipeline stage, task source, and diversity dimension, yielding concrete recipes rather than ad-hoc recipes
- Assembles a 100K-example training set from the pipeline and fine-tunes Qwen3-32B, achieving 44.8% average accuracy across 7 agentic benchmarks (vs 40.9% for Nemotron-Terminal-32B — a 3.9 pp gain)
- Demonstrates strong scaling properties: the OT-Agent training data outperforms alternative open datasets at every training-set size under compute-controlled comparisons
- Publicly releases training sets, data pipeline, experimental data, and models at openthoughts.ai

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
- [[qwen-agentworld-language-world-models-for-general-agents-2606.24597]] — Same-window paper on agentic foundation-model training via world-model warm-up
- [[beyond-reward-engineering-a-data-recipe-for-long-context-reinforcement-learning-2606.18831]] — Prior data-centric recipe framing for long-context RL (precursor philosophy)