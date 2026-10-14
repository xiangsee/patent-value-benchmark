from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import validate_rights_control as v  # noqa: E402


class RightsControlValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = v.load_json(v.SCHEMA_PATH)
        evidence_rows = v.load_jsonl(v.EVIDENCE_GLOB)
        ledger_rows = v.load_jsonl(v.LEDGER_GLOB)
        cls.evidence_lookup = {
            obj["evidence_id"]: obj for _, _, obj in evidence_rows
        }
        cls.ledger_ids = {
            obj["ledger_id"] for _, _, obj in ledger_rows
        }
        cls.records = [
            obj for _, _, obj in v.load_jsonl(v.DATA_GLOB)
        ]

    def validate(self, record):
        return v.validate_record(
            record,
            self.schema,
            self.evidence_lookup,
            self.ledger_ids,
        )

    def record_with_events(self):
        return next(r for r in self.records if r["adjudication_events"])

    def test_all_backfill_records_validate(self):
        failures = {}
        for record in self.records:
            errors = self.validate(record)
            if errors:
                failures[record["rights_control_id"]] = errors
        self.assertEqual({}, failures)

    def test_adverse_but_operative_state_is_valid(self):
        record = next(
            r for r in self.records
            if r["rights_control_id"] == "RC-CATERPILLAR-US7140693-C19-T0-2020"
        )
        self.assertEqual("rights_adverse", record["adjudication_events"][0]["outcome_category"])
        self.assertEqual("not_issued", record["finality_state"]["formal_effect"])
        self.assertEqual("operative", record["operative_control"]["remedy_status"])
        self.assertEqual([], self.validate(record))

    def test_event_after_t0_is_rejected(self):
        record = copy.deepcopy(self.record_with_events())
        record["adjudication_events"][0]["decision_date"] = "2099-01-01"
        errors = self.validate(record)
        self.assertTrue(any("occurs after T0" in e for e in errors))

    def test_missing_evidence_is_rejected(self):
        record = copy.deepcopy(self.record_with_events())
        record["evidence_ids"].append("E-DOES-NOT-EXIST")
        errors = self.validate(record)
        self.assertTrue(any("missing evidence_id E-DOES-NOT-EXIST" in e for e in errors))

    def test_score_field_is_rejected(self):
        record = copy.deepcopy(self.record_with_events())
        record["rights_control_score"] = 99
        errors = self.validate(record)
        self.assertTrue(any("rights_control_score" in e for e in errors))

    def no_ruling_record(self):
        # In-memory twin of data/experimental/rights-control/fixture-no-ruling-ordinary-r0.jsonl.
        return {
            "rights_control_id": "RC-TEST-NO-RULING-ZL202110873119X",
            "schema_version": "experimental-0.1",
            "source_ledger_ids": ["LEDGER-ZL202110873119.X"],
            "patent_id": "CN113467774B",
            "claim_set_id": "CN113467774B-ALL",
            "claims_at_issue": ["all"],
            "jurisdiction": "CN",
            "as_of_date": "2026-10-12",
            "scope_type": "all_granted_claims",
            "adjudication_events": [],
            "finality_state": {
                "status": "not_applicable",
                "appeal_status": "none_known",
                "rehearing_status": "none_known",
                "formal_effect": "not_applicable",
                "evidence_ids": [],
            },
            "operative_control": {
                "enforceability_state": "unknown",
                "remedy_types": ["none"],
                "remedy_status": "none",
                "evidence_ids": [],
            },
            # Legal-status lookup context only (no ruling found); PP01 does not set any RC state.
            "evidence_ids": ["E-TIP-PP01-PRESERVATION-CONTEXT"],
            "notes": "No-ruling RC record; optional; PP01 is context only (PP01 != R/RC).",
        }

    def test_no_ruling_record_validates(self):
        self.assertEqual([], self.validate(self.no_ruling_record()))

    def test_no_ruling_record_requires_not_applicable_finality(self):
        record = self.no_ruling_record()
        record["finality_state"]["status"] = "final"
        errors = self.validate(record)
        self.assertTrue(any("no-ruling record requires" in e for e in errors))

    def test_not_applicable_finality_with_events_is_rejected(self):
        record = copy.deepcopy(self.record_with_events())
        record["finality_state"]["status"] = "not_applicable"
        errors = self.validate(record)
        self.assertTrue(any("requires zero adjudication_events" in e for e in errors))

    def test_value_carrier_mapping_is_optional(self):
        record = copy.deepcopy(self.record_with_events())
        record.pop("value_carrier_mapping", None)
        self.assertEqual([], self.validate(record))

    def test_on_disk_no_ruling_fixture_validates(self):
        """data/experimental/rights-control/fixture-no-ruling-ordinary-r0.jsonl (#49)."""
        fixture = next(
            (
                r
                for r in self.records
                if r["rights_control_id"]
                == "RC-NO-RULING-ZL202110873119X-T0-2026-10-12"
            ),
            None,
        )
        self.assertIsNotNone(fixture, "missing on-disk no-ruling RC fixture")
        self.assertEqual([], fixture["adjudication_events"])
        self.assertEqual("not_applicable", fixture["finality_state"]["status"])
        self.assertEqual("not_applicable", fixture["finality_state"]["formal_effect"])
        self.assertNotIn("value_carrier_mapping", fixture)
        self.assertEqual([], self.validate(fixture))

    def test_on_disk_no_ruling_fixture_distinct_from_h9(self):
        # H9 has rulings; ordinary no-ruling fixture must stay empty-events.
        h9 = next(
            r
            for r in self.records
            if r["rights_control_id"].startswith("RC-HOLDOUT-H9")
        )
        self.assertTrue(h9["adjudication_events"])
        no_ruling = next(
            r
            for r in self.records
            if r["rights_control_id"]
            == "RC-NO-RULING-ZL202110873119X-T0-2026-10-12"
        )
        self.assertEqual([], no_ruling["adjudication_events"])

    def test_rc_not_required_for_ordinary_ledgers(self):
        # Ordinary contrib ledgers may omit RC entirely; one optional no-ruling
        # fixture may exist for #49 validation without making RC required.
        rc_ledgers = {lid for r in self.records for lid in r["source_ledger_ids"]}
        contrib = {lid for lid in self.ledger_ids if lid.startswith("LEDGER-ZL")}
        self.assertTrue(contrib)
        # Only the explicit no-ruling research fixture may attach to ordinary ZL.
        ordinary_with_rc = contrib & rc_ledgers
        self.assertEqual(
            {"LEDGER-ZL202110873119.X"},
            ordinary_with_rc,
            "ordinary ZL ledgers must not require RC; only #49 no-ruling fixture allowed",
        )


if __name__ == "__main__":
    unittest.main()
