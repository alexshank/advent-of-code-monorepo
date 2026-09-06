# Build log — the 2022 test harness

A running record of how this harness was built with Claude Code: what was asked for, what the agent did, which prompting choices mattered, and where the design changed in response to what the code actually looked like. Kept as raw material for a later blog post.

## The motivation

The 2022 solutions were finished in December 2022 and never touched as a set again. They work, but only in the sense that each one worked once, on the day it was written, on the machine it was written on. There was no way to answer "do all 25 days still run, and do they still produce the right answers?" without running 25 commands by hand and remembering what each should print. There was also curiosity behind it: some of these days were slow enough to be memorable — day 16 took about eight minutes with caching, day 19 needed its own profiler run — and it would be good to have those numbers measured rather than remembered.

So the goal was a single command that runs every day, asserts both answers, and profiles each day's time and memory plus the total for the suite. Deliberately not pytest, because the year is not all Python: there is a Haskell day 1, a Kotlin day 12, and everything else in Python.

## Opening move: a worktree, not a branch switch

The first instruction was to open a git worktree and a feature branch rather than switching branches in place. The main checkout was sitting on `feat/2022-writeups` with its own work in progress. A worktree gives the agent a clean checkout of `main` to build in without disturbing that.

```shell
git worktree add -b feat/2022-harness ../aoc-2022-harness main
```

This turns out to matter more with an agent than without one. An agent runs solutions, creates temp files, and installs tools; keeping all of that in a disposable directory means the real checkout is never in an ambiguous state.

## Reconnaissance before design

The agent's first several tool calls were all reads: the monorepo README, the 2022 directory listing, `helpers.py`, a handful of solutions, the import list across all days, and the available toolchain (`ruff`, `ghc`, `kotlinc`, `java`, `uv`). Then it ran every day with a timeout and captured the output.

That last step was the one that changed the design. The task description assumed a uniform shape — "run all days and assert their two answers" — and the reconnaissance showed that shape does not exist:

- Day 1 prints one number. Day 11 prints one number. So do days 14, 17, 19, 22, and 23.
- Day 7 prints a full directory tree before its answers. Day 22 prints about 176,000 lines of debug output before its answer. Day 9 and day 14 print grid animations.
- Output formats differ per day: bare numbers, `Part 1: 14526`, `Answer 2: 2772`, `answer: 1542941176480`.
- Day 10's part 2 answer is rendered pixels, not a number.
- Day 21 imports `sympy` and fails outright without it.
- `day-6.hs` is a truncated fragment that does not compile.

The reason for the missing parts is visible in the source: in 2022 the usual move was to edit part 1 into part 2 rather than keep both. Day 11 has its `worry = worry // 3` line commented out. The part 1 code is simply gone. That means "assert their two answers" is not achievable for those days without rewriting the solutions.

**Prompting lesson:** the agent was given a goal stated in terms of the desired end state, not a specification of the code to write. It spent its first phase discovering that the end state as stated was not reachable, and surfaced that as a decision rather than either silently narrowing the goal or silently rewriting 25 solutions to fit it.

## The decision point

The agent stopped and asked three questions instead of picking for me:

1. Normalize all the solutions to print two answers, do it incrementally, or leave the solutions alone and record what they actually print?
2. Tier the slow days, run everything always, or enforce a per-day timeout?
3. Reformat the existing solutions, or add lint config without touching them?

Question 3 had a hidden constraint the agent found on its own: `writeups.md` contains reference blocks citing solution line numbers, and the monorepo README documents a downstream consumer in another repository that parses that file. Reformatting the Python would shift every line number those blocks point at.

The choices made were the least invasive of each: leave the solutions untouched, enforce per-day timeouts, and lint without reformatting. The harness therefore records the world as it is — including "this day only prints part 2" — rather than reshaping the world to make the harness prettier. The missing part 1 answers are recorded in the manifest as notes, recovered from `writeups.md`, so the information is not lost even though it is not asserted.

## Two implementation details worth keeping

**Substring matching, in order.** Given output that ranges from a bare `509` to 176,000 lines of coordinate dumps, the check is: every expected answer string must appear in the combined output, in the listed order. Exact-output golden files would have been the obvious alternative, and would have been far more brittle — any debug print becomes a test failure, and day 22's golden file would be megabytes.

**`os.wait4` instead of `subprocess.run`.** Per-process memory and CPU come from the child's `rusage`, and `Popen.communicate()` reaps the child before you can read it. So the runner writes child output to a temp file, polls `os.wait4(pid, os.WNOHANG)` itself, and enforces the timeout in that loop. This is the one place where the harness is more complicated than it looks like it should be, and it is the reason the profiling numbers are per-day rather than a single number for the whole suite.

The runner was verified against synthetic cases — a wrong answer, a hang, a crash, and a 200 MB allocation — before being pointed at the real solutions, so the FAIL, TIMEOUT, ERROR, and memory-reporting paths were each known to work independently of whether the solutions passed.

## The constraint, made explicit

