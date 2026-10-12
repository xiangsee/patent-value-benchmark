from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import validate_data as v  # noqa: E402


def _ledger(stage: str, levels: list[str], link: str, patent_value: str = "unknown") -> dict:
    return {
        "v0_7_state": {
            "realization_stage": stage,
            "attribution_evidence_state": {
                "evidence_levels_present": levels,
                "exact_patent_value_carrier_link": link,
                "patent_level_attributable_value": patent_value,
            },
        }
    }


class ColdstartLeverTests(unittest.TestCase):
    def test_r0_with_e2_only_is_ok(self):
        errors = v.coldstart_consistency_errors(
            "L1", _ledger("R0", ["E2"], "unknown")
        )
        self.assertEqual([], errors)

    def test_sibling_false_mapping_blocked(self):
        errors = v.coldstart_consistency_errors(
            "L1", _ledger("R3", ["E2"], "confirmed")
        )
        self.assertTrue(any("requires E3" in e for e in errors))
        self.assertTrue(any("sibling-family" in e for e in errors))

    def test_r0_cannot_claim_exact_link(self):
        errors = v.coldstart_consistency_errors(
            "L1", _ledger("R0", ["E2", "E3"], "confirmed")
        )
        self.assertTrue(any("R0 requires exact_patent_value_carrier_link=unknown" in e for e in errors))

    def test_portfolio_non_inheritance_needs_e4(self):
        errors = v.coldstart_consistency_errors(
            "L1", _ledger("R5", ["E3"], "confirmed", "confirmed")
        )
        self.assertTrue(any("requires E4" in e for e in errors))
        self.assertTrue(any("portfolio/program" in e for e in errors))

    def test_confirmed_link_with_e3_ok(self):
        errors = v.coldstart_consistency_errors(
            "L1", _ledger("R4", ["E2", "E3"], "confirmed")
        )
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
