import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask.testing import FlaskClient

import app 
class appTests(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"index.html", response.data)

    def test_process_with_valid_data(self):
        with patch('app.tokenizer') as mock_tokenizer:
            mock_tokenizer.return_value = MagicMock(data={'input_ids': [1, 2, 3]})
            response = self.client.post('/process', json={
                'text_input': 'example text',
                'context': 'example context'
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'input_ids': [1, 2, 3]})
            mock_tokenizer.assert_called_with('example text', 'example context', truncation=True, padding=True)

    def test_process_with_empty_context(self):
        with patch('app.tokenizer') as mock_tokenizer:
            mock_tokenizer.return_value = MagicMock(data={'input_ids': [1, 2, 3]})
            response = self.client.post('/process', json={
                'text_input': 'example text',
                'context': ''
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'input_ids': [1, 2, 3]})
            mock_tokenizer.assert_called_with('example text', truncation=True, padding=True)

    @patch('app.logging')
    def test_home_exception(self, mock_logging):
        with patch('builtins.open', side_effect=Exception('Test exception')):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 500)
            mock_logging.exception.assert_called_once_with("Error reading index.html file")

    @patch('app.logging')
    def test_process_exception(self, mock_logging):
        with patch('app.tokenizer', side_effect=Exception('Test exception')):
            response = self.client.post('/process', json={
                'text_input': 'example text',
                'context': 'example context'
            })
            self.assertEqual(response.status_code, 500)
            mock_logging.exception.assert_called_once_with("Error processing input")

if __name__ == '__main__':
    unittest.main()