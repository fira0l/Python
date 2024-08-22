import requests
from twilio.rest import Client
import sys


api_key = "d45afe4162aeb8a45ea4fd69edbce754"
account_sid = ""
auth_token = ""

parameters = {
    "lat": 7.864380,
    "lon": 39.629940,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]
# print(data["hourly"][0]["weather"][0]["id"])
# print(weather_slice)

will_rain = False

for hour in weather_slice:
    condition_code = int(hour["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body ="It's is Going to rain today. Remeber to bring an ☔",
        from_="+12088048774",
        to ="+251976104860"
    )
    print(message.status)

