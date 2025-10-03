from pathlib import Path

from fpl.domain import RuleSet


def test_rules_load():
    rs = RuleSet.load(Path("src/fpl/rules/fpl_rules.json"))
    assert "initial_setup_and_team_management" in rs.raw
