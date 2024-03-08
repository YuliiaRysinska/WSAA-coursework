#1. get json from web
import requests
import json
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
response = requests.get(url)
#print(response.json())

#2. create this json file
data = response.json()
with open("cur_wind.json","w")as fp:
    json.dump(data,fp)

#3.ALT+SHIFT+F. get specific data: current--> wind_speed_10m
current = data["current"]
wind_speed_10m = current["wind_speed_10m"]
print(wind_speed_10m)


