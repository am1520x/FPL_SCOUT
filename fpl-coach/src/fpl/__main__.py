# src/fpl/__main__.py
import argparse
from pathlib import Path

from fpl.domain import RuleSet


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("cmd", nargs="?", default="demo")
    args = p.parse_args(argv)

    if args.cmd == "demo":
        # example usage so the file stays runnable/typed
        rules_path = Path("src/fpl/rules/fpl_rules.json")
        _ = RuleSet.load(rules_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
