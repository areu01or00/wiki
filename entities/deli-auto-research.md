# Deli_AutoResearch

## Updates
- **2026-06-17** | [Deli_AutoResearch — Autonomous Research Framework](https://victorchen96.github.io/auto_research/framework.html) | kw: deli auto research framework | source: deli-auto-research

## Overview

Protocol framework (single self-contained `SKILL.md`) for **long-horizon autonomous tasks (days to weeks)**. Targets three empirically-observed failure modes — **cognitive loop**, **stalling**, **runtime fragility** — by prescribing state management, stall detection, and watchdog mechanisms. Ships no executable code; prescribes conventions only.

**Key principle:** "The common cause of all failures is **missing engineering scaffolding, not insufficient model capability**."

## Hard Rules (Behavioral Constraints)

1. **Zero interaction** — no Plan Mode, no question tool, no ending on a question. Continue until stopped. Log decisions (`level=decision`).
2. **Ready means execute** — never ask "should I submit?" after finishing prep. Submitting/resubmitting/fixing/starting monitors is routine.
3. **Callback means report-alive** — first action of every callback updates its own `last_seen`, then checks liveness; restarts on failure.
4. **Persist state to files** — `state/` files, not conversation memory. Each iteration starts a fresh session, injecting curated state. **Never resume.**
5. **Guardian/worker separation** — heartbeat patrol may only do 3 things to other tasks: liveness-check, restart, nudge. Does NOT read data, modify state, or report for them.

## Architecture

```
┌── Orchestrator (current session / durable cron) ──┐
│ monitor state files → detect stalls → inject direction │
└────┬─────────────┬─────────────┬────────────┘
   [Task A]      [Task B]      [Task C]   ← each its own fresh session
```

- **Separate execution from evaluation** — work agent doesn't judge its own progress
- **Fresh session over resume** — context accumulation is the primary cause of cognitive loops
- **Enforced direction diversity** — new direction must differ from all history

## State File System

```
{task}/state/
├── task_spec.md           # goal / milestones / success criteria
├── progress.json          # {iteration, status, stale_count, ...}
├── findings.jsonl         # accumulated findings (append-only)
├── directions_tried.json  # directions tried (basis for diversity)
└── iteration_log.jsonl    # per-iteration summary

{task}/logs/
├── work.jsonl             # work agent; decisions tagged level=decision
├── orchestrator.jsonl     # orchestrator
└── heartbeat.jsonl        # heartbeat watchdog
```

Log line: `{"ts":"...", "source":"...", "level":"info|warn|error|decision", "event":"...", "detail":"..."}`

## Stall Detection & Pivoting

| Mechanism | Rule |
|---|---|
| Stall detection | 0 new findings or metric drop → `stale_count + 1` |
| Forced pivot | `stale_count >= 2` → change a **structural constraint**, not tactical; `>= 4` → flag for human |
| Direction diversity | new direction must differ from every tried one |
| Round cap | single work session caps at **15 rounds or 30 minutes** |

**"Pivot structure, not tactics"** — when a task stalls repeatedly within a frame, the decisive gain comes from correcting the environment/structural constraint itself, not from tuning strategy parameters harder inside the existing frame.

## Heartbeat Watchdog (3-Layer V3)

| Layer | Form | Depends on | Role |
|---|---|---|---|
| **L0** | resident shell guard | no session | heartbeat stale > 2h → spin up emergency patrol via headless agent |
| **L1** | durable cron, hourly | a living interactive session | check each loop's `last_seen`, restart timed-out loops, detect stalling, nudge |
| **L2** | business loops | each its own session | first line of each callback updates its own `last_seen` |

Any one layer dying can be detected and recovered by another.

**Stall threshold:** 2h no update + last output is a question → stalled, launch nudge. 3 consecutive nudges with no progress → structurally stuck, stop nudging, reopen with new direction. 2h is **deliberately shorter** than 4h stuck-task threshold (stalling is voluntary stop, cheap to fix).

## Subagent Scheduling Patterns

| Pattern | Use | Key idea |
|---|---|---|
| **A** Goal-driven | research iteration | inject tried directions, require verifiable findings, write to `findings.jsonl` |
| **B** Parallel exploration | complex sub-problems | fire multiple agents in one message: investigation + refutation + cross-domain analogy |
| **C** Experiment run | long compute jobs | start minute-level polling right after submit: auto-diagnose errors, fix, resubmit |
| **D** Verification | post-iteration QA | independent subagent audits the evidence chain of findings |

Subagent prompt must include: **background, verifiable deliverable, working directory, file/line caps, completion criteria**.

## Engineering Constraints

1. At most **5 large files** per iteration; no single file over **300 lines**
2. State is injected via files, not conversation history
3. Validation (test/compile/check) must run **between iterations**
4. Citation-like content is verified **every 20 entries**, never batched
5. With multiple candidate directions, prefer **adding diversity** over digging one deeper
6. Unresolvable external-dependency failures escalate: full report + notify owner + poll for reply; **never abandon silently**

## Validation

Paper-track output (in-framework self-rating, not external):

| Paper | Pages | Citations | Self-rated |
|---|---|---|---|
| Autonomous Research Agents | 59 | 228 | 8.0 |
| Continual Learning | 65 | 326 | 8.0 |
| Long-Horizon Decision-Making | 55 | 384 | 8.0 |
| Self-Play (285B RL experiment + theory hardening) | 75 | 217 | 8.6 |

**Longest continuous run:** 72 hours, 6 directional human inputs, zero operational intervention.

## Honest Limits

- Scores are in-framework multi-persona simulated review (not external quality claim)
- Fabricated citations/data artifacts originate from the LLM; framework makes external checking mechanical, doesn't remove error source
- Separation of duties relies on **protocol constraints, not model self-discipline** — removing constraints brings overstepping back

## Cross-References

- See [[agent-orchestration]] for broader topic
- Raw source: `raw/articles/deli-auto-research-framework.md`
