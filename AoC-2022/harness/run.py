#!/usr/bin/env python3
"""Run every AoC 2022 solution, assert its answers, and profile time and memory.

Solutions read their inputs with paths relative to AoC-2022/, so every case runs
with that directory as its working directory.
"""

import argparse
import datetime
import json
import os
import platform
import statistics
import subprocess
import sys
import tempfile
import time
import tomllib
from pathlib import Path

SOLUTIONS_DIR = Path(__file__).resolve().parent.parent
MANIFEST = Path(__file__).resolve().parent / "manifest.toml"
RESULTS_DIR = Path(__file__).resolve().parent / "results"
DEFAULT_REPEATS = 10


def run_once(case):
	# os.wait4 is what gives per-child rusage; Popen.communicate would reap the
	# child first and lose it, so output goes to a temp file and we wait by hand.
	with tempfile.TemporaryFile("w+b") as sink:
		start = time.perf_counter()
		process = subprocess.Popen(case["cmd"], cwd=SOLUTIONS_DIR, stdout=sink, stderr=subprocess.STDOUT)
		deadline = start + case["timeout"]
		timed_out = False
		while True:
			pid, status, usage = os.wait4(process.pid, os.WNOHANG)
			if pid:
				break
			if time.perf_counter() > deadline:
				process.kill()
				_, status, usage = os.wait4(process.pid, 0)
				timed_out = True
				break
			time.sleep(0.01)
		wall = time.perf_counter() - start
		process.returncode = status
		sink.seek(0)
		output = sink.read().decode("utf-8", "replace")

	sample = {
		"wall_seconds": round(wall, 3),
		"cpu_seconds": round(usage.ru_utime + usage.ru_stime, 3),
		"peak_rss_mb": round(usage.ru_maxrss / 1024, 1),  # ru_maxrss is KiB on Linux
		"exit_status": status,
	}

	if timed_out:
		sample["status"] = "TIMEOUT"
		sample["detail"] = f"exceeded {case['timeout']}s"
	elif status != 0:
		sample["status"] = "ERROR"
		sample["detail"] = output.strip().splitlines()[-1] if output.strip() else "no output"
	else:
		sample["status"], sample["detail"] = check_answers(case["answers"], output)
	return sample


def run_case(case, repeats, progress):
	"""Repeat a case and aggregate it. A failure on any repeat fails the case."""
	samples = []
	for attempt in range(repeats):
		if progress:
			print(f"{case['id']:<12} run {attempt + 1}/{repeats}...", end="\r\033[K", flush=True)
		samples.append(run_once(case))
		if samples[-1]["status"] != "PASS":
			break

	walls = [sample["wall_seconds"] for sample in samples]
	memories = [sample["peak_rss_mb"] for sample in samples]
	return {
		"id": case["id"],
		"status": samples[-1]["status"],
		"detail": samples[-1]["detail"],
		"repeats": len(samples),
		"input_bytes": (SOLUTIONS_DIR / case["input"]).stat().st_size,
		"wall_seconds": round(statistics.fmean(walls), 3),
		"wall_min": min(walls),
		"wall_max": max(walls),
		"wall_stdev": round(statistics.stdev(walls), 3) if len(walls) > 1 else 0.0,
		"cpu_seconds": round(statistics.fmean([sample["cpu_seconds"] for sample in samples]), 3),
		"peak_rss_mb": round(statistics.fmean(memories), 1),
		"peak_rss_max": max(memories),
		"samples": samples,
	}


def check_answers(answers, output):
	"""Each answer must appear in the output, in order."""
	cursor = 0
	for answer in answers:
		found = output.find(answer, cursor)
		if found < 0:
			return "FAIL", f"missing answer: {answer.strip().splitlines()[0]!r}"
		cursor = found + len(answer)
	return "PASS", ""


