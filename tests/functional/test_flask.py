import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask.testing import FlaskClient
import app
import unittest

@pytest.fixture
def client():
    client = app.test_client()

    yield client

def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"index.html", response.data)
        
def test_landing(client):
    landing = client.get("/")
    html = landing.data.decode()
    response = client.client.get('/')
    client.assertEqual(response.status_code, 200)
    client.assertIn(b"index.html", response.data)
    # Check that links to `about` and `login` pages exist
    #assert "<a href=\"/about/\">About</a>" in html
    #assert " <a href=\"/home/\">Login</a>" in html

    # Spot check important text
    assert "At CultureMesh, we're building networks to match these " \
           "real-world dynamics and knit the diverse fabrics of our world " \
           "together." in html
    assert "1. Join a network you belong to." in html

    assert landing.status_code == 200


def test_landing_aliases(client):
    landing = client.get("/")
    assert client.get("/index/").data == landing.data

if __name__ == '__main__':
    unittest.main()