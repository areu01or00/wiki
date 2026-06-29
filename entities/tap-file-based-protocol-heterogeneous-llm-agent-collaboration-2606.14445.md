---
title: "tap: A File-Based Protocol for Heterogeneous LLM Agent Collaboration"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [multi-agent, protocol, llm, collaboration, heterogeneity]
sources: ["https://arxiv.org/abs/2606.14445"]
---

# tap: A File-Based Protocol for Heterogeneous LLM Agent Collaboration

## Overview
tap (Tool-hAndshake Protocol) is a file-based collaboration protocol enabling LLM agents from different vendors (e.g., Claude/Anthropic and Codex/OpenAI) to collaborate on shared codebases without shared memory or a common runtime. The protocol solves the fundamental problem that existing multi-agent systems assume homogeneous execution environments, preventing cross-vendor collaboration.

## Key Facts
- **Authors**: Minseo Kim et al.
- **Year**: 2026
- **arXiv**: [2606.14445](https://arxiv.org/abs/2606.14445)
- **Submitted**: 2026-06-12
- **Subjects**: Software Engineering (cs.SE); Artificial Intelligence (cs.AI); Human-Computer Interaction (cs.HC)
- **Venue**: KCC 2026

## Key Contributions
- **File-first protocol design**: Markdown files with metadata serve as original messages, preserving the collaboration history durably on disk
- **Two-tier communication**: Tier 1 = file inspection path (file communication) + Tier 2 = real-time notification paths (for Claude and Codex), enabling both synchronous and asynchronous collaboration
- **Git worktree isolation**: Separate git worktrees isolate each agent's work, enabling parallel development without interference
- **Heterogeneous model pair advantage**: 69.8% of reviews from heterogeneous model pairs (Claude+Codex) recorded at least one defect, vs 53.1% for homogeneous pairs — heterogeneous collaboration broadens review perspectives
- **Self-applied operation**: 27-day, 37-generation self-applied operation developing and reviewing tap itself, yielding 209 pull requests and 717 operational artifacts

## Related Papers
- [[mesh-memory-protocol-semantic-infrastructure-multi-agent-llm-2604.19540]] — Both protocols address cross-session agent collaboration; tap focuses on heterogeneous cross-vendor file-based communication while Mesh Memory Protocol focuses on semantic infrastructure for cross-session cognitive state sharing
- [[hallucination-as-context-drift-synchronization-protocols-for-multi-agent-llm-systems-2606.21666]] — Both address multi-agent synchronization failures; tap provides a concrete file-based protocol while Context Drift characterizes the failure mode
