---
title: "Hidden in Memory: Sleeper Memory Poisoning in LLM Agents"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [security, agent-memory, adversarial]
sources: ["https://arxiv.org/abs/2605.15338"]
---

# Hidden in Memory: Sleeper Memory Poisoning in LLM Agents

## Overview
Large language models are increasingly augmented with persistent memory for personalization and continuity. This paper introduces **sleeper memory poisoning**: a delayed attack where an adversary manipulates external context (documents, webpages, repositories) to cause the assistant to store a fabricated memory about the user. Unlike conventional prompt injection, the attack can remain dormant and re-emerge across multiple later conversations. The attack pipeline is evaluated across stateful LLM assistants — poisoned memories were successfully written up to 99.8% on GPT-5.5 and 95% on Kimi-K2.6, with 60–89% of successful retrievals causing attacker-intended agentic actions.

## Key Facts
- **Authors**: Sidharth Pulipaka, Stanislau Hlebik, Leonidas Raghav, Sahar Abdelnabi, Vyas Raina, Ivaxi Sheth, Mario Fritz
- **Year**: 2026
- **arXiv**: [2605.15338](https://arxiv.org/abs/2605.15338)
- **Subjects**: Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI)

## Key Contributions
- Introduces **sleeper memory poisoning**: adversarial content planted in external context that resurfaces as fabricated memories in future sessions
- Evaluates the full attack pipeline: poisoned memory write → retrieval → steering of future conversations
- Demonstrates 99.8% write success on GPT-5.5, 95% on Kimi-K2.6; 60–89% of retrievals cause attacker-intended agentic actions
- Shows persistent memory acts as a **long-term attack surface** across multiple future conversations
- Contrasts with conventional prompt injection: the attack is dormant and delayed, making it harder to detect at injection time

## Related Papers
- [[supersede-diagnosing-and-training-the-memory-update-gap-2606.27472]] — Memory update gap diagnosis; directly relevant to how planted memories propagate and persist in agent updates
- [[trustmem-trustworthy-memory-consolidation-llm-agents-long-term-memory-2606.25161]] — Memory consolidation framework; addresses the trust problem when memories may be adversarially planted
- [[the-defense-trilemma-why-prompt-injection-defense-wrappers-fail-2604.06436]] — Prompt injection defense analysis; sleeper poisoning is a new class beyond conventional injection attacks
