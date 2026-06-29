---
title: "Mesh Memory Protocol: Semantic Infrastructure for Multi-Agent LLM Systems"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [multi-agent, memory, protocol, llm, semantic-infrastructure]
sources: ["https://arxiv.org/abs/2604.19540"]
---

# Mesh Memory Protocol: Semantic Infrastructure for Multi-Agent LLM Systems

## Overview
The Mesh Memory Protocol (MMP) specifies the missing "semantic infrastructure" layer for cross-session agent-to-agent cognitive collaboration — where LLM agents share, evaluate, and combine each other's cognitive state in real time across sessions spanning days or weeks. MMP addresses three protocol-level problems: field-level message acceptance (P1), source-traceable claims (P2), and session-survivable memory relevance (P3).

## Key Facts
- **Authors**: Hongwei Xu et al.
- **Year**: 2026
- **arXiv**: [2604.19540](https://arxiv.org/abs/2604.19540)
- **Submitted**: 2026-04-21
- **Subjects**: Multiagent Systems (cs.MA); Artificial Intelligence (cs.AI)
- **License**: CC BY 4.0 (specification); Apache 2.0 (reference implementations @sym-bot/sym, @sym-bot/mesh-channel)

## Key Contributions
- **CAT7 schema**: Fixed seven-field schema for every Cognitive Memory Block (CMB), providing a universal message format for agent cognitive state
- **SVAF primitive**: Semantic Value Alignment Framework — evaluates each CMB field against the receiver's role-indexed anchors, enabling selective field-level acceptance (P1)
- **Inter-agent lineage**: Claims carry parents and ancestors as content-hash keys, making every piece of information traceable to its source (P2)
- **Remix primitive**: Stores only the receiver's role-evaluated understanding of accepted content, never raw peer signals (P3)
- **Production deployment**: Running in production across three reference deployments; each session is an autonomous mesh peer with its own identity and memory

## Related Papers
- [[tap-file-based-protocol-heterogeneous-llm-agent-collaboration-2606.14445]] — Both protocols address cross-session agent collaboration; tap focuses on heterogeneous cross-vendor file-based communication while Mesh Memory Protocol focuses on semantic infrastructure for cognitive state sharing
- [[hallucination-as-context-drift-synchronization-protocols-for-multi-agent-llm-systems-2606.21666]] — Both address synchronization failures in multi-agent systems; MMP provides the semantic infrastructure layer while Context Drift characterizes synchronization failure modes
