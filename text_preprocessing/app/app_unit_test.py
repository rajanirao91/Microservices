import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask.testing import FlaskClient
import os
import app  # Replace with the name of your module
import yaml
class appTests(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    
    def test_url(self):
        #cur_path = os.path.dirname(__file__)
        #new_path = os.path.relpath('resources/config.yaml', cur_path)
        with open("resources/config.yaml", "r") as config_file:
            config = yaml.safe_load(config_file)
            model_url = config["model_url"]
            self.assertEqual(app.model_url, model_url)
            
    
if __name__ == '__main__':
    unittest.main()