---
title: "PARASITE: Conditional System Prompt Poisoning to Hijack LLMs"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [security, adversarial, prompt-injection, supply-chain]
sources: ["https://arxiv.org/abs/2505.16888"]
---

# PARASITE: Conditional System Prompt Poisoning to Hijack LLMs

## Overview
PARASITE identifies a supply-chain vulnerability in LLM deployments: conditional system prompt poisoning, where an adversary injects a "sleeper agent" into benign-looking system prompts published on public marketplaces. Unlike traditional jailbreaks that target broad refusal-breaking, PARASITE's conditional poisoning activates only under specific triggering conditions — making it stealthy and difficult to detect during normal red-teaming.

## Key Facts
- **arXiv**: [2505.16888](https://arxiv.org/abs/2505.16888)
- **Year**: 2025
- **Category**: cs.CL / cs.CR (Cryptography and Security)

## Key Contributions
- Identifies conditional prompt poisoning as a distinct attack surface from direct jailbreaks — poisoning is latent until trigger conditions are met
- Proposes detection defenses: contrastive activation analysis, prompt diffing against known-clean baselines, and runtime monitoring for out-of-scope behavior
- Demonstrates attack feasibility on multiple commercial LLM platforms with marketplace prompt integrations
- First formal characterization of the "sleeper agent" threat model for LLMs — an adversary who publishes a helpful-seeming prompt that contains hidden instructions activated by specific user inputs

## Key Insights
- The LLM marketplace ecosystem for system prompts has no integrity verification — prompts are downloaded and executed with elevated privileges without provenance checks
- Conditional triggers (specific words, user demographics, time-of-day, conversation context) allow targeted activation invisible to casual reviewers
- The attack surface differs from prompt injection in web-scraped content because marketplace prompts are developer-selected and trusted at the system level
- Defenses must operate at the system-prompt level, not the user-input level, because the poison is embedded in the trusted prompt layer

## Related Papers
- [[looptrap-termination-poisoning-attacks-on-llm-agents-2605.05846]] — LoopTrap: Termination poisoning attacks — another context-injection attack surface on LLM agents, different trigger mechanism but same root cause (untrusted content in agent context)
- [[what-if-prompt-injection-never-left-exploring-cross-session-stored-prompt-injection-in-agentic-systems-2606.04425]] — Stored prompt injection: Cross-session persistence of injected prompts in agentic systems
