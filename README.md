# Advent of Code — Monorepo

Solutions to [Advent of Code](https://adventofcode.com) puzzles across multiple years, consolidated from four separate repositories into a single place while preserving the full git history of each.

## Repository Layout

```
advent-of-code-monorepo/
├── AoC-2019/    # C++ solutions (partial, days 1–6)
├── AoC-2020/    # Python solutions
├── AoC-2022/    # Mostly Python, some Haskell and Kotlin
├── AoC-2023/    # JavaScript and Haskell solutions
└── AoC-2025/    # Python solutions
```

## Years

### [AoC-2019](./AoC-2019/README.md)

C++ solutions for days 1–6, written while learning the language. Migrated from a separate `misc-languages` repo. Git history was **not** preserved.

### [AoC-2020](./AoC-2020/README.md)

Python solutions with puzzle prompts archived in the `prompts/` folder. Each completed puzzle includes a subjective difficulty rating and brief approach notes.

### [AoC-2022](./AoC-2022/README.md)

> **TODO:** The difficulty and description of each day are currently filled with placeholder values. These should be manually reviewed and updated with real thoughts on each day.
>
> Additionally, the tags for each day should also be reviewed and homogenized. Commit history that is read during website builds should be reviewed for any sensitive info.

Mostly Python, with some Haskell and Kotlin experiments. Full 25-day run. Includes implementation notes (`implementation-notes.pdf`) and profiler results for the trickier days, plus per-day commentary in [`writeups/`](./AoC-2022/writeups/).

#### Test Harness

A test harness was developed to run and assert correct answers for all 25 days. Additionally, this test harness profiles each day based on memory usage and execution time. Outputs are written to JSON files that can be consumed by downstream systems (mainly the showcase app).

#### Showcase App

The 2022 solutions are the source for a showcase app at [scratch.alexandershank.com/aoc](https://scratch.alexandershank.com/aoc), built from the [`scratch-app`](https://github.com/alexshank/scratch-app) repo.

This repository does not depend on `scratch-app`, does not build against it, and needs nothing from it. The source code and test harness outputs of this repo are used as input to the showcase app.

### [AoC-2023](./AoC-2023/README.md)

Mixed-language year: JavaScript for the early days, Haskell for later ones. Partial completion.

### [AoC-2025](./AoC-2025/README.md)

Python solutions. Run any day's solution from the repo root with:

```shell
python3 ./AoC-2025/day-01/solution.py
```

## History

Each subdirectory contains the complete git history of its original standalone repository, migrated using `git filter-repo` and `git merge --allow-unrelated-histories`. File history is fully traceable:

```shell
git log --follow -- AoC-2022/day-19.py
```
