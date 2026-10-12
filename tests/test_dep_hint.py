"""Smoke checks for shared dependency hints (CI / cold-start failure mode)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import dep_hint  # noqa: E402


class DepHintTests(unittest.TestCase):
    def test_venv_hint_mentions_getting_started_and_jsonschema(self):
        hint = dep_hint._VENV_HINT
        self.assertIn("jsonschema", hint)
        self.assertIn(".venv", hint)
        self.assertIn("getting-started.md", hint)

    def test_require_jsonschema_returns_validators(self):
        Draft202012Validator, FormatChecker = dep_hint.require_jsonschema()
        self.assertTrue(callable(Draft202012Validator))
        self.assertTrue(callable(FormatChecker))


if __name__ == "__main__":
    unittest.main()
