# Tasks: AINSSB2-1 Health check script: print ok and exit 0

- [x] T001 Create `pyproject.toml`: project metadata, `requires-python >=3.10`, `dependencies = []`, dev dependency group with `pytest` only, pytest `testpaths = ["tests"]`, no build-system and no ruff. Files: `pyproject.toml`
- [x] T002 [P] Create the stdlib-only health check script with `main()` that writes `ok\n` to stdout and returns 0, plus a `__main__` guard calling `sys.exit(main())`. Files: `scripts/healthcheck.py`
- [x] T003 Write `tests/test_healthcheck.py` with a subprocess test from the repo root (stdout `ok\n`, empty stderr, exit 0) and a second test from a different cwd via `tmp_path`, using a script path resolved from `__file__`. Files: `tests/test_healthcheck.py` (depends on T002)
- [x] T004 [P] Add a "## Health check" section to the README covering how to run `python scripts/healthcheck.py`, the expected output `ok`, and exit code 0. Files: `README.md`
- [x] T005 Run `uv run pytest` and `uvx ruff check .`, and fix any failures in the files above. Files: `scripts/healthcheck.py`, `tests/test_healthcheck.py`, `pyproject.toml` (depends on T001-T004)
- [x] T006 Verify that `git status` shows no changes under `.github/`, `.specify/`, `.claude/` or `CLAUDE.md`, and that no stray files (e.g. `__pycache__`, `.venv`) are staged. Check that `.gitignore` covers them, and add entries only if missing. Files: `.gitignore` (only if needed)
