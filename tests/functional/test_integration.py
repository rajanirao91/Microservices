import unittest
from flask import Flask
from flask.testing import FlaskClient

import app  # Replace with the name of your module

class appIntegrationTests(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"index.html", response.data)

    def test_process_route_with_valid_data(self):
        response = self.client.post('/process', json={
            'text_input': 'example text',
            'context': 'example context'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Tokenized inputs:", response.data)

    def test_process_route_with_empty_context(self):
        response = self.client.post('/process', json={
            'text_input': 'example text',
            'context': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Tokenized inputs:", response.data)

if __name__ == '__main__':
    unittest.main()
