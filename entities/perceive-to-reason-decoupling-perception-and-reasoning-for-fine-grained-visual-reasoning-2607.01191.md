---
title: "Perceive-to-Reason: Decoupling Perception and Reasoning for Fine-Grained Visual Reasoning"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [multimodal, reasoning, vision-language]
sources: ["https://arxiv.org/abs/2607.01191"]
---

# Perceive-to-Reason: Decoupling Perception and Reasoning for Fine-Grained Visual Reasoning

## Overview
Perceive-to-Reason (P2R) is a unified framework that formulates fine-grained visual reasoning as a two-stage process: first a Perceiver module localizes question-relevant evidence in high-resolution images, then a Reasoner module answers the question based on the full image plus cropped evidence regions. This explicit decoupling of perception from reasoning addresses the key failure mode in VLMs where small but critical visual cues are buried in high-resolution inputs. Built on Qwen3-VL-Instruct-2B/4B/8B, P2R-4B achieves 93.2% on V-Star, 81.9% on HR-Bench-4K, and 80.5% on HR-Bench-8K, substantially outperforming its backbone.

## Key Facts
- **Authors**: Li, Hongxing; Huang, Xiufeng; Li, Dingming + 11
- **Year**: 2026
- **arXiv**: [2607.01191](https://arxiv.org/abs/2607.01191)

## Key Contributions
- **Two-stage P2R framework**: Perceiver localizes question-relevant evidence; Reasoner processes annotated image plus cropped regions
- **PRA-GRPO training**: Perception-Reasoning Alternating GRPO — role-aware RL strategy alternating between perception-focused and reasoning-focused updates using only final-answer supervision
- **Scale-consistent improvements**: P2R consistently improves performance across Qwen3-VL-Instruct-2B/4B/8B model scales
- **Broad transfer**: Benefits extend beyond high-resolution benchmarks to broader multimodal reasoning tasks
- **Architecture insight**: Explicitly decoupling perception from reasoning is more effective than end-to-end approaches for fine-grained visual question answering

## Related Papers
- [[athena-r1-an-ai-agent-for-treatment-reasoning-over-a-biomedical-tool-universe-2606.28692]] — Athena-R1 uses tool-grounded reasoning; P2R provides a perceptual decoupling prior that could inform how tool-relevant evidence is localized before reasoning
- [[a-multi-agent-audit-framework-for-high-stakes-reasoning-evaluation-and-interpret-2606.21123]] — Multi-agent audit framework evaluates reasoning quality; P2R's decoupled architecture provides a natural split between perceptual and reasoning agents in audit pipelines
