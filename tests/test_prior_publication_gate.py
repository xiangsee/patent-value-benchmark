import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from validate_prior_publication_gate import audit_case,FIXTURES

class PriorPublicationGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows={r["id"]:r for r in [json.loads(s) for s in FIXTURES.read_text(encoding="utf-8").splitlines() if s]}
    def test_all_synthetic_scenarios(self):
        for r in self.rows.values():
            self.assertEqual(audit_case(r)["status"],r["expected_status"])
    def test_later_B_does_not_inherit_earlier_A(self):
        r=self.rows["SYN-LATE-B"]
        result=audit_case(r)
        self.assertFalse(result["chronology_ok"])
        self.assertEqual(result["status"],"POST_CUTOFF")
    def test_earlier_A_still_needs_element_map(self):
        r=self.rows["SYN-EARLY-A"]
        res=audit_case(r)
        self.assertTrue(res["chronology_ok"])
        self.assertFalse(res["ready_for_claim_review"])
    def test_same_applicant_no_automatic_mapping(self):
        r=copy.deepcopy(self.rows["SYN-EARLY-A"])
        r["comparator"]["same_assignee"]=True
        r["comparator"]["same_family_root"]=True
        r["comparator"]["technical_overlap"]="verified"
        self.assertEqual(audit_case(r)["status"],"TIME_ELIGIBLE_UNMAPPED")
    def test_one_line_quote_is_not_element_map(self):
        r=copy.deepcopy(self.rows["SYN-MAPPED"])
        r["comparator"]["element_map"]=r["comparator"]["element_map"][:1]
        self.assertFalse(audit_case(r)["ready_for_claim_review"])
    def test_complete_dossier_not_legal_opinion(self):
        res=audit_case(self.rows["SYN-MAPPED"])
        self.assertEqual(res["status"],"ELEMENT_MAPPED_REVIEW")
        self.assertIsNone(res["legal_validity"]);self.assertIsNone(res["monetary_value"])
        self.assertEqual(res["E3"],"Unknown")
    def test_priority_cutoff_date_must_be_explicit(self):
        r=copy.deepcopy(self.rows["SYN-MAPPED"])
        r["subject"].pop("claimed_priority_date")
        self.assertEqual(audit_case(r)["status"],"UNTRACED")

if __name__=="__main__":
    unittest.main()
