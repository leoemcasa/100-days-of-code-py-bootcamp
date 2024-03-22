"""pixela"""

import os
from datetime import datetime
from dotenv import load_dotenv
import requests

load_dotenv()

USERNAME = "bartimaeus"
TOKEN = os.getenv("TOKEN_PIXELA")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_usr_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Criação do usr feita uma vez e mantida como comentário
# response = requests.post(url=pixela_endpoint, json=pixela_usr_param, timeout = 5)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type":  "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Criação do primeito g´rafico comentaod após execução
# https://pixe.la/v1/users/bartimaeus/graphs/graph1.html
# resp = requests.post(url=graph_endpoint, json=graph_config, headers=headers, timeout = 5)
# print(resp.text)

pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "19.74"
}

# Create pixle
# resp = requests.post(url=pixel_create_endpoint, json=pixel_data, headers=headers, timeout=5)
# print(resp.text)

pixel_updt_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240321"
pixel_updt_data = {"quantity": "17.74"}

# updt pixel
# resp = requests.put(url=pixel_updt_endpoint, json=pixel_updt_data, headers=headers, timeout=5)
# print(resp.text)

# del pixel
resp = requests.delete(url=pixel_updt_endpoint, headers=headers, timeout=5)
print(resp.text)
