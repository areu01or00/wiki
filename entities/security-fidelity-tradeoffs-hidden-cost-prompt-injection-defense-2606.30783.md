---
title: "Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [safety, security, prompt-injection, defense, llm]
sources: ["https://arxiv.org/abs/2606.30783"]
---

# Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense

## Overview
The paper identifies a fundamental security-fidelity tradeoff in defending LLMs against indirect prompt injection: defenses resist injected instructions by suppressing untrusted text, which corrupts tasks that must preserve it (translation, document editing). Attack-success metrics miss this because a model that ignores an injection and one that faithfully processes it score identically. The paper introduces SecFid, a benchmark where executing, processing, and ignoring injections produce distinguishable outputs.

## Key Facts
- **Authors**: Hermon, Mitchell; Gupta, Rahul; Ruan, Weitong + 2
- **Year**: 2026
- **arXiv**: [2606.30783](https://arxiv.org/abs/2606.30783)
- **Online Date**: 2026-06-29

## Key Contributions
- Identifies security-fidelity tradeoff as a fundamental property of prompt injection defense, not a defect
- Shows no model or defense achieves both high security and high fidelity across 1,168 examples / 48 configurations
- Demonstrates decision-theoretic analysis: the correct behavior depends on deployment context (relative cost of hijack vs. dropped span), not the defense alone
- Exposes that security-alone metrics hide the fidelity price paid for robustness
- First benchmark to make fidelity measurable for prompt injection defense

## Related Papers
- [[adaptive-evaluation-out-of-band-defenses-against-prompt-injection-in-llm-agents-2606.26479]] — Adaptive evaluation framework for prompt injection defenses in LLM agents
- [[defending-against-adaptive-prompt-injection-attacks-via-reasoning-enabled-task-alignment-2606.15441]] — Reasoning-enabled task alignment defense against adaptive prompt injection
- [[agentvisor-defending-llm-agents-prompt-injection-semantic-virtualization-2604.24118]] — Semantic virtualization defense for LLM agents against prompt injection
