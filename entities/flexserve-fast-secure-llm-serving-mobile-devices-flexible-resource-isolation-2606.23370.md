---
title: "FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, security, mobile, privacy, llm-serving, trustzone]
sources: ["https://arxiv.org/abs/2606.23370"]
---

# FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation

## Overview
FlexServe addresses security and efficiency challenges of device-side LLM inference on mobile. It uses ARM TrustZone for hardware isolation but decouples access permission from management permission of secure resources, enabling efficient secure LLM inference without the inflexibility of traditional TrustZone designs. Introduces Recallable Resource Isolation for Flex-Mem and Flex-NPU.

## Key Facts
- **Year**: 2026
- **arXiv**: [2606.23370](https://arxiv.org/abs/2606.23370)

## Key Contributions
- Recallable Resource Isolation: secure resources can be accessed only by secure world but efficiently allocated/reclaimed by normal-world OS
- FlexServe Framework for secure LLM inference in ARM TrustZone with cooperative memory management
- Achieves 10.05x TTFT speedup over strawman TrustZone designs, 2.44x over optimized strawman
- Solves two core TrustZone problems: inflexible resource isolation and inefficient secure resource management

## Related Papers
- [[privacyalign-contextual-privacy-alignment-for-llm-agents-2606.21710]] — PrivacyAlign contextual privacy alignment for LLM agents
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Agent-native memory system readiness
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Context management as load-bearing for LLM agents
