import json
import requests

def moves():
    MOVES = dict()
    for i in range(1, 1000):
        while True:
            try:
                response = requests.get(f"https://pokeapi.co/api/v2/move/{i}/")
                break
            except Exception:
                print("pass")
                pass

        if response.status_code == 200:
            data = response.json()

            mname = data["name"]
            realname = data["names"]
            for lang in realname:
                if lang["language"]["name"] == "en":
                    realname = lang["name"]

            MOVES[mname] = dict()
            MOVES[mname]["name"] = realname
            MOVES[mname]["type"] = data["type"]["name"]
            MOVES[mname]["learned_by_pokemon"] = dict()
            print(f"{mname}: {realname}")
        else:
            print(f"Stopped at {i}")
            break
    with open("data/allmoves.json", "w") as file:
        json.dump(MOVES, file, indent=4)
