import requests
from pprint import pprint

API_Key = "" # apply for your own API key

location = "Saskatoon"  # input("Enter Your Desired Location: ")
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid="
final_url = weather_url + API_Key
weather_data = requests.get(final_url).json()

print("------------")
pprint(weather_data)