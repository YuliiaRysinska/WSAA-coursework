# get json from web
import requests
import json
url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"
response = requests.get(url)
print(response.json())

# create this json file in VSC
data = response.json()
with open("weatherdump.json",'w') as fp:
        json.dump(data,fp)


# get spesific data 'temperature'
current = data["current"]
temperature_2m = current["temperature_2m"]
print(temperature_2m)

