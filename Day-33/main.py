import smtplib
import time
import requests
from datetime import datetime as dt

MY_LAT = 9.145000
MY_LONG = 40.489674
MY_EMAIL = "firaforpython@gmail.com"
MY_PASSWORD = "odsfplyzjibggmof"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    #
    # iss_position = (longitude, latitude)
    #
    # print(iss_position)

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
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

    time_now = dt.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.send_message(
            to_addrs="Firaolanbessa170@gmail.com",
            from_addr=MY_EMAIL,
            msg="Subject: Notifying u about the status of the ISS-Location status\n\nDear Fira, This is a notification for"
                " u so that u look up to the sky and enjoy the view of ISS station"
                                )





