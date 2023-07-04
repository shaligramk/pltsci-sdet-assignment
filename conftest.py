import pytest
import requests

@pytest.fixture
def api_url():
    return 'http://localhost:8080/v1/cleaning-sessions'

@pytest.fixture
def headers():
    return {'Content-Type': 'application/json'}

@pytest.fixture
def response():
    return None

@pytest.fixture
def api_client(api_url, headers):
    return requests.Session()
