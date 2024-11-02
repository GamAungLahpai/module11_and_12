import requests
import json
from apikey import open_weather_key
from datetime import datetime

# task 1
server = "https://api.chucknorris.io"
request = server + "/jokes/random"

try:
    # Make the GET request and parse the JSON response
    response = requests.get(request).json()
    # Print only the joke text
    print(response["value"])
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

# task 2
def open_weathermap(city):
    server = "https://api.openweathermap.org/data/2.5/weather"
    req = f"{server}?q={city}&appid={open_weather_key()}"
    response = requests.get(req)
    return response.status_code, requests.get(req).json()

def tem_in_cel(kelvin):
    return kelvin - 273.15

city = input("Enter which do you want to check the weather: ")

try:
    (result, data) = open_weathermap(city)
    if result == 200:
        print(f" current weather:  {data ['weather'][0]['description']},"
              f"Temperature: {tem_in_cel(data['main']['temp']):.1f}")

    elif result == 401:
        print("This is not a valid API key")
    elif result == 404:
        print("This is no weather info for" + city)
    else:
        print("Unknown response code" + str(result))

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

