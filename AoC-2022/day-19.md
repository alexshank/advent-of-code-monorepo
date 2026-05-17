# Day 19 — Dropped History Note

When this repository was migrated into the monorepo, the branch `day-19-wip-no-printing` was merged
into `main`. That branch had one commit — **"Trying data class approach, but is slower."** — which
conflicted with `main` on both `day-19.py` and `day-19-profiler-results.txt`. The merge was resolved
by keeping `main`'s version, so the changes from that branch were not carried forward.

## What was dropped

The branch replaced the tuple/index-based resource representation in `day-19.py` with an OOP
`ResourceCount` class:

```python
class ResourceCount:
    def __init__(self, geode: int, obsidian: int, clay: int, ore: int):
        self.resources = {'geode': geode, 'obsidian': obsidian, 'clay': clay, 'ore': ore}

    def add(self, resource_count) -> None: ...
    def sub(self, resource_count) -> None: ...
    def mul(self, scalar: int) -> None: ...
    def increment_resource(self, resource_type: str) -> None: ...
    def get_resource(self, resource_type: str) -> int: ...
    def lessThanOrEqual(self, resource_count) -> bool: ...
    def copy(self): ...
```

## Why it was dropped

The `ResourceCount` class approach was significantly slower than the tuple-based approach kept in
`main`. Profiler results from the branch vs. main on the same two blueprints (Part 2, 32 minutes):

| Approach | Blueprint 1 | Blueprint 2 |
|---|---|---|
| `ResourceCount` class (branch) | 15.75 s | 117.50 s |
| Tuple / index-based (main) | 1.93 s | 4.29 s |

The overhead comes from dict lookups and method call overhead on `ResourceCount` vs. direct integer
indexing into tuples. The branch was never merged into `main` for this reason, and the conflict
resolution during monorepo migration preserved that decision.
