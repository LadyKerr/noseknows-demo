import unittest

class TestRecommendPerfumes(unittest.TestCase):
    def test_recommend_perfumes(self):
        liked_perfumes = ['Perfume A', 'Perfume B']
        num_recs = 3

        result = recommend_perfumes(liked_perfumes, num_recs)

        self.assertEqual(len(result['rec_perfumes']), num_recs)
        self.assertEqual(len(result['rec_perfumes_details']), num_recs)
        self.assertTrue(all(isinstance(perfume, str) for perfume in result['rec_perfumes']))
        self.assertTrue(all(isinstance(details, dict) for details in result['rec_perfumes_details']))
        self.assertTrue(all('Name' in details for details in result['rec_perfumes_details']))
        self.assertTrue(all('Image URL' in details for details in result['rec_perfumes_details']))
        self.assertTrue(all('Description' in details for details in result['rec_perfumes_details']))
        self.assertTrue(all('Notes' in details for details in result['rec_perfumes_details']))

    def test_recommend_perfumes_invalid_perfume(self):
        liked_perfumes = ['Perfume A', 'Invalid Perfume']
        num_recs = 3

        result = recommend_perfumes(liked_perfumes, num_recs)

        self.assertEqual(len(result['rec_perfumes']), num_recs)
        self.assertEqual(len(result['rec_perfumes_details']), num_recs)
        self.assertTrue(all(isinstance(perfume, str) for perfume in result['rec_perfumes']))
        self.assertTrue(all(isinstance(details, dict) for details in result['rec_perfumes_details']))
        self.assertTrue(all('Name' in details for details in result['rec_perfumes_details']))
        self.assertTrue(all('Image URL' in details for details in result['rec_perfumes_details']))
        self.assertTrue(all('Description' in details for details in result['rec_perfumes_details']))
        self.assertTrue(all('Notes' in details for details in result['rec_perfumes_details']))

if __name__ == '__main__':
    unittest.main()