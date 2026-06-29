---
title: "Human-on-the-Loop Orchestration for AI-Assisted Legal Discovery"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agentic-failure, e-discovery, trajectory-collapse, legal-AI, HOTL]
sources: ["https://arxiv.org/abs/2606.19812"]
---

# Human-on-the-Loop Orchestration for AI-Assisted Legal Discovery

## Overview
Autonomous LLM agents are increasingly deployed in electronic discovery (e-discovery), where compounding errors across multi-step reasoning chains can constitute legal malpractice. Unlike single-turn retrieval, agentic workflows operating over privileged document corpora exhibit "trajectory collapse": an early misclassification silently propagates, rendering an entire privilege review invalid. This paper introduces a four-layer verification architecture spanning planning, reasoning, execution, and uncertainty quantification to intercept failures before they compound.

## Key Facts
- **Authors**: Anushree Sinha, Srivaths Ranganathan, Abhishek Dharmaratnakar, Debanshu Das
- **Year**: 2026
- **arXiv**: [2606.19812](https://arxiv.org/abs/2606.19812)
- **Subject**: Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
- **Submitted**: 18 Jun 2026

## Key Contributions
- **Trajectory collapse taxonomy**: First structured taxonomy of agentic failures in legal information retrieval organized by functional stage — planning, reasoning, execution, and uncertainty quantification
- **Four-layer HOTL verification architecture**: Planning layer (goal tracking), reasoning layer (claim validation), execution layer (document handling), and uncertainty quantification layer (calibrated confidence)
- **61% privilege-waiver risk reduction**: Calibrated uncertainty thresholds reduce privilege-waiver risk by up to 61% versus fully autonomous deployment while routing fewer than one quarter of documents to attorney review
- **First paper to formalize trajectory collapse as a distinct failure mode in multi-turn agentic e-discovery workflows**

## Related Papers
- [[reflect-intervention-supported-error-attribution-for-silent-failures-in-llm-agent-traces-2606.09071]] — REFLECT: error attribution for silent failures — shares error attribution methodology; HOTL is the deployment instantiation, REFLECT is the diagnostic framework
- [[from-confident-closing-to-silent-failure-characterizing-false-success-in-llm-agents-2606.09863]] — False Success characterization — orthogonal axis (false success vs trajectory collapse); both are AGENTIC-PLANNING-COLLAPSE primitives but different failure modes
- [[hallucination-as-context-drift-synchronization-protocols-for-multi-agent-llm-systems-2606.21666]] — Context drift as hallucination — orthogonal axis (context drift vs trajectory collapse in legal documents); both concern multi-agent belief divergence
