import unittest
from recommend_fragrance import recommend_perfumes

class TestRecommendPerfumes(unittest.TestCase):
    def test_recommend_perfumes(self):
        liked_perfumes = ['Perfume A', 'Perfume B']
        num_recs = 5

        result = recommend_perfumes(liked_perfumes, num_recs)

        # Assert that the result contains the expected keys
        self.assertIn("rec_perfumes", result)
        self.assertIn("rec_perfumes_details", result)

        # Assert that the length of the recommended perfumes is equal to num_recs
        self.assertEqual(len(result["rec_perfumes"]), num_recs)

        # Assert that the length of the recommended perfumes details is equal to num_recs
        self.assertEqual(len(result["rec_perfumes_details"]), num_recs)

        # Assert that the recommended perfumes are not in the liked perfumes list
        for perfume in result["rec_perfumes"]:
            self.assertNotIn(perfume, liked_perfumes)

if __name__ == '__main__':
    unittest.main()