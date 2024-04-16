import json
import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_recommend_endpoint(self):
        # Prepare test data
        liked_perfumes = ['perfume1', 'perfume2']
        data = {'liked_perfumes': liked_perfumes}
        headers = {'Content-Type': 'application/json'}

        # Send a GET request to the recommend endpoint
        response = self.app.get('/api/recommend', data=json.dumps(data), headers=headers)

        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert the response data is correct
        expected_recs = ['rec1', 'rec2', 'rec3']
        self.assertEqual(response.json, expected_recs)

if __name__ == '__main__':
    unittest.main()