Partway through, the standing rule was stated outright: the agent should never edit solution files, and never run anything that reformats them. Only handwritten edits to solutions get committed.

That confirmed the choice already made, but it is worth separating the two. Before, "don't reformat the solutions" was a judgement call about line-number churn in `writeups.md`. After, it is a property of the repository: these files are a record of how each puzzle was actually solved, and an agent rewriting them — even harmlessly, even just whitespace — damages that record. The tooling has to be additive or it does not belong here.

In practice that shapes the tooling in three places. The formatter target is scoped to the agent-written directory (`ruff format harness`, never `ruff format .`). Linting is read-only, never `--fix`. And where a day's output is inconvenient — one answer instead of two, an answer buried in debug prose — the manifest records the reality rather than the solution being normalized to suit the harness. The awkwardness lives in the config file, which is disposable, instead of in the solutions, which are not.

## Measured results

All 26 cases pass. The saved baseline is `harness/results/20260906T160051Z-363ec458-dirty.json`: the whole year runs in **320.86s** and reads **277.8 KB** of input, and two days are 90% of the runtime.

| Case | Wall | Peak RSS | Input |
| --- | --- | --- | --- |
| day-16-py | 145.57s | 3138.3 MB | 3.4 KB |
| day-19-py | 142.36s | 2125.2 MB | 4.7 KB |
| day-15-py | 21.35s | 14.8 MB | 1.9 KB |
| day-23-py | 3.10s | 21.4 MB | 5.0 KB |
| day-24-py | 2.24s | 309.8 MB | 3.2 KB |
| day-13-py | 2.04s | 14.8 MB | 20.6 KB |
| day-17-py | 1.70s | 127.0 MB | 9.9 KB |
| day-12-kt | 0.33s | 349.2 MB | 5.5 KB |
| everything else | under 0.6s each | ~15 MB | 0.9-33.7 KB |

Things worth noticing:

- Days 16 and 19 are the two that were remembered as painful, and the measurement agrees. Day 16 peaks above 3 GB on 3.4 KB of input — the memoization that made part 2 finish in minutes instead of never is paid for entirely in memory.
- Input size predicts nothing. The largest input in the year is day 21 at 33.7 KB, which runs in a quarter of a second. The two slowest days read 3.4 KB and 4.7 KB. Runtime here is a property of the search space, not the file.
- Day 16's peak RSS is not stable between runs: 3.1 GB, then 4.2 GB, then 3.1 GB again, with identical code. Peak memory of a large growing dictionary depends on when it happens to resize and when the allocator returns pages. Treat it as a rough figure, and do not read a 20% change in it as a result.
- Day 24 uses 310 MB for a 2.2s run, out of proportion to every other Python day, and worth a look someday.
- The Kotlin day costs 349 MB and 0.33s, essentially all JVM startup. The Haskell day costs 157 MB under `runghc`, which is the interpreter rather than the program.
- Wall time and CPU time match almost exactly everywhere. Nothing in this year is I/O bound; it is all compute.

Two suite runs briefly overlapped during development, which made the day 15/16/19 numbers from that run meaningless. The baseline above is from a single run with nothing else competing for the machine. Worth remembering that a profiling harness measures the machine as much as the code.

## Turning a gate into an instrument

The harness started as a correctness gate: does everything still work. The next request changed what it is for. The plan is to record every run in full detail, change solutions, record again, and eventually write up which design choices actually moved time and memory. That makes the harness a measuring instrument, and instruments need provenance.

So `--save` writes the whole run to `harness/results/` as JSON, carrying more than the numbers: the commit, whether the tree was dirty at the time, the machine and CPU count, the Python version, whether it was a full suite or a subset, and a `--label` saying what changed since last time. Any one of those being missing is enough to make an old measurement unusable a month later — a fast run means nothing if you cannot tell which commit produced it, or whether it was measured on the same machine.

Recording the dirty flag matters more than it looks. Most of these measurements will be taken mid-experiment, on an uncommitted working tree, because that is when you want to know whether a change helped. The record should say plainly that it cannot be tied to a commit rather than implying it can.

Input file size was added at the same time, one field per case, straight from `stat`. It is the cheapest possible measure of problem size, and it is what makes a memory number interpretable: day 16 reading 3.4 KB of input and peaking at 4 GB is a fact about the algorithm, not about the puzzle.

## Prompting approaches used

- **State the outcome, not the implementation.** "Run all days and assert their two answers, and profile time and memory" left the agent free to discover that a manifest plus a subprocess runner beat a pytest harness for a multi-language year.
- **Say the constraints that are not in the code.** "Not necessarily pytest, there are days in other languages" ruled out the default answer up front.
- **Let reconnaissance precede design.** The most useful thing the agent did was run all 25 days before writing any harness code. Every real design decision came out of that output.
- **Make the agent surface decisions instead of guessing.** The three questions each had a materially different amount of churn behind them, from zero to a rewrite of every solution file.
- **Prefer the least invasive option when in doubt.** The harness is entirely additive: it does not modify a single 2022 solution.
