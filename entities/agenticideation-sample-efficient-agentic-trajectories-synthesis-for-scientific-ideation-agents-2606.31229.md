---
title: "Agentic-Ideation: Sample Efficient Agentic Trajectories Synthesis for Scientific Ideation Agents"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agentic-ai, scientific-agents, trajectory-synthesis, llm]
sources: ["https://arxiv.org/abs/2606.31229"]
---

# Agentic-Ideation: Sample Efficient Agentic Trajectories Synthesis for Scientific Ideation Agents

## Overview
Agentic-Ideation is a framework for training LLMs to perform scientific ideation — autonomously generating novel research directions — by synthesizing agentic trajectories at scale. It addresses the key bottleneck in prior approaches: prohibitively expensive data synthesis when applying agentic data methods to scientific reasoning tasks. The framework uses an Oracle-Guided Data Synthesis strategy that leverages a reference idea as guidance to steer a multi-agent system through directed trajectory generation rather than random trial-and-error.

## Key Facts
- **Year**: 2026
- **arXiv**: [2606.31229](https://arxiv.org/abs/2606.31229)

## Key Contributions
- Oracle-Guided Data Synthesis: uses a reference idea as oracle to steer multi-agent trajectory generation, improving sample efficiency by over 10× vs workflow-based baselines
- Automated trajectory synthesis pipeline combining 3 external tools and 3 cognitive tools
- Masking strategy on tool execution results to focus model on decision-making logic
- +11.91% quality improvement over SOTA workflow-based baseline on scientific ideation tasks

## Related Papers
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Context management as load-bearing for LLM agents; Agentic-Ideation's trajectory masking complements context-persistence insights
- [[autodata-an-agentic-data-scientist-to-create-high-quality-synthetic-data-2606.25996]] — Agentic data scientist pipeline; both address synthetic data generation for agentic training
- [[calvert-augmenting-agents-with-calibrated-verifier-telemetry-improves-action-and-learning-in-knowledge-intensive-tasks-2606.21777]] — Verifier-augmented agentic learning; shared focus on trajectory-quality via calibrated feedback
