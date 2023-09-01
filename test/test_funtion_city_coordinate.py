import os
import requests
from dotenv import load_dotenv
import pytest

from app import fetch_data_city_locality

@pytest.fixture
def city_data():
    load_dotenv('.env')
    key = os.environ['KEY']
    URL = f"https://api.openweathermap.org/geo/1.0/direct?q=Paris&appid={key}"
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def test_fetch_data_city_locality_success(city_data):
    if city_data:
        longitude, latitude = fetch_data_city_locality("Paris")
        assert isinstance(longitude, float)
        assert isinstance(latitude, float)

def test_fetch_data_city_locality_error(city_data):
    if not city_data:
        result = fetch_data_city_locality("InvalidCityName")
        assert result == "ERROR !"
