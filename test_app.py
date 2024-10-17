import unittest
from app import app

class BasicTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client for the Flask application
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # Test the home page for status code 200
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        # Test the home page content
        response = self.app.get('/')
        self.assertIn(b"Hello, Flask!", response.data)

if __name__ == '__main__':
    unittest.main()
