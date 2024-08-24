import requests
from datetime import datetime


pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "fira0l"
TOKEN = "thisisasecrettokenforme"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# # response.raise_for_status()
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_conf = {
    "id": "graph2",
    "name": "Workout Graph",
    "unit": "Kg",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_conf, headers=headers)
# print(response.text)

today = datetime.now()
print(today)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Kilos are u today? ")
}
#
# response = requests.post(url=f"{graph_endpoint}/graph2", json=pixel_data, headers=headers)
# print(response.text)

put_data = {
    "quantity": "90.4"
}

response = requests.put(url=f"{graph_endpoint}/graph2/{today.strftime('%Y%m%d')}", json=put_data, headers=headers)
print(response.text)
