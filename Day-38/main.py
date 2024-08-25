import requests


USER_SID = "105f4e75"
API_KEY = "f37315f4d36bc5d593199639e2a31426"
HOST_DOMAIN = "https://trackapi.nutritionix.com"
ENDPOINT = "/v2/natural/exercise"


WEIGHT = 87
HEIGHT = 168.5
AGE = 22

user_query = input("What Kind of Exercise did u perform? ")

headers = {
    "x-app-id": USER_SID,
    "x-app-key": API_KEY
}

parameters = {
    "query": user_query,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=f"{HOST_DOMAIN}{ENDPOINT}", headers=headers, json=parameters)
response.raise_for_status()
result = response.json()
print(result)
