import json

import requests


def main():
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    main()
