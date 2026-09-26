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
        record = copy.deepcopy(self.records[0])
        record["adjudication_events"][0]["decision_date"] = "2099-01-01"
        errors = self.validate(record)
        self.assertTrue(any("occurs after T0" in e for e in errors))

    def test_missing_evidence_is_rejected(self):
        record = copy.deepcopy(self.records[0])
        record["evidence_ids"].append("E-DOES-NOT-EXIST")
        errors = self.validate(record)
        self.assertTrue(any("missing evidence_id E-DOES-NOT-EXIST" in e for e in errors))

    def test_score_field_is_rejected(self):
        record = copy.deepcopy(self.records[0])
        record["rights_control_score"] = 99
        errors = self.validate(record)
        self.assertTrue(any("rights_control_score" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
