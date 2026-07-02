---
title: "Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [VLA, embodied-AI, knowledge-retention, benchmarking]
sources: ["https://arxiv.org/abs/2606.19297"]
---

# Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models

## Overview
Embodied Vision-Language-Action (VLA) models are typically obtained by fine-tuning powerful pretrained VLMs on robotics data. This paper shows that failures on knowledge-sensitive tasks in VLA systems are ambiguous — they conflates missing knowledge with poor generalization of low-level control. The authors introduce Act2Answer, a lightweight protocol for distinguishing knowledge gaps from control generalization failures in deployed VLA systems.

## Key Facts
- **Authors**: Kachaev, Nikita; Moskalenko, Andrey; Skripkin, Matvey + 10 others
- **Year**: 2026
- **arXiv**: [2606.19297](https://arxiv.org/abs/2606.19297)

## Key Contributions
- Identifies knowledge retention after VLA fine-tuning as a distinct failure mode from control generalization — these require different mitigation strategies
- Act2Answer protocol enables practitioners to diagnose whether VLA failures stem from hallucinated world knowledge or from low-level control policy errors
- Empirically evaluates multiple VLA families showing consistent knowledge degradation after robotics fine-tuning

## Related Papers
- [[eventvla-event-driven-visual-evidence-memory-for-long-horizon-vision-language-action-policies-2606.20092]] — Event-driven VLA with explicit visual memory mechanisms
- [[insight-self-guided-skill-acquisition-via-steerable-vlas-2606.24884]] — Skill acquisition in VLA systems
