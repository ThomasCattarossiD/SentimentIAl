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
        self.assertIn(b"TOS Violation Detection", response.data)  # Ensure the title is present

    def test_home_post_offensive_input(self):
        """Test POST request with input that should be classified as offensive."""
        response = self.app.post('/', data={'user_input': 'I hate everyone!'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The message is likely to contain harmful or offensive content.', response.data)

    def test_home_post_non_offensive_input(self):
        """Test POST request with input that should not be classified as offensive."""
        response = self.app.post('/', data={'user_input': 'I love programming!'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The message does not seem to break TOS regarding racism or hate speech.', response.data)

    def test_home_post_edge_case(self):
        """Test POST request with a neutral input."""
        response = self.app.post('/', data={'user_input': 'This is a neutral statement.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The message does not seem to break TOS regarding racism or hate speech.', response.data)

if __name__ == '__main__':
    unittest.main()
