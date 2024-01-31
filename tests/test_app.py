from app import app
from bs4 import BeautifulSoup
import pytest
import json


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['DEBUG'] = False
    with app.test_client() as client:
        yield client


def test_index_redirect(client):
    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200
    assert '/report' in response.request.path


def test_report_page(client):
    response = client.get('/report/')
    assert response.status_code == 200
    soup = BeautifulSoup(response.data, 'html.parser')
    table = soup.find("table", class_="table-striped")
    assert table is not None


def test_drivers_page(client):
    response = client.get('/report/drivers/')
    assert response.status_code == 200
    soup = BeautifulSoup(response.data, 'html.parser')
    drivers_list = soup.find("ul", class_="list-group")
    assert drivers_list is not None


def test_driver_info_page(client):
    driver_id = 'SVF'  # Example driver ID
    response = client.get(f'/report/drivers/{driver_id}')
    assert response.status_code == 200
    soup = BeautifulSoup(response.data, 'html.parser')
    driver_name = soup.find(string='Sebastian Vettel')
    assert driver_name is not None


def test_order_parameter(client):
    response = client.get('/report/drivers/?order=desc')
    assert response.status_code == 200

# New tests for API endpoints


def test_api_report(client):
    response = client.get('/api/v1/report/')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert isinstance(data, list)  # Expecting a list of drivers


def test_api_drivers(client):
    response = client.get('/api/v1/drivers/')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert isinstance(data, list)  # Expecting a list of drivers


def test_api_driver_info(client):
    driver_id = 'SVF'  # Example driver ID
    response = client.get(f'/api/v1/drivers/{driver_id}/')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert 'name' in data and 'team' in data  # Check for expected keys


def test_api_driver_info_not_found(client):
    driver_id = 'XYZ'  # Non-existent driver ID
    response = client.get(f'/api/v1/drivers/{driver_id}/')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data is None

def test_api_report_order_parameter(client):
    response = client.get('/api/v1/report/?order=desc')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert isinstance(data, list)  # Expecting a list of drivers

# export PYTHONPATH=$PYTHONPATH:$(pwd)
# usage: pytest tests/test_app.py
# coverage run -m pytest tests/test_app.py
# coverage report -m
