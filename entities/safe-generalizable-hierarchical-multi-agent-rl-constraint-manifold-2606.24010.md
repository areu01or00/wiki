---
title: "Safe and Generalizable Hierarchical Multi-Agent RL via Constraint Manifold Control"
created: 2026-06-22
updated: 2026-06-22
type: entity
tags: [agent-eval, benchmark, emergent-agentic]
sources: ["https://arxiv.org/abs/2606.24010"]
---

# Safe and Generalizable Hierarchical Multi-Agent RL via Constraint Manifold Control

## Overview
Multi-agent systems are widely used in safety-critical applications that require coordinated behavior under strict safety constraints. Existing approaches face a fundamental trade-off: learning-based methods achieve strong empirical performance but lack theoretical safety guarantees, while control-theoretic methods provide guarantees but struggle to scale. We propose Constraint Manifold Control (CMC), a hierarchical multi-agent RL framework that learns a constraint manifold in the joint policy space — a low-dimensional structure encoding all safety-critical constraints — and projects actor updates onto this manifold. CMC separates safety (manifold projection) from task performance (policy gradient) into orthogonal learning phases. We prove that CMC converges to constraint-satisfying policies with probability 1 and provides formal generalizability bounds. Experiments across 4 multi-agent safety domains (collision avoidance, resource allocation, formation control, adversarial coverage) show CMC achieves 99.7% constraint satisfaction vs. 87.3% for baseline methods while maintaining equivalent task performance. We provide the first unified framework combining learning adaptivity with control-theoretic safety guarantees for hierarchical multi-agent systems.

## Key Facts
- **Authors**: Tanaka, Rin; Chen, Siyuan; Ivanov, Plamen; Dubois, Margot; Okoro, Nia; Hoffmann, Felix; Santos, Ana; Petrov, Alexei; Kim
- **Year**: 2026
- **arXiv**: [2606.24010](https://arxiv.org/abs/2606.24010)

## Key Contributions
-

## Related Papers
- [[gbc-gradient-based-connections-for-optimizing-multi-agent-systems-2606.28187]] — Gradient-based connections for multi-agent optimization
- [[beyond-goodharts-law-a-dynamic-benchmark-for-evaluating-compliance-in-multi-agent-systems-2606.07805]] — Compliance evaluation in multi-agent systems
