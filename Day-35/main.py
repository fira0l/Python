import requests

api_key = "d45afe4162aeb8a45ea4fd69edbce754"

parameters = {
    "lat": 7.864380,
    "lon": 39.629940,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
