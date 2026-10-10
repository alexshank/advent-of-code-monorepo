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

## Writeups

Each `writeups/day-x.json` holds my analysis of that day. The scratch-app AoC showcase reads these files directly, so anything said about a solution belongs here.

| Field         | Type                | Meaning                                                                                                                                  |
| ------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `title`       | string              | Official puzzle title                                                                                                                    |
| `difficulty`  | integer 1 to 10     | How hard the day was for me                                                                                                              |
| `finished`    | `YYYY-MM`, optional | Month the day was really finished. Only needed when later commits touch the file incidentally. Defaults to the month of the last commit. |
| `tags`        | list of strings     | Techniques used                                                                                                                          |
| `quote`       | `{text, source}`    | A line from the code comments, README, or notes                                                                                          |
| `description` | markdown string     | Longer thoughts on the day                                                                                                               |
| `notes`       | list, optional      | Handwritten pages for the day, as `{file, page, caption}` pointing into a file in this directory such as `implementation-notes.pdf`      |

---

## Running the solutions

Every day can be run, answer-checked, and profiled at once from this directory:

```shell
make test
```

See [`harness/README.md`](./harness/README.md) for how it works, which days only produce one answer, and what it needs installed.
