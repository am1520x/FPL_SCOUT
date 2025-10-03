from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class RuleSet:
    raw: dict[str, Any]

    @classmethod
    def load(cls, path: Path) -> RuleSet:
        data = json.loads(Path(path).read_text())
        return cls(raw=data)
