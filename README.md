# Advent of Code — Monorepo

Solutions to [Advent of Code](https://adventofcode.com) puzzles across multiple years, consolidated
from four separate repositories into a single place while preserving the full git history of each.

## Repository Layout

```
advent-of-code-monorepo/
├── AoC-2020/    # Python solutions
├── AoC-2022/    # Mostly Python, some Haskell and Kotlin
├── AoC-2023/    # JavaScript and Haskell solutions
└── AoC-2025/    # Python solutions
```

## Years

### [AoC-2020](./AoC-2020/README.md)
Python solutions with puzzle prompts archived in the `prompts/` folder. Each completed puzzle
includes a subjective difficulty rating and brief approach notes.

### [AoC-2022](./AoC-2022/README.md)
Mostly Python, with some Haskell and Kotlin experiments. Full 25-day run. Includes implementation
notes (`implementation-notes.pdf`) and profiler results for the trickier days.

### [AoC-2023](./AoC-2023/README.md)
Mixed-language year: JavaScript for the early days, Haskell for later ones. Partial completion.

### [AoC-2025](./AoC-2025/README.md)
Python solutions. Run any day's solution from the repo root with:
```shell
python3 ./AoC-2025/day-01/solution.py
```

## History

Each subdirectory contains the complete git history of its original standalone repository, migrated
using `git filter-repo` and `git merge --allow-unrelated-histories`. File history is fully traceable:

```shell
git log --follow -- AoC-2022/day-19.py
```
