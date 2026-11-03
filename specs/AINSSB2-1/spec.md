# Feature Specification: Health check script: print ok and exit 0

**Jira**: AINSSB2-1 | **Status**: Draft | **Autonomy**: L4 (gates G1, G2, G4 off; auto-passed with a Jira comment)

## Goal

Give operators and CI a minimal, dependency-free way to confirm the project is runnable: a script that prints `ok` and exits 0. The story also creates the project's first test, dependency manifest and README section.

## User-visible behaviour

- Running `python scripts/healthcheck.py` prints exactly `ok` followed by a newline to standard output, prints nothing to standard error, and exits with status 0.
- The script uses the Python standard library only and takes no arguments or environment configuration.
- `pyproject.toml` declares the project with `pytest` as its only dev dependency (no runtime dependencies, no ruff).
- The README has a "Health check" section that says how to run the script and what to expect.

## User scenarios

### Story 1 - Run the health check (P1)

An operator or CI job runs the script and relies on the output and exit code.

**Independent test**: run the script as a subprocess; assert stdout is `ok\n`, stderr is empty, return code is 0.

**Acceptance scenarios**:

1. **Given** a checkout with Python installed, **When** the script is run, **Then** it prints `ok` and exits 0.
2. **Given** the script is run from a different working directory using its path, **Then** the result is the same.

### Story 2 - Verified by automated test (P2)

A developer runs `uv run pytest` and the health check is verified automatically.

**Independent test**: `uv run pytest` passes with the new test included.

## Acceptance criteria

- [ ] `scripts/healthcheck.py` exists, uses only the standard library, prints `ok` and exits 0.
- [ ] Output is exactly `ok` plus a trailing newline on stdout; stderr is empty.
- [ ] A pytest test under `tests/` runs the script in a subprocess and asserts the output (and exit code 0).
- [ ] `pyproject.toml` exists; `pytest` is the only dev dependency; no runtime dependencies.
- [ ] `README.md` contains a section titled "Health check" describing how to run it and the expected output.
- [ ] `uv run pytest` and `uvx ruff check .` both pass.
- [ ] No files under `.github/`, `.specify/`, `.claude/` or `CLAUDE.md` are changed.
- [ ] The gate auto-pass comments for G1, G2 and G4 are posted by the orchestrator (L4); not part of the code change.

## Out of scope

- Real dependency, network, database or service checks.
- Flags, JSON output, verbose mode or configurable exit codes.
- Wiring the script into CI, Docker or deployment health probes.
- Adding ruff or any other tool as a dependency.
- Packaging/publishing the project.

## Open questions

- None blocking. Assumed: the Python version floor in `pyproject.toml` is the version available in CI (default 3.10+ unless the plan finds otherwise).
- Assumed: the script lives at `scripts/healthcheck.py` without needing to be an importable package.
