import requests
from datetime import *
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "fresnel"
TOKEN = "hiafnihhsdbvioubndsuh"
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN,
}
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# quantity = input("Enter the amount of cycling done today: ")
today = datetime.now()
print(today.strftime("%Y%m%d"))
graph_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.5"
}
date = today.strftime("%Y%m%d")
# response = requests.post(url=graph_update_endpoint, json=graph_update, headers=headers)
# print(response.text)
graph_up_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
# graph_up = {
#     "quantity": quantity,
# }
# response = requests.put(url=graph_up_endpoint, json=graph_up, headers=headers)
# print(response.text)

response = requests.delete(url=graph_up_endpoint, headers=headers)
print(response.text)