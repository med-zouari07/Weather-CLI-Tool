import requests
import sys

API_KEY = "your api"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    request_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        print(f"Weather in {city_name}:")
        print(f"Condition: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        save_weather_data(city_name, weather, temperature, humidity)
    else:
        print("Error fetching weather data. Please check the city name or API key.")

def save_weather_data(city_name, weather, temperature, humidity):
    with open("weather_data.txt", "a") as file:
        file.write(f"{city_name}: {weather}, {temperature}°C, {humidity}%\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        city_name = sys.argv[1]
        get_weather(city_name)
    else:
        print("Please provide a city name as an argument.")