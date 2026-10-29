"""Negative and positive applied valuation-gate tests. All data synthetic."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from validate_applied_gates import DATA, evaluate

class AppliedGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures={x["case_id"]:x for x in map(json.loads,DATA.read_text(encoding="utf-8").splitlines()) if x}
    def test_fixture_contract(self):
        for case in self.fixtures.values():
            result=evaluate(case)
            self.assertEqual(case["expected"]["valuation_status"],result["valuation_status"])
            self.assertEqual(case["expected"]["assessment_status"],result["assessment_status"])
            self.assertIsNone(result["value_amount"])
    def test_perfect_case_permits_review_but_not_prices(self):
        r=evaluate(self.fixtures["SYN-ALLOW"])
        self.assertEqual(r["assessment_status"],"Ready: Track B reviewed score")
        self.assertAlmostEqual(r["award_score"],79.1)
        self.assertEqual(r["valuation_status"],"L2: eligible to develop indicative range")
        self.assertIsNone(r["value_amount"])
    def test_high_historical_score_cannot_bypass_gates(self):
        case=copy.deepcopy(self.fixtures["SYN-MISSING-G3"])
        case["historical_score"]=99.9
        r=evaluate(case)
        self.assertEqual(r["valuation_status"],"L0: Not Valuation Ready")
        self.assertIsNone(r["value_amount"])
    def test_missing_source_blocks_fake_pass(self):
        case=copy.deepcopy(self.fixtures["SYN-ALLOW"])
        case["valuation"]["gates"][2]["evidence_ids"]=["FAKE"]
        self.assertEqual(evaluate(case)["valuation_status"],"L0: Not Valuation Ready")
    def test_wrong_subject_blocks_valuation(self):
        case=copy.deepcopy(self.fixtures["SYN-ALLOW"])
        case["valuation"]["economic_object"]="OTHER-OBJECT"
        self.assertEqual(evaluate(case)["valuation_status"],"L0: Not Valuation Ready")
    def test_post_t0_evidence_blocks_valuation(self):
        case=copy.deepcopy(self.fixtures["SYN-ALLOW"])
        for item in case["evidence_registry"]:
            if item["stage"]=="G4":item["observed_date"]="2099-01-01"
        self.assertEqual(evaluate(case)["valuation_status"],"L0: Not Valuation Ready")
    def test_duplicate_reviewers_block_award_score(self):
        case=copy.deepcopy(self.fixtures["SYN-ALLOW"])
        case["assessment"]["reviewers"][1]["reviewer_id"]="A"
        self.assertIsNone(evaluate(case)["award_score"])
    def test_one_dimension_absent_is_not_zero(self):
        case=copy.deepcopy(self.fixtures["SYN-ALLOW"])
        case["assessment"]["dimensions"]["use_protection"]["score"]=None
        self.assertIsNone(evaluate(case)["award_score"])
    def test_verdict_not_cash_or_intrinsic_price(self):
        case=copy.deepcopy(self.fixtures["SYN-ALLOW"])
        case["claimed_verdict_amount"]=5700000000
        r=evaluate(case)
        self.assertIsNone(r["value_amount"])
        self.assertTrue("L2" in r["valuation_status"])

if __name__=="__main__":
    unittest.main()
