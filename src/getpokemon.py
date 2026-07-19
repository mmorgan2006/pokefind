import json

import requests


def get(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))
        print(data["icons"])
    else:
        print(f"Error: {response.status_code}")
