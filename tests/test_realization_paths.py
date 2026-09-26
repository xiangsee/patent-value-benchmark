from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import project_realization_paths as p  # noqa: E402
import validate_realization_paths as v  # noqa: E402


class RealizationPathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.event_schema = v.load_json(v.EVENT_SCHEMA_PATH)
        evidence_rows = v.load_jsonl(v.EVIDENCE_GLOB)
        cls.evidence_lookup = {
            obj["evidence_id"]: obj for _, _, obj in evidence_rows
        }
        cls.records = p.load_paths()
        cls.by_id = {r["path_id"]: r for r in cls.records}

    def validate(self, record):
        errors = v.schema_errors(record, self.event_schema)
        if not errors:
            errors.extend(v.validate_path_semantics(record, self.evidence_lookup))
        return errors

    def test_all_backfill_records_validate(self):
        failures = {}
        for record in self.records:
            errors = self.validate(record)
            if errors:
                failures[record["path_id"]] = errors
        self.assertEqual({}, failures)

    def test_taction_verdict_is_not_cash(self):
        snap = p.project(self.by_id["RP-TACTION-APPLE-2026"])
        self.assertIn("damages_verdict", snap["realization_mechanisms"])
        self.assertEqual("established", snap["entitlement_state"])
        self.assertEqual("unresolved", snap["economic_realization"]["cash"]["status"])
        self.assertEqual(5700000000, snap["observed_amount_events"][0]["value"])
        self.assertNotEqual("received", snap["observed_amount_events"][0]["payment_status"])

    def test_editas_realizes_cash_without_infringement(self):
        snap = p.project(self.by_id["RP-EDITAS-VERTEX-CAS9-2024"])
        self.assertEqual("contractual", snap["entitlement_state"])
        self.assertIn("license", snap["realization_mechanisms"])
        self.assertIn("receivable_monetization", snap["realization_mechanisms"])
        self.assertEqual("received", snap["economic_realization"]["cash"]["status"])
        self.assertIn(
            "receivable_sold",
            snap["economic_realization"]["contractual_future_value"]["states"],
        )

    def test_wirtgen_control_realization_without_cash(self):
        snap = p.project(self.by_id["RP-WIRTGEN-CAT-309-LEO-2026"])
        self.assertIn("exclusion_order", snap["realization_mechanisms"])
        self.assertEqual("operative", snap["economic_realization"]["control"]["status"])
        self.assertEqual("not_required", snap["economic_realization"]["cash"]["status"])

    def test_source_cannot_hand_maintain_snapshot(self):
        record = copy.deepcopy(self.records[0])
        record["current_snapshot"] = {"fake": True}
        errors = self.validate(record)
        self.assertTrue(any("current_snapshot" in e for e in errors))

    def test_post_t0_event_is_rejected(self):
        record = copy.deepcopy(self.records[0])
        record["events"][-1]["event_date"] = "2099-01-01"
        errors = self.validate(record)
        self.assertTrue(any("occurs after as_of_date" in e for e in errors))

    def test_missing_evidence_is_rejected(self):
        record = copy.deepcopy(self.records[0])
        record["events"][0]["evidence_ids"].append("E-MISSING")
        errors = self.validate(record)
        self.assertTrue(any("missing evidence_id E-MISSING" in e for e in errors))

    def test_score_is_rejected(self):
        record = copy.deepcopy(self.records[0])
        record["realization_score"] = 88
        errors = self.validate(record)
        self.assertTrue(any("realization_score" in e for e in errors))

    def test_settlement_can_realize_without_merits_judgment(self):
        synthetic = {
            "path_id": "RP-SYNTH-SETTLEMENT",
            "schema_version": "experimental-0.1",
            "rights_subject": {
                "scope_type": "patent",
                "identifiers": ["SYNTH-PATENT"],
                "note": None,
            },
            "path_type": "settlement",
            "actor": "A",
            "counterparties": ["B"],
            "jurisdiction": "US",
            "as_of_date": "2026-01-01",
            "events": [
                {
                    "event_id": "S1",
                    "event_type": "settlement_executed",
                    "event_date": "2025-12-01",
                    "date_precision": "exact",
                    "date_label": None,
                    "state_effect": "Settlement created contractual entitlement.",
                    "evidence_ids": ["E-RP-EDITAS-2023-LICENSE"],
                }
            ],
            "enforcement_capacity_context": {
                "status": "not_assessed",
                "observability": "unknown",
                "note": None,
            },
            "notes": "Synthetic projection test only.",
        }
        snap = p.project(synthetic)
        self.assertEqual("contractual", snap["entitlement_state"])
        self.assertIn("settlement", snap["realization_mechanisms"])

    def test_rights_available_without_action_has_no_realization(self):
        synthetic = {
            "path_id": "RP-SYNTH-NO-ACTION",
            "schema_version": "experimental-0.1",
            "rights_subject": {
                "scope_type": "patent",
                "identifiers": ["SYNTH-PATENT"],
                "note": None,
            },
            "path_type": "other",
            "actor": "A",
            "counterparties": ["none"],
            "jurisdiction": "US",
            "as_of_date": "2026-01-01",
            "events": [
                {
                    "event_id": "N1",
                    "event_type": "rights_available",
                    "event_date": "2025-01-01",
                    "date_precision": "exact",
                    "date_label": None,
                    "state_effect": "Rights exist but no realization action is recorded.",
                    "evidence_ids": ["E-I4I-449-E5-VALIDITY"],
                }
            ],
            "enforcement_capacity_context": {
                "status": "not_assessed",
                "observability": "unknown",
                "note": None,
            },
            "notes": "Synthetic projection test only.",
        }
        snap = p.project(synthetic)
        self.assertEqual("rights_available", snap["entitlement_state"])
        self.assertEqual([], snap["realization_mechanisms"])
        self.assertEqual("none", snap["economic_realization"]["cash"]["status"])


if __name__ == "__main__":
    unittest.main()
