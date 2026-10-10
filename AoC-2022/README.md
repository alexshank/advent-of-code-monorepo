# AoC-2022

Advent of Code solutions for 2022 (mostly in Python). Fingers crossed we can learn some Haskell along the way.

---

## Structure

For each day, there will be the following files:

> **Note:** There may be additional test input files or `.hs` / `.kt` solution files.

- `prompts/day-x-prompt.txt`
- `inputs/day-x-input.txt`
- `writeups/day-x.json`
- `day-x.py`

---

## Running the solutions

Every day can be run, answer-checked, and profiled at once from this directory:

```shell
make test
```

See [`harness/README.md`](./harness/README.md) for how it works, which days only produce one answer, and what it needs installed.
