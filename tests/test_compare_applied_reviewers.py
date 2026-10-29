import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"tools"))
from compare_applied_reviewers import compare,kappa

class BlindReviewComparisonTests(unittest.TestCase):
    def test_undefined_kappa_when_all_one_class(self):
        self.assertIsNone(kappa(["待核"]*6,["待核"]*6))
    def test_perfect_varied_kappa(self):
        self.assertEqual(kappa(["已核","待核","已核","待核"],["已核","待核","已核","待核"]),1.0)
    def test_no_actual_raters_is_not_run(self):
        self.assertEqual(compare({"B-01":{"编码":"B-01"}},{"B-01":{"编码":"B-01"}})["status"],"Not Run")
    def test_duplicate_reviewers_not_independent(self):
        a={"B-01":{"评委内部编码":"A"}}
        b={"B-01":{"评委内部编码":"A"}}
        self.assertEqual(compare(a,b)["status"],"Invalid")
    def test_incomplete_ratings_do_not_become_zeros(self):
        a={"B-01":{"评委内部编码":"A","产业实施核验":"待核","综合分（合格后）":""}}
        b={"B-01":{"评委内部编码":"B","产业实施核验":"待核","综合分（合格后）":""}}
        result=compare(a,b)
        self.assertIsNone(result["score_mae"]["综合分（合格后）"]["mean_abs_difference"])
        self.assertIsNone(result["categorical"]["产业实施核验"]["cohen_kappa"])
        self.assertEqual(result["categorical"]["产业实施核验"]["agreement"],1.0)
if __name__=="__main__":unittest.main()
