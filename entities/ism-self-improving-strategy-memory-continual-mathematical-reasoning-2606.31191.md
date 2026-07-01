---
title: "ISM: Self-Improving Strategy Memory for Continual Mathematical Reasoning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [continual-learning, memory-augmented-llm, mathematical-reasoning, strategy-memory]
sources: ["https://arxiv.org/abs/2606.31191"]
---

# ISM: Self-Improving Strategy Memory for Continual Mathematical Reasoning

## Overview
ISM (Intelligent Schema Memory) is a self-evolving memory-augmented system that improves mathematical reasoning for a frozen LLM under continual learning settings. It uses a hybrid extractor combining rule-based keyword matching with learned surface-form pattern recognition to identify and store high-value strategy schemas, then retrieves relevant schemas at inference time to guide reasoning without requiring gradient updates to the base model.

## Key Facts
- **Authors**: Dixit, Prakhar; Oates, Tim
- **Year**: 2026
- **arXiv**: [2606.31191](https://arxiv.org/abs/2606.31191)

## Key Contributions
- Self-evolving external memory for frozen LLMs — strategy schemas are extracted, stored, and retrieved without any model weight updates
- Hybrid extractor: rule-based branch (keyword matchers) + learned surface-form pattern branch for schema identification
- Episodic hard resets prevent catastrophic forgetting of previously learned strategies
- Application to continual mathematical reasoning, demonstrating durability of accumulated strategy knowledge across multiple learning episodes

## Related Papers
- [[agent-dice-geometric-consensus-agent-continual-learning-2601.03641]] — Agent DiCE for geometric consensus in continual learning; ISM shares the memory-augmented frozen-LLM approach but targets mathematical strategy memory instead
- [[group-evolving-agents-open-ended-self-improvement-via-experience-sharing-2602.04837]] — Group-evolving agents with experience sharing; ISM's self-evolving memory schema is conceptually related but isolated to a single model's strategy accumulation
- [[attribution-guided-continual-learning-for-llms-2605.05285]] — Attribution-guided continual learning; both address catastrophic forgetting in LLMs via different mechanisms (attribution vs episodic hard resets)
