# Suite results

One JSON file per recorded run, written by `python3 harness/run.py --save` (or `make record LABEL="..."`).

The point is comparison over time: run the suite, change a solution, run it again, and the two files show exactly what the change cost or saved, per day, in wall time and peak memory.

Each file records:

- `label` — what changed since the last run, passed via `--label`
- `git` — commit, branch, and whether the tree was dirty. A dirty tree means the numbers cannot be tied to a commit, so the filename is suffixed `-dirty` too
- `machine` — platform, CPU count, and Python version, because these numbers are only comparable within one machine
- `full_suite` — false when only some cases were run, so partial runs are not mistaken for baselines
- `suite_wall_seconds` and `total_input_bytes`
- `results` — per case: `input_bytes`, `wall_seconds`, `cpu_seconds`, `peak_rss_mb`, `exit_status`, `status`, `detail`

Filenames are `<UTC timestamp>-<short commit>[-dirty].json`.

Two cautions when reading these:

- Peak RSS for the memory-heavy days is not stable run to run. Day 16 has been seen at both 3.1 GB and 4.2 GB with identical code.
- Do not record a run while anything else heavy is running on the machine, including a second copy of this suite.
