import requests
from API import *


BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr"
    }
    response = requests.get(BASE_URL, params=params)
    print("Status code:", response.status_code)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data):
    if data:
        name = data["name"]
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"{name} için hava durumu:")
        print(f"Sıcaklık: {temp}°C")
        print(f"Açıklama: {description}")
    else:
        print("Şehir bulunamadı veya API hatası.")

if __name__ == "__main__":
    city = input("Şehir adı girin: ")
    weather_data = get_weather(city)
    display_weather(weather_data)