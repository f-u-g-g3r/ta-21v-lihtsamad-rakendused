import json
import pip._vendor.requests

api_key = "48e84370663b15b4520231f167f6262b"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Tallinn"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = pip._vendor.requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    z = x["weather"]
    print(" Temperature in Tallin = " + str(round(current_temperature - 273.15, 1)))
 
else:
    print(" City Not Found ")