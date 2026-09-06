# AoC 2022 harness

Runs every 2022 solution, asserts its answers, and profiles how long each one takes and how much memory it uses.

```shell
make test                            # run everything
make record LABEL="what changed"     # run everything and save the numbers
make lint                            # ruff, correctness rules only
make format                          # format harness code (solutions are left alone)

python3 harness/run.py --list        # list case ids
python3 harness/run.py day-16-py     # run one or more cases
python3 harness/run.py --json        # machine-readable results
python3 harness/run.py --save        # save this run to harness/results/
python3 harness/run.py --repeats 1   # one timing run per case instead of ten
```

Exit status is non-zero if any case fails, so `make test` works as a CI gate.

## How it works

`manifest.toml` holds one case per runnable solution: an id, the command to run it, its input file, a timeout, the answer strings its output must contain, and optionally how many times to repeat it. `run.py` runs each command with `AoC-2022/` as the working directory (the solutions read their inputs from relative paths), captures combined stdout and stderr, and checks that the expected answers appear **in order**.

Matching is by substring rather than exact output for a reason: these solutions were written across a month in 2022 with no shared output convention. Some print bare numbers, some print `Part 1: <n>`, and several print grids, progress counters, or debug dumps around the answer. Substring matching lets the harness assert the answers without rewriting 25 days of solutions.

Per-case profiling comes from `os.wait4`, which returns the child's own `rusage`. That is why the runner does its own process waiting instead of using `subprocess.run`: `communicate()` reaps the child first, and the rusage goes with it. Reported per case:

- wall clock seconds
- CPU seconds (user + system)
- peak resident set size in MB (`ru_maxrss`)
- the size of the input file that case reads

Every case runs **10 times** by default and the reported figures are means, with the standard deviation of wall time shown next to it and every individual run kept in the saved record. One run of a Python program is mostly noise — interpreter startup, page cache state, CPU frequency — and a single number invites reading that noise as a result.

Three days override this in the manifest, because 10 runs of them is not worth the wall time: day 15 runs 3 times, and days 16 and 19 run once each. At 10 repeats those two alone would take about 48 minutes. Their `repeats` value is recorded in the results, so a single-run figure is never mistaken for an averaged one. Use `--repeats N` to override every case at once, e.g. `--repeats 1` for a quick correctness check.

Answers are asserted on every repeat, and the case stops early on the first failure.

The suite also reports total wall time, the slowest case, and the heaviest case.

A case that exceeds its manifest timeout is killed and reported as `TIMEOUT`, which counts as a failure.

## Recording runs

`--save` writes the whole run to `harness/results/` as JSON, tagged with the commit, whether the tree was dirty, the machine, and a `--label` describing what changed. That turns the harness into a before-and-after measurement for solution changes rather than just a pass/fail gate. See [`results/README.md`](./results/README.md).

## What the manifest records about missing parts

Several days do not print two answers, because the 2022 solutions were usually edited in place to turn part 1 into part 2 — the part 1 code no longer exists to run. Those cases assert the one answer that is still produced, and carry a `note` naming the part 1 answer recovered from the writeups. Days 1, 11, 14, 17, 19, 22, and 23 are in that state. Day 25 has no part 2 by design.

## Coverage

26 cases across three languages: 24 Python days, `day-1.hs` via `runghc`, and `day-12.kt` via the committed `day-12.jar`.

Not covered:

- `day-6.hs` — the source is an unfinished fragment and does not compile.
- Rebuilding `day-12.jar` from source. `day-12.sh` needs `kotlinc`, which is not assumed to be installed; the committed jar is run instead.

## Requirements

- Python 3.11+ (the runner uses `tomllib`)
- `uv` — used to run `ruff`, and to supply `sympy` for day 21, the only day with a third-party dependency
- `runghc` (GHC) for the day 1 Haskell case
- `java` for the day 12 Kotlin case
