---
title: "HIPIF: Hierarchical Planning and Information Folding for Long-Horizon LLM Agent Learning"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [agent, planning, long-horizon, hierarchical-reinforcement-learning, llm]
sources: ["https://arxiv.org/abs/2606.10507"]
---

# HIPIF: Hierarchical Planning and Information Folding for Long-Horizon LLM Agent Learning

## Overview
HIPIF addresses the long-context interference problem in multi-turn long-horizon LLM agentic tasks — where continuously growing histories weaken the agent's ability to track global task state. The method trains agents end-to-end around explicit subgoals while folding completed subgoal histories to reduce long-context interference. It combines hierarchical reflection and subgoal-oriented process rewards to guide subgoal generation, transition, and execution.

## Key Facts
- **Authors**: Unknown (from arxiv 2606.10507)
- **Year**: 2026
- **arXiv**: [2606.10507](https://arxiv.org/abs/2606.10507)

## Key Contributions
- Hierarchical Planning + Information Folding: end-to-end training with explicit subgoal decomposition and completed-history folding to combat long-context interference
- Subgoal-oriented process rewards: hierarchical reflection guides subgoal generation, transition, and execution without auxiliary models
- Long-context interference reduction: folding completed subgoal histories maintains agent tracking of global task state
- Three publicly available agentic benchmarks validated; outperforms baselines on long-horizon task completion

## Related Papers
- [[meta-cognitive-memory-policy-optimization-for-long-horizon-llm-agents-2605.30159]] — Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents (related long-horizon memory/planning)
- [[context-recycling-for-long-horizon-llm-inference-2606.26105]] — Context Recycling for Long-Horizon LLM Inference (related context management for long sequences)
- [[foresight-failure-detection-long-horizon-robotic-manipulation-2606.23085]] — Foresight Failure Detection for Long-Horizon Robotic Manipulation (related long-horizon planning failure detection)
