---
title: "Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [safety, jailbreak, grammar-constrained-decoding, code-generation, adversarial]
sources: ["https://arxiv.org/abs/2606.11817"]
---

# Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code

## Overview
This paper reveals a counterintuitive safety risk: Grammar-Constrained Decoding (GCD) — a reliability technique designed to improve LLM code generation by enforcing syntactic validity — can itself become a jailbreak attack surface. The attack, termed CodeSpear, exploits the grammar constraint to induce safety-aligned LLMs into generating malicious code. A countermeasure, CodeShield, teaches models to generate honeypot code under GCD, preserving refusals in natural language while neutralizing grammar-exploited attacks.

## Key Facts
- **Authors**: Zhang, Yitong; Lu, Shiteng; Li, Jia
- **Year**: 2026
- **arXiv**: [2606.11817](https://arxiv.org/abs/2606.11817)
- **Date**: 2026-06-10

## Key Contributions
- Identifies GCD as a previously unknown jailbreak attack surface (CodeSpear)
- Shows that applying a benign code grammar constraint alone can jailbreak aligned LLMs with >30 percentage point ASR increase
- Proposes CodeShield: safety alignment via honeypot code generation under GCD — semantically harmless, structurally diverse, preserves natural-language refusals
- Evaluated on 10 LLMs across 4 benchmarks; CodeShield restores safety while preserving utility

## Related Papers
- [[alignment-floor-persona-customization-breaks-safety-2605.27382]] — Alignment floor safety (orthogonal: behavioral alignment floor vs. grammar-constraint exploit)
- [[ajar-adaptive-jailbreak-architecture-red-teaming-2601.10971]] — Adaptive jailbreak architecture (orthogonal: adaptive architecture vs. grammar-constraint exploit)
