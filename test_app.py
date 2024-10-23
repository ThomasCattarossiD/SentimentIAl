import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Set up a test client for Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_home_get(self):
        """Test GET request for the home page."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Enter text:", response.data)  # Ensure the form is present

    def test_home_post(self):
        """Test POST request to submit the form and check the output."""
        response = self.app.post('/', data={'user_input': 'Test Input'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"You entered: Test Input", response.data)  # Check if output is correct

if __name__ == '__main__':
    unittest.main()
