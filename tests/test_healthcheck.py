import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "healthcheck.py"


def _run(cwd=None):
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        check=False,
        capture_output=True,
        text=True,
        cwd=cwd,
    )


def test_healthcheck_from_repo_root():
    result = _run(cwd=SCRIPT.parent.parent)
    assert result.stdout == "ok\n"
    assert result.stderr == ""
    assert result.returncode == 0


def test_healthcheck_from_other_directory(tmp_path):
    result = _run(cwd=tmp_path)
    assert result.stdout == "ok\n"
    assert result.stderr == ""
    assert result.returncode == 0
