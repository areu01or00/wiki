---
title: "LLM-Based Scientific Peer Review: Methods, Benchmarks, and Reliability Challenges"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [llm, survey, peer-review, evaluation, robustness, llm]
sources: ["https://arxiv.org/abs/2606.25057"]
---

# LLM-Based Scientific Peer Review: Methods, Benchmarks, and Reliability Challenges

## Overview
A systems-level survey of LLM-based scientific peer review that organizes the field around two core evaluative functions — critique generation and score prediction — and presents a structured taxonomy of modeling approaches (prompt-based, supervised, retrieval-augmented, and alignment-optimized). The survey uniquely treats automated peer review as a high-stakes, multi-objective decision problem and surfaces emerging robustness risks (prompt injection, data poisoning, retrieval vulnerabilities, reward hacking) that expose automated review pipelines to strategic manipulation.

## Key Facts
- **Authors**: Thi Huyen Nguyen, Zahra Ahmadi
- **Year**: 2026
- **arXiv**: [2606.25057](https://arxiv.org/abs/2606.25057)

## Key Contributions
- **Two-function framing**: Reframes LLM peer review as critique generation + score prediction — a clean decomposition that separates the generative and ranking aspects of review.
- **Modeling-approach taxonomy**: A structured taxonomy of prompt-based, supervised, retrieval-augmented, and alignment-optimized approaches — useful as a literature navigation tool.
- **Robustness risk inventory**: Explicitly identifies prompt injection, data poisoning, retrieval vulnerabilities, and reward hacking as attack surfaces — surfacing an adversarial-evaluation axis that prior peer-review work largely overlooked.
- **Open-challenges roadmap**: From a data-mining perspective, outlines key open challenges in modeling subjective disagreement and cross-domain generalization — reframing automated review as a high-stakes, multi-objective decision problem.

## Related Papers
- [[counsel-a-meta-evaluation-dataset-for-agentic-tasks-2606.21627]] — Sibling meta-evaluation paper at the agentic-task axis; LLM peer review operates at the scientific-task axis (different content domain).
- [[beyond-static-leaderboards-predictive-validity-evaluation-llm-agents-2606.19704]] — Sibling predictive-validity critique paper at the LLM-agent-eval axis; LLM peer review operates at the LLM-reviewer axis (different evaluated subject).
- [[dailyreport-an-open-ended-benchmark-for-evaluating-search-agents-on-daily-2606.12871]] — Sibling open-ended benchmark paper at the search-agent axis; LLM peer review operates at the paper-reviewer axis (different evaluated subject).
- [[naturebench-can-coding-agents-match-the-published-sota-of-nature-family-papers-2606.24530]] — Sibling benchmark paper at the published-SOTA axis; LLM peer review operates at the review-generation axis (the inverse direction — reviewer role rather than reproduce-SOTA role).