---
title: "Dockerless: Environment-Free Program Verifier for Coding Agents"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [coding-agent, verification, reinforcement-learning, tool-use]
sources: ["https://arxiv.org/abs/2606.28436"]
---

# Dockerless: Environment-Free Program Verifier for Coding Agents

## Overview
Dockerless proposes an environment-free agentic patch verifier that evaluates generated code patches without executing them. Instead of matching candidate patches to references, Dockerless judges patch correctness using evidence from code semantics and execution traces. This eliminates the substantial environment setup costs of Docker-based verification, enabling coding agents to verify patches at scale without per-repository environment management overhead.

## Key Facts
- **Year**: 2026
- **arXiv**: [2606.28436](https://arxiv.org/abs/2606.28436)

## Key Contributions
- Environment-free patch verification using semantic evidence rather than execution
- Eliminates Docker image setup overhead for coding agent trajectory selection
- Provides RL rewards without per-repository sandbox infrastructure
- Judging correctness via code patch semantics vs reference matching

## Related Papers
- [[how-much-static-structure-do-code-agents-need-a-study-of-deterministic-anchoring-2606.26979]] — Deterministic anchoring study for coding agents
- [[autopass-evidenceguided-llm-agents-for-compiler-performance-tuning-2606.20373]] — Evidence-guided compiler tuning agent
