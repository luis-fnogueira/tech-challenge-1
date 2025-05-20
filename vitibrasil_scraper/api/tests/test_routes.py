import unittest
from vitibrasil_scraper.api.index import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_endpoint(self):
        """Test the index endpoint returns the expected structure"""
        response = self.app.get('/')
        data = response.get_json()

        # Test basic structure
        self.assertEqual(response.status_code, 200)
        self.assertIn('name', data)
        self.assertIn('version', data)
        self.assertIn('endpoints', data)

        # Test API info
        self.assertEqual(data['name'], 'API VitiBrasil')
        self.assertEqual(data['version'], '0.1.0')

        # Test endpoints structure
        self.assertIsInstance(data['endpoints'], list)
        self.assertTrue(len(data['endpoints']) > 0)

        # Test first endpoint structure
        first_endpoint = data['endpoints'][0]
        self.assertIn('path', first_endpoint)
        self.assertIn('methods', first_endpoint)
        self.assertIn('description', first_endpoint)
        self.assertIn('parameters', first_endpoint)

if __name__ == '__main__':
    unittest.main() 