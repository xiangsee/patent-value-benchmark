#!/usr/bin/env python3
"""Shared dependency bootstrap with external-reproducer hints.

Encode the recurring cold-start failure mode once:
system Python without jsonschema → point at .venv + getting-started.
"""

from __future__ import annotations

import sys
from typing import Any


_VENV_HINT = """\
Missing dependency 'jsonschema'.

Local tip (external cold-start):
  python3 -m venv .venv
  source .venv/bin/activate          # Windows: .venv\\Scripts\\activate
  python -m pip install -r requirements-dev.txt

Or without activating:
  .venv/bin/python -m pip install -r requirements-dev.txt
  .venv/bin/python tools/validate_data.py

See docs/getting-started.md §1.
"""


def require_jsonschema() -> tuple[Any, Any]:
    """Import jsonschema validators or exit with a .venv hint."""
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ModuleNotFoundError as exc:  # pragma: no cover - exercised manually
        if getattr(exc, "name", None) == "jsonschema":
            print(_VENV_HINT, file=sys.stderr)
            raise SystemExit(2) from exc
        raise
    return Draft202012Validator, FormatChecker
