import requests
from pprint import pprint
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api-key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_info = {
            "City": data["name"],
            "Temperature": data["main"]["temp"],
            "Weather": data["weather"][0]["description"],
            "Humidity": data["main"]["humidity"],
            "Wind Speed": data["wind"]["speed"]
        }
        return weather_info
    else:
        return {"Error": data.get("message", "An error occurred")}
city = input("Enter the city name: ")
weather = get_weather(city)
pprint(weather)
