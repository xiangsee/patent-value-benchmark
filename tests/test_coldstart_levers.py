from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import scaffold_ledger as scaffold  # noqa: E402
import validate_data as v  # noqa: E402


def _ledger(stage: str, levels: list[str], link: str, patent_value: str = "unknown") -> dict:
    return {
        "v0_7_state": {
            "realization_stage": stage,
            "attribution_evidence_state": {
                "evidence_levels_present": levels,
                "exact_patent_value_carrier_link": link,
                "patent_level_attributable_value": patent_value,
                "evidence_ids": [],
            },
        },
        "knowledge_origin": {"evidence_ids": []},
        "technology": {"evidence_ids": []},
        "value_carriers": [],
        "value_links": [],
        "value_metrics": [],
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

    def test_supporting_evidence_levels_ignores_unknown(self):
        rows = [
            {"evidence_level": "E2", "status": "confirmed"},
            {"evidence_level": "E3", "status": "unknown"},
            {"evidence_level": "E2", "status": "strong_evidence"},
            {"evidence_level": "E1", "status": "unknown"},
        ]
        self.assertEqual({"E2"}, v.supporting_evidence_levels(rows))

    def test_unknown_e3_does_not_count_as_present(self):
        """PR #32 lesson: sought-but-not-found E3 stays in evidence file but
        must not put E3 in evidence_levels_present."""
        ledger = _ledger("R0", ["E2", "E3"], "unknown")
        ledger["v0_7_state"]["attribution_evidence_state"]["evidence_ids"] = [
            "E-PRODUCT",
            "E-SOUGHT-E3",
        ]
        evidence = {
            "E-PRODUCT": {"evidence_level": "E2", "status": "confirmed"},
            "E-SOUGHT-E3": {"evidence_level": "E3", "status": "unknown"},
        }
        errors = v.coldstart_consistency_errors("L1", ledger, evidence)
        self.assertTrue(any("unknown-E3" in e or "status≠unknown" in e or "status!=unknown" in e or "without status" in e for e in errors))
        self.assertTrue(any("E3" in e for e in errors))

    def test_r0_e2_with_unknown_e3_row_ok_when_levels_exclude_e3(self):
        """Align with BYD / 远光 cold-starts: levels=['E2'] even if unknown E3 row exists."""
        ledger = _ledger("R0", ["E2"], "unknown")
        ledger["v0_7_state"]["attribution_evidence_state"]["evidence_ids"] = [
            "E-PRODUCT",
            "E-SOUGHT-E3",
        ]
        evidence = {
            "E-PRODUCT": {"evidence_level": "E2", "status": "confirmed"},
            "E-SOUGHT-E3": {"evidence_level": "E3", "status": "unknown"},
        }
        errors = v.coldstart_consistency_errors("L1", ledger, evidence)
        self.assertEqual([], errors)

    def test_e3_present_requires_non_unknown_support(self):
        ledger = _ledger("R3", ["E2", "E3"], "confirmed")
        ledger["v0_7_state"]["attribution_evidence_state"]["evidence_ids"] = [
            "E-PRODUCT",
            "E-MAP",
        ]
        evidence = {
            "E-PRODUCT": {"evidence_level": "E2", "status": "confirmed"},
            "E-MAP": {"evidence_level": "E3", "status": "confirmed"},
        }
        errors = v.coldstart_consistency_errors("L1", ledger, evidence)
        self.assertEqual([], errors)


class ScaffoldBibliographicTests(unittest.TestCase):
    def test_build_ledger_seeds_optional_biblio(self):
        ledger = scaffold.build_ledger(
            application_number="ZL202012345678.9",
            title="示例",
            assignees=["甲公司"],
            as_of_date="2026-10-12",
            publication_number="CN123456789A",
            grant_number="CN123456789B",
            filing_date="2020-06-22",
            grant_date="2024-02-02",
            earliest_priority_date="2020-01-01",
            family_note="Sibling CN999 — do not inherit.",
        )
        patent = ledger["patent"]
        self.assertEqual("CN123456789A", patent["publication_number"])
        self.assertEqual("CN123456789B", patent["grant_number"])
        self.assertEqual("2020-06-22", patent["filing_date"])
        self.assertEqual("2024-02-02", patent["grant_date"])
        self.assertEqual("2020-01-01", patent["earliest_priority_date"])
        self.assertIn("Sibling", patent["family_note"])
        self.assertEqual("R0", ledger["v0_7_state"]["realization_stage"])
        self.assertIn("Bibliographic flags supplied", ledger["notes"])
        self.assertIn("evidence_levels_present", ledger["notes"])

    def test_build_ledger_null_biblio_hints_hand_fill(self):
        ledger = scaffold.build_ledger(
            application_number="ZL202012345678.9",
            title="示例",
            assignees=[],
            as_of_date="2026-10-12",
        )
        self.assertIsNone(ledger["patent"]["publication_number"])
        self.assertIsNone(ledger["patent"]["grant_number"])
        self.assertIn("Bibliographic fields still null", ledger["notes"])
        self.assertIn("--publication-number", ledger["notes"])

    def test_parser_accepts_optional_biblio_flags(self):
        parser = scaffold.build_parser()
        args = parser.parse_args(
            [
                "--application-number",
                "ZL202012345678.9",
                "--title",
                "示例",
                "--publication-number",
                "CN123456789A",
                "--grant-number",
                "CN123456789B",
                "--filing-date",
                "2020-06-22",
                "--grant-date",
                "2024-02-02",
            ]
        )
        self.assertEqual("CN123456789A", args.publication_number)
        self.assertEqual("CN123456789B", args.grant_number)
        self.assertEqual("2020-06-22", args.filing_date)
        self.assertEqual("2024-02-02", args.grant_date)



class ScaffoldTrapHintTests(unittest.TestCase):
    def test_notes_mention_prefiling_and_carrier_hint(self):
        ledger = scaffold.build_ledger(
            application_number="ZL202012345678.9",
            title="示例",
            assignees=["甲公司"],
            as_of_date="2026-10-12",
        )
        notes = ledger["notes"]
        self.assertIn("before this application filing", notes)
        self.assertIn("equipment or component", notes)

    def test_cli_help_path_still_builds(self):
        parser = scaffold.build_parser()
        args = parser.parse_args(["--application-number", "ZL1", "--title", "t"])
        self.assertEqual("ZL1", args.application_number)


if __name__ == "__main__":
    unittest.main()
