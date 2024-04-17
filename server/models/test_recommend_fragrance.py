import unittest
from recommend_fragrance import recommend_perfumes

class TestRecommendPerfumes(unittest.TestCase):
    def test_recommend_perfumes(self):
        # Test case 1: Liked perfumes exist in the database
        liked_perfumes = ['Perfume A', 'Perfume B']
        expected_rec_perfumes = ['Perfume C', 'Perfume D', 'Perfume E', 'Perfume F', 'Perfume G']
        expected_rec_perfumes_details = [
            {'Name': 'Perfume C', 'Image URL': 'url_c', 'Description': 'desc_c', 'Notes': 'notes_c'},
            {'Name': 'Perfume D', 'Image URL': 'url_d', 'Description': 'desc_d', 'Notes': 'notes_d'},
            {'Name': 'Perfume E', 'Image URL': 'url_e', 'Description': 'desc_e', 'Notes': 'notes_e'},
            {'Name': 'Perfume F', 'Image URL': 'url_f', 'Description': 'desc_f', 'Notes': 'notes_f'},
            {'Name': 'Perfume G', 'Image URL': 'url_g', 'Description': 'desc_g', 'Notes': 'notes_g'}
        ]

        result = recommend_perfumes(liked_perfumes)
        self.assertEqual(result['rec_perfumes'], expected_rec_perfumes)
        self.assertEqual(result['rec_perfumes_details'], expected_rec_perfumes_details)

        # Test case 2: Liked perfumes do not exist in the database
        liked_perfumes = ['Perfume X', 'Perfume Y']
        expected_rec_perfumes = ['Perfume C', 'Perfume D', 'Perfume E', 'Perfume F', 'Perfume G']
        expected_rec_perfumes_details = [
            {'Name': 'Perfume C', 'Image URL': 'url_c', 'Description': 'desc_c', 'Notes': 'notes_c'},
            {'Name': 'Perfume D', 'Image URL': 'url_d', 'Description': 'desc_d', 'Notes': 'notes_d'},
            {'Name': 'Perfume E', 'Image URL': 'url_e', 'Description': 'desc_e', 'Notes': 'notes_e'},
            {'Name': 'Perfume F', 'Image URL': 'url_f', 'Description': 'desc_f', 'Notes': 'notes_f'},
            {'Name': 'Perfume G', 'Image URL': 'url_g', 'Description': 'desc_g', 'Notes': 'notes_g'}
        ]

        result = recommend_perfumes(liked_perfumes)
        self.assertEqual(result['rec_perfumes'], expected_rec_perfumes)
        self.assertEqual(result['rec_perfumes_details'], expected_rec_perfumes_details)

if __name__ == '__main__':
    unittest.main()