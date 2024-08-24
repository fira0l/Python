import requests

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
#
# response = requests.post(url=graph_endpoint, json=graph_conf, headers=headers)
# print(response.text)

pixel_data = {
    "date": "20240824",
    "quantity": "89.4"
}

response = requests.post(url=f"{graph_endpoint}/graph2", json=pixel_data, headers=headers)
print(response.text)

