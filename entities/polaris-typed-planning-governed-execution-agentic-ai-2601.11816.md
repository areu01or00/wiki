---
title: "POLARIS: Typed Planning and Governed Execution for Agentic AI in Back-Office Automation"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [agentic-ai, planning, enterprise-automation]
sources: ["https://arxiv.org/abs/2601.11816"]
---

# POLARIS: Typed Planning and Governed Execution for Agentic AI in Back-Office Automation

## Overview
POLARIS (Policy-Aware LLM Agentic Reasoning for Integrated Systems) is a governed orchestration framework for enterprise back-office automation that treats automation as typed plan synthesis and validated execution over LLM agents. A planner proposes structurally diverse, type-checked DAGs, a rubric-guided reasoning module selects a single compliant plan, and execution is guarded by validator-gated checkpoints.

## Key Facts
- **Authors**: Zahra Moslemi, Keerthi Koneru, Yen-Ting Lee, Sheethal Kumar, Ramesh Radhakrishnan
- **Year**: 2026
- **arXiv**: [2601.11816](https://arxiv.org/abs/2601.11816)

## Key Contributions
- Typed plan synthesis: planner proposes DAGs where nodes carry semantic types (e.g., invoice → approval → payment), enabling structural correctness verification
- Rubric-guided reasoning module selects a single policy-compliant plan from the candidate DAGs
- Validator-gated execution checkpoints ensure each step completes successfully before the next begins
- First "governed orchestration" framework that makes agentic workflows auditable and policy-aligned by construction

## Related Papers
- [[self-regulated-agentic-reasoning-simulative-planning-2605.22138]] — Self-Regulated Simulative Planning: complementary planning decomposition methodology (token-efficient reactive vs structured DAG-based)
- [[crystal-kv-efficient-kv-cache-management-chain-thought-2601.16986]] — Crystal-KV: KV cache efficiency for long-running agentic推理
