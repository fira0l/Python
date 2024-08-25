import requests


USER_SID = "105f4e75"
API_KEY = "f37315f4d36bc5d593199639e2a31426"
HOST_DOMAIN = "https://trackapi.nutritionix.com"
ENDPOINT = "/v2/natural/nutrients"


headers = {
    "x-app-id": USER_SID,
    "x-app-key": API_KEY
}

parameters = {
    "query": None,


}
