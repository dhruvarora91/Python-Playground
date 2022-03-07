import requests
from datetime import datetime

TOKEN = ""
USERNAME = ""
GRAPH_ID = ""

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}

# response = requests.post(PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_params = {
  "id": GRAPH_ID,
  "name": "Coding",
  "unit": "hours",
  "type": "float",
  "color": "sora",
}

headers = {
  "X-USER-TOKEN": TOKEN
}

# response = requests.post(GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

date_to_update = datetime().now().strftime("%Y%m%d")

pixel_params = {
  "date": date_to_update,
  "quantity": "5",
}

# response = requests.post(PIXEL_CREATION_ENDPOINT, json=pixel_params, headers=headers)
# print(response.text)

PIXEL_UPDATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"

pixel_update_params = {
  "quantity": "5"
}

# response = requests.put(PIXEL_UPDATION_ENDPOINT, json=pixel_update_params, headers=headers)
# print(response.text)

PIXEL_DELETION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"

# response = requests.delete(PIXEL_DELETION_ENDPOINT, headers=headers)
# print(response.text)
