"""Minimal health check: print ok and exit 0."""
import sys


def main() -> int:
    sys.stdout.write("ok\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
