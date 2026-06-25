---
title: "FedOT: Ownership Verification and Leakage Tracing via Watermarks for Federated LDMs"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [federated-learning, latent-diffusion-models, watermarking, ownership-verification, leakage-tracing, model-security]
sources: ["https://arxiv.org/abs/2606.22875"]
---

# FedOT: Ownership Verification and Leakage Tracing via Watermarks for Federated LDMs

## Overview
Cheng, Gan, Xu, and Miao address a structural security gap in federated training of Latent Diffusion Models (LDMs) — where FL's distributed nature creates both ownership-verification needs (proving the model belongs to the training coalition) and leakage-tracing needs (identifying which client redistributed the model), and where existing VAE-based watermarking techniques fail because they can be removed simply by replacing the decoder with a clean counterpart — and propose FedOT, the first framework for joint ownership verification and leakage tracing in federated LDMs, using a chunked watermark (one part for ownership, one part for client identification) plus Latent Vector Transformation (LVT) that modifies the VAE latent distribution so that any VAE replacement for watermark removal causes significant image-quality degradation rendering the model unusable.

## Key Facts
- **Authors**: Cheng, Wenlong; Gan, Yuan; Xu, Yunqiu; Miao, Jiaxu
- **Year**: 2026
- **arXiv**: [2606.22875](https://arxiv.org/abs/2606.22875)
- **Date**: 2026-06-22

## Key Contributions
- Diagnoses a structural security gap in federated Latent Diffusion Model (LDM) training: FL distributes the model across multiple clients who could unauthorized-redistribute or resell it, and existing VAE-based watermarking is insufficient because (1) it supports ownership verification but cannot trace which client leaked the model, and (2) VAE watermarks can be removed by swapping in a clean VAE decoder without affecting the rest of the model.
- Proposes FedOT, the first framework for *joint* ownership verification and leakage tracing in federated LDMs, using a chunked watermark where the first part supports coalition-level ownership claims and the second part encodes client-specific identification — closing both the ownership-verification gap and the per-client attribution gap in one design.
- Introduces Latent Vector Transformation (LVT), which strengthens the coupling between the VAE and U-Net latent spaces by modifying the VAE's original latent distribution, so that any attempt to remove the watermark by replacing the VAE causes significant image-quality degradation rendering the model unusable — closing the VAE-replacement attack surface.
- Surfaces a methodology-level contribution to generative-model security: ownership verification and leakage tracing are *joint design constraints*, not separable problems — a watermark that supports ownership only cannot answer "which client leaked", and a watermark that supports tracing only cannot answer "is this the coalition's model at all"; FedOT's chunked design unifies both questions into a single watermark payload with two functionally-coupled halves.

## Related Papers
- [[emergent-concepts]] — Parent meta-page that aggregates this and other emergent-concept discoveries from the wiki-explore-agent pipeline.
- [[privacyalign-contextual-privacy-alignment-for-llm-agents-2606.21710]] — Sibling privacy work in the LLM-agent surface; both papers address *structural privacy threats in distributed generative-model deployments* — PrivacyAlign does this on the LLM-agent surface by aligning context-aware privacy expectations, FedOT does it on the federated-diffusion surface by watermarking the model itself so unauthorized redistribution is attributable.
- [[when-lower-privileges-suffice-investigating-over-privileged-tool-selection-in-llm-agents-2606.20023]] — Sibling access-control work in the LLM-agent surface; both papers argue that *deployment-time leakage / over-privilege* is a load-bearing threat that the field has under-addressed — FedOT isolates model-redistribution leakage in federated diffusion training, Over-Privileged isolates tool-selection over-privilege in deployed LLM agents.
- [[diffusionbench-holistic-evaluation-diffusion-transformers-2606.24888]] — Sibling diffusion-model work; both papers address structural under-exploration in the diffusion-model surface — DiffusionBench argues for multi-axis evaluation discipline (the field uses single-anchor ImageNet-FID), FedOT argues for security discipline (the field uses VAE-replaceable watermarks). Both surface load-bearing evaluation/security gaps the canonical setup cannot probe.
