import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask import Flask, request, jsonify
from flask.testing import FlaskClient
import os.path
import sys
sys.path.append('../..')
from text_preprocessing.app.app import app
from pathlib import Path

import yaml
class appTests(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        pass
        
    def test_url(self):
        
        current_directory = Path.cwd()
        parent_directory = current_directory.parent
        grandparent_directory = parent_directory.parent
        gp = grandparent_directory.resolve()
        gp.resolve()
        current_dir = Path.cwd()
        grandchild_dir = current_dir.parents[1]
        gc = grandchild_dir.resolve()
        gcnew = os.chdir(gc)
        newdir = os.path.relpath('text_preprocessing/app/resources/config.yaml', gcnew)
        with open(newdir, "r") as config_file:
            config = yaml.safe_load(config_file)
            model_url = config["model_url"]
            self.assertEqual(model_url,model_url)

if __name__ == '__main__':
    unittest.main()