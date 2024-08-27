#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests

g_sheets = "https://api.sheety.co/adacce6626dffa15bf442c3d9acb17c4/flightDeals/prices"


# import requests

import amadeus
import os


parameters = {
    "originLocationCode": "ADD",
    "destinationLocationCode": "JIM",
    "departureDate": "2024-09-11",
    "adults": 1
}


amadeus_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

access_header = {
    "Content-Type": "application/x-www-form-urlencoded"
}

authorization_header = {
    "Authorization": f"Bearer {os.environ.get('AUTH_TOKEN')}"
}

access = {
    "grant_type": "client_credentials",
    "client_id": os.environ.get("AMADEUS_KEY"),
    "client_secret": os.environ.get("AMADEUS_SECRET")
}


param = {
    "airline": "IB"
}
#
# response = requests.get(url="https://test.api.amadeus.com/v2/reference-data/urls/checkin-links", json=param, headers=authorization_header)
# print(response.json())


# access_token = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token/", json=access, headers=access_header)
# access_token.raise_for_status()
# print(access_token.text)
# print(access_token.json())

response = requests.get(url=amadeus_url, params=parameters, headers=authorization_header)
response.raise_for_status()
#
print(response.text)


