import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract relevant data
        weather = {
            'City': data['name'],
            'Country': data['sys']['country'],
            'Temperature (°C)': data['main']['temp'],
            'Feels Like (°C)': data['main']['feels_like'],
            'Humidity (%)': data['main']['humidity'],
            'Weather': data['weather'][0]['description'].title(),
            'Wind Speed (m/s)': data['wind']['speed']
        }

        return weather

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except KeyError:
        print("Invalid response received from the API.")
    return None

def main():
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    city_name = input("Enter the city name: ").strip()

    weather_info = get_weather(city_name, api_key)

    if weather_info:
        print("\nCurrent Weather Information:")
        for key, value in weather_info.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()