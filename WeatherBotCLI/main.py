import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return f"Error: {data.get('message', 'Something went wrong.')}"
    
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']

    return (f"🌍 Weather in {city}:\n"
            f"☁️ Condition: {weather}\n"
            f"🌡️ Temp: {temp}°C (feels like {feels_like}°C)\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind Speed: {wind} m/s")


API_KEY = "abd39iirii93rYOURAPIKEYHERE"

while True:
    city = input("Enter a city (or type 'exit' to quit): ")
    if city.lower() == 'exit':
        break
    print(get_weather(city, API_KEY))
