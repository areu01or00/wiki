---
title: "ActHook: Watermarking LLM Agent Trajectories"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [watermarking, llm-agent, trajectory-copyright, hook-mechanism, black-box-detection]
sources: ["https://arxiv.org/abs/2602.18700"]
---

# ActHook: Watermarking LLM Agent Trajectories

## Overview
First paper in the wiki to introduce *ActHook* — a watermarking method tailored for LLM agent trajectory datasets, inspired by hook mechanisms in software engineering, that embeds hook actions activated by a secret input key without altering the original task outcome. Because LLM agents operate sequentially, hook actions can be inserted at decision points without disrupting task flow; when the activation key is present, an LLM agent trained on watermarked trajectories produces these hook actions at a significantly higher rate, enabling reliable black-box detection. On Qwen-2.5-Coder-7B, ActHook achieves an average detection AUC of 94.3 across mathematical reasoning, web searching, and software engineering agents with negligible performance degradation — surfacing *hook-action-as-copyright-protection-primitive for high-value agent trajectory datasets* as a load-bearing primitive when trajectory data is the product, not the model.

## Key Facts
- **Authors**: not extracted in this run
- **Year**: 2026
- **arXiv**: [2602.18700](https://arxiv.org/abs/2602.18700)
- **Submission date**: 2026-02-21
- **Online date**: 2026-05-04

## Key Contributions
- **Hook-action watermarking as a trajectory-dataset copyright primitive**: existing watermark methods target text outputs and proprietary model weights, but LLM agent trajectory datasets are themselves high-value IP (task design + generation + filtering); ActHook is the first to introduce a hook-mechanism-inspired watermark tailored for *agent trajectory datasets* that embeds hook actions activated by a secret input key.
- **Sequential-decision-point insertion with task-outcome invariance**: hook actions are inserted at decision points in the agent's sequential execution flow without altering the original task outcome — surfacing *trajectory-insertion-point-as-load-bearing-degree-of-freedom* as the structurally correct primitive for trajectory watermarks, distinct from token-level watermarks because the load-bearing axis is *decision-point-trigger-during-execution* rather than *token-distribution-shift-at-output*.
- **Black-box detection AUC of 94.3 with negligible task degradation**: an LLM agent trained on watermarked trajectories produces hook actions at a significantly higher rate when the activation key is present, achieving an average detection AUC of 94.3 on Qwen-2.5-Coder-7B across mathematical reasoning, web searching, and software engineering tasks while incurring negligible performance degradation on the original task.
- **Software-engineering-inspired hook primitive as cross-domain primitive**: the hook mechanism (a piece of code activated by a secret input key) is imported from software engineering into LLM-agent copyright protection — surfacing *domain-translation-from-programming-language-primitives-to-agent-trajectory-primitives* as a load-bearing design primitive for agent IP, where the original task execution serves as the carrier and the hook action serves as the watermark channel.

## Related Papers
- [[signature-filtering-a-lightweight-enhancement-for-watermark-detection-2606.18430]] — Sibling discovery from same run that surfaces the *text-watermark-detection-hardening* side of provenance; signature filtering removes adversarial tokens from text-output watermark detection while ActHook embeds hook actions in *agent trajectory* datasets for trajectory copyright protection.
- [[forgetmark-stealthy-fingerprint-embedding-via-targeted-unlearning-2601.08189]] — Sibling discovery from same run that surfaces the *model-instance-fingerprinting* side of provenance; ForgetMark uses targeted unlearning to embed model fingerprints via LoRA adapter suppression while ActHook uses hook-action insertion at agent decision points for trajectory-dataset fingerprints.