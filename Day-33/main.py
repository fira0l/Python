import requests
from datetime import datetime as dt

MY_LAT = 9.145000
MY_LONG = 40.489674

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

time_now = dt.now()
# print(time_now.hour)




