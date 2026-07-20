import json
import requests
def abilities():
    ABILITIES = dict()
    for i in range(1, 1000):
        while True:
            try:
                response = requests.get(f"https://pokeapi.co/api/v2/ability/{i}/")
                break
            except Exception:
                print("pass")
                pass

        if response.status_code == 200:
            data = response.json()

            aname = data["name"]
            realname = data["names"]
            for lang in realname:
                if lang["language"]["name"] == "en":
                    realname = lang["name"]

            ABILITIES[aname] = dict()
            ABILITIES[aname]["name"] = realname
            ABILITIES[aname]["pokemon"] = []
            print(f"{aname}: {realname}")
        else:
            print(f"Stopped at {i}")
            break
    with open("data/allabilities.json", "w") as file:
        json.dump(ABILITIES, file, indent=4)