def git_state():
	def git(*args):
		return subprocess.run(["git", *args], cwd=SOLUTIONS_DIR, capture_output=True, text=True).stdout.strip()

	# a dirty tree means the record cannot be traced back to a commit, so say so
	return {
		"commit": git("rev-parse", "HEAD"),
		"branch": git("rev-parse", "--abbrev-ref", "HEAD"),
		"dirty": bool(git("status", "--porcelain")),
	}


def save_record(results, suite_wall, label, full_suite):
	state = git_state()
	record = {
		"recorded_at": datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds"),
		"label": label,
		"full_suite": full_suite,
		"git": state,
		"machine": {
			"platform": platform.platform(),
			"processor": platform.processor(),
			"cpu_count": os.cpu_count(),
			"python": platform.python_version(),
		},
		"suite_wall_seconds": round(suite_wall, 3),
		"total_input_bytes": sum(result["input_bytes"] for result in results),
		"results": results,
	}

	RESULTS_DIR.mkdir(exist_ok=True)
	stamp = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%SZ")
	path = RESULTS_DIR / f"{stamp}-{state['commit'][:8]}{'-dirty' if state['dirty'] else ''}.json"
	path.write_text(json.dumps(record, indent=2) + "\n")
	return path


def main():
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("cases", nargs="*", help="case ids to run, e.g. day-01-py (default: all)")
	parser.add_argument("--list", action="store_true", help="list case ids and exit")
	parser.add_argument("--json", action="store_true", help="emit results as JSON")
	parser.add_argument("--save", action="store_true", help="save the run to harness/results/ for comparison over time")
	parser.add_argument("--label", default="", help="what changed since the last run, stored with --save")
	parser.add_argument(
		"--repeats",
		type=int,
		help=f"override every case's repeat count (default: {DEFAULT_REPEATS}, or the manifest's per-case value)",
	)
	args = parser.parse_args()

	cases = tomllib.loads(MANIFEST.read_text())["case"]
	if args.list:
		print("\n".join(case["id"] for case in cases))
		return 0
	if args.cases:
		wanted = set(args.cases)
		cases = [case for case in cases if case["id"] in wanted]
		for missing in sorted(wanted - {case["id"] for case in cases}):
			print(f"no such case: {missing}", file=sys.stderr)
			return 2

	# progress ticker only helps on a terminal; it would be noise in a pipe
	progress = not args.json and sys.stdout.isatty()
	results = []
	suite_start = time.perf_counter()
	for case in cases:
		result = run_case(case, args.repeats or case.get("repeats", DEFAULT_REPEATS), progress)
		results.append(result)
		if not args.json:
			print(
				f"{result['id']:<12} {result['status']:<8} "
				f"{result['wall_seconds']:>8.2f}s +-{result['wall_stdev']:<6.2f} "
				f"{result['peak_rss_mb']:>7.1f} MB "
				f"{result['input_bytes'] / 1024:>6.1f} KB in "
				f"x{result['repeats']:<3} {result['detail']}".rstrip()
			)
	suite_wall = time.perf_counter() - suite_start
	failed = [result for result in results if result["status"] != "PASS"]
	saved = save_record(results, suite_wall, args.label, not args.cases) if args.save else None

	if args.json:
		print(json.dumps({"suite_wall_seconds": round(suite_wall, 3), "results": results}, indent=2))
	else:
		slowest = max(results, key=lambda result: result["wall_seconds"])
		heaviest = max(results, key=lambda result: result["peak_rss_mb"])
		print(f"\n{len(results) - len(failed)}/{len(results)} passed in {suite_wall:.2f}s")
		print(f"slowest: {slowest['id']} ({slowest['wall_seconds']:.2f}s mean)")
		print(f"heaviest: {heaviest['id']} ({heaviest['peak_rss_mb']:.1f} MB mean)")
		print(f"input read: {sum(result['input_bytes'] for result in results) / 1024:.1f} KB")
		if saved:
			print(f"saved: {saved.relative_to(SOLUTIONS_DIR)}")
	return 1 if failed else 0


if __name__ == "__main__":
	sys.exit(main())
