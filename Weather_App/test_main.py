import requests
from unittest.mock import patch
from main import get_weather

mock_response_data = {
    'name': 'London',
    'sys': {'country': 'GB'},
    'main': {
        'temp': 15.0,
        'feels_like': 13.0,
        'humidity': 82
    },
    'weather': [{'description': 'light rain'}],
    'wind': {'speed': 4.1}
}

@patch('main.requests.get')
def test_get_weather_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response_data

    result = get_weather('London', 'fake_api_key')
    assert result == {
        'City': 'London',
        'Country': 'GB',
        'Temperature (°C)': 15.0,
        'Feels Like (°C)': 13.0,
        'Humidity (%)': 82,
        'Weather': 'Light Rain',
        'Wind Speed (m/s)': 4.1
    }

@patch('main.requests.get')
def test_get_weather_http_error(mock_get):
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
    result = get_weather('InvalidCity', 'fake_api_key')
    assert result is None

@patch('main.requests.get')
def test_get_weather_request_exception(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException("Network error")
    result = get_weather('London', 'fake_api_key')
    assert result is None

@patch('main.requests.get')
def test_get_weather_key_error(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {}
    result = get_weather('London', 'fake_api_key')
    assert result is None