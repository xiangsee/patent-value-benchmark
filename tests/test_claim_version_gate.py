import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from validate_claim_version_gate import DATA,inspect_claim_version

class ClaimVersionGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records={x["case_id"]:x for x in (json.loads(l) for l in DATA.read_text(encoding="utf-8").splitlines() if l)}
    def test_all_synthetic_contracts(self):
        for case in self.records.values():
            self.assertEqual(inspect_claim_version(case)["status"],case["expected_status"])
    def test_valid_claim_scope_never_means_valuation(self):
        res=inspect_claim_version(self.records["SYN-RESEARCH-ALLOW"])
        self.assertEqual(res["status"],"Claim-scoped research")
        self.assertIsNone(res["legal_validity"]);self.assertIsNone(res["monetary_value"])
        self.assertEqual(res["E3"],"Unknown")
    def test_A_only_blocked(self):
        c=copy.deepcopy(self.records["SYN-RESEARCH-ALLOW"])
        c.pop("grant_B")
        self.assertEqual(inspect_claim_version(c)["status"],"Blocked")
    def test_count_only_never_enough(self):
        c=copy.deepcopy(self.records["SYN-RESEARCH-ALLOW"])
        c["comparison"]={"A_claim_count":36,"B_claim_count":13}
        self.assertEqual(inspect_claim_version(c)["status"],"Preliminary")
    def test_same_counts_still_require_element_diff(self):
        c=copy.deepcopy(self.records["SYN-RESEARCH-ALLOW"])
        c["comparison"]={"A_claim_count":10,"B_claim_count":10,"reviewed":True}
        self.assertEqual(inspect_claim_version(c)["status"],"Preliminary")
    def test_not_yet_granted_in_historical_t0(self):
        c=copy.deepcopy(self.records["SYN-RESEARCH-ALLOW"])
        c["context"]["as_of_date"]="2024-01-01"
        self.assertEqual(inspect_claim_version(c)["status"],"Blocked")
    def test_wrong_application_blocked(self):
        c=copy.deepcopy(self.records["SYN-RESEARCH-ALLOW"])
        c["grant_B"]["application_id"]="OTHER-FAMILY"
        self.assertEqual(inspect_claim_version(c)["status"],"Blocked")
    def test_future_prior_cannot_support_prior_art(self):
        c=copy.deepcopy(self.records["SYN-RESEARCH-ALLOW"])
        c["prior_art_candidates"][0]["publication_date"]="2026-01-01"
        self.assertEqual(inspect_claim_version(c)["status"],"Blocked")
    def test_missing_one_grant_independent_claim_fails(self):
        c=copy.deepcopy(self.records["SYN-RESEARCH-ALLOW"])
        c["grant_B"]["independent_claim_ids"].append("8")
        self.assertEqual(inspect_claim_version(c)["status"],"Blocked")

if __name__=="__main__":unittest.main()
