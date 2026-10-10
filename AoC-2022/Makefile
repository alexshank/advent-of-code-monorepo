.PHONY: test record lint format

# run every solution and assert its answers, with per-day time and memory
test:
	python3 harness/run.py

# same, but keep the numbers in harness/results/ for comparison over time
# usage: make record LABEL="what changed since last time"
record:
	python3 harness/run.py --save --label "$(LABEL)"

lint:
	uvx ruff check .

# the 2022 solutions are left as written; only harness code is formatted
format:
	uvx ruff format harness
