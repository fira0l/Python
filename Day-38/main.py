import requests


USER_SID = "NUTRITIONIX_SID"
NUT_API_KEY = "NUTRITIONIX_API_KEY"
HOST_DOMAIN = "https://trackapi.nutritionix.com"
ENDPOINT = "/v2/natural/exercise"
GOOGLE_SHEETS_URL = "https://api.sheety.co/adacce6626dffa15bf442c3d9acb17c4/workoutsData/workouts"


WEIGHT = 87
HEIGHT = 168.5
AGE = 22

user_query = input("What Kind of Exercise did u perform? ")

headers = {
    "x-app-id": USER_SID,
    "x-app-key": NUT_API_KEY
}

parameters = {
    "query": user_query,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}


response = requests.post(url=f"{HOST_DOMAIN}{ENDPOINT}", headers=headers, json=parameters)
response.raise_for_status()
result = response.json()["exercises"][0]["name"]
print(result)


