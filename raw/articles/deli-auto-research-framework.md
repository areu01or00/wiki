---
title: "Deli_AutoResearch — Autonomous Research Framework"
url: https://victorchen96.github.io/auto_research/framework.html
fetched: 2026-06-17
type: framework-spec
tags: [autonomous, long-horizon, zero-interaction, anti-loop, heartbeat-watchdog, multi-agent, orchestration, stall-detection, state-persistence]
---

# Deli_AutoResearch — Autonomous Research Framework

A protocol framework for long-horizon autonomous tasks (days to weeks). Ships
no executable code; prescribes battle-tested conventions for state
persistence, stall detection, guardian layering, and behavioral constraints.

**Source:** https://victorchen96.github.io/auto_research/framework.html
**Type:** Agent Framework | Single self-contained SKILL.md document.
**Tags:** autonomous, long-horizon, zero-interaction, anti-loop, heartbeat-watchdog, multi-agent, unattended, orchestration

## 1. Three Failure Modes

| # | Failure Mode | Description |
|---|---|---|
| 1 | **Cognitive Loop** | Successive iterations try similar directions with diminishing returns, unable to escape a local optimum. |
| 2 | **Stalling** | Agent finishes a chunk, summarizes, waits for feedback. Session looks alive, polling runs, but work has stopped — more common than crashes. |
| 3 | **Runtime Fragility** | Context compaction silently breaks the loop; closing a session takes down timers parasitic on it. |

**Common cause:** missing engineering scaffolding, not insufficient model capability.

## 2. Behavioral Constraints (Hard Rules)

| # | Rule |
|---|---|
| i | **Zero interaction** — no Plan Mode, no question tool, no ending on a question. Continue until stopped. Resolve ambiguity yourself and log (`level=decision`). |
| ii | **Ready means execute** — finishing prep and asking "should I submit?" is the most common hidden violation. |
| iii | **Callback means report-alive** — first action of every callback updates its own `last_seen`, then checks liveness. |
| iv | **Persist state to files** — all progress in `state/` files, not conversation memory. Each iteration starts fresh, injecting only curated state. |
| v | **Guardian/worker separation** — heartbeat patrol may only do 3 things to other tasks: liveness-check, restart, nudge. Does NOT read data, modify state, or report for them. |

## 3. Architecture

```
┌── Orchestrator (current session / durable cron) ──┐
│ monitor state files → detect stalls → inject direction │
└────┬─────────────┬─────────────┬────────────┘
   [Task A]      [Task B]      [Task C]   ← each its own fresh session
```

**Three core decisions:**
1. Separate execution from evaluation
2. Fresh session over resume
3. Enforced direction diversity

## 4. State File System

```
{task}/state/
├── task_spec.md           # goal / milestones / success criteria
├── progress.json          # {iteration, total_findings, status, stale_count}
├── findings.jsonl         # accumulated findings (append-only)
├── directions_tried.json  # directions already tried
└── iteration_log.jsonl    # per-iteration summary

{task}/logs/
├── work.jsonl             # work agent; decisions tagged level=decision
├── orchestrator.jsonl     # orchestrator
└── heartbeat.jsonl        # heartbeat watchdog
```

**Log line format:** `{"ts":"...", "source":"...", "level":"info|warn|error|decision", "event":"...", "detail":"..."}`

## 5. Stall Detection & Pivoting

| Mechanism | Rule |
|---|---|
| **Stall detection** | 0 new findings or metric drop → `stale_count + 1` |
| **Forced pivot** | `stale_count >= 2` → change a **structural constraint**, not tactical parameters; `>= 4` → flag for human |
| **Direction diversity** | New direction must differ from every tried one |
| **Round cap** | Single work session caps at **15 rounds or 30 minutes** |

**Why pivot structure, not tactics:** decisive gain comes from correcting the environment/structural constraint, not tuning strategy parameters harder.

## 6. Heartbeat Watchdog (3-Layer)

| Layer | Form | Role |
|---|---|---|
| **L0** | Resident shell guard (no session) | Heartbeat stale > 2h → spin up emergency patrol via headless agent |
| **L1** | Durable cron, hourly | Check `last_seen`, restart timed-out loops, detect stalling, nudge |
| **L2** | Business loops (each its own session) | First line of each callback updates its own `last_seen` |

**Stall detection:** if progress has no update for > 2h and last output is a question → stalled, launch nudge subagent. 3 consecutive nudges with no progress → structurally stuck, reopen with new direction.

## 7. Subagent Scheduling Patterns

| Pattern | Use | Key idea |
|---|---|---|
| **A** Goal-driven | Research iteration | Inject tried directions, require verifiable findings, write back to `findings.jsonl` |
| **B** Parallel exploration | Complex sub-problems | Fire multiple agents in one message: investigation, refutation, cross-domain analogy |
| **C** Experiment run | Long compute jobs | Start minute-level polling right after submit: auto-diagnose errors, fix, resubmit |
| **D** Verification | Post-iteration QA | Independent subagent audits the evidence chain of findings |

Subagent prompt must include: background, verifiable deliverable, working directory, file/line caps, completion criteria.

## 8. Engineering Constraints

1. At most 5 large files per iteration; no single file over 300 lines.
2. State is injected via files, not conversation history.
3. Validation (test/compile/check) must run between iterations.
4. Citation-like content is verified every 20 entries, never batched up.
5. With multiple candidate directions, prefer adding diversity over digging one deeper.
6. Unresolvable external-dependency failures escalate: full report + notify owner + poll for reply; never abandon silently.

## 9. Validation & Limits

Paper-track output:

| Paper | Pages | Citations | Self-rated |
|---|---|---|---|
| Autonomous Research Agents | 59 | 228 | 8.0 |
| Continual Learning | 65 | 326 | 8.0 |
| Long-Horizon Decision-Making | 55 | 384 | 8.0 |
| Self-Play (285B RL experiment + theory hardening) | 75 | 217 | 8.6 |

**Limits (honest disclosure):**
- Scores are in-framework multi-persona simulated review; not external quality claim.
- Longest continuous run: 72 hours, 6 directional human inputs, zero operational intervention.
- Fabricated citations/data artifacts originate from LLM; framework makes external checking mechanical, doesn't remove error source.
- Separation of duties relies on protocol constraints, not model discipline.

## SKILL.md (authoritative)

The page also embeds a full copyable SKILL.md with frontmatter:
```yaml
---
name: Deli_AutoResearch
description: A protocol framework for long-horizon autonomous tasks. Targets three empirically-observed failure modes — cognitive loops, stalling, runtime fragility — by prescribing state management, stall detection, and watchdog mechanisms. Validated on multiple task types including paper writing (4 ICLR-format surveys, in-framework self-rating 8.0-8.6/10).
type: Agent Framework
tags: autonomous, long-horizon, zero-interaction, anti-loop, heartbeat-watchdog, loop, multi-agent, unattended, orchestration
---
```
