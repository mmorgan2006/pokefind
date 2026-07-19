import json
import requests
ALLDATA = dict()
for i in range(1, 1026):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{i}/"
    response = requests.get(url)
    if response.status_code == 200:
        speciesdata = response.json()
        pokemon = dict()
        pokemon["forms"] = dict()
        for v in speciesdata["varieties"]:
            vname = v["pokemon"]["name"]
            if "-gmax" in vname:
                continue
            vurl = v["pokemon"]["url"]
            response = requests.get(vurl)
            if response.status_code == 200:
                vdata = response.json()
                print(vname)
                form = dict()


                form["types"] = list()
                for type in vdata["types"]:
                    form["types"].append(type["type"]["name"])


                form["stats"] = dict()
                for stat in vdata["stats"]:
                    form["stats"][stat["stat"]["name"]] = stat["base_stat"]


                form["abilities"] = vdata["abilities"]


                vmoves = vdata["moves"]
                movepools = dict()
                if "-mega" not in vname:
                    for move in vmoves:
                        movename = move["move"]["name"]
                        for gamedetails in move["version_group_details"]:
                            game = gamedetails["version_group"]["name"]
                            if game not in movepools:
                                movepools[game] = set()
                            movepools[game].add(movename)
                    for k in movepools:
                        movepools[k] = list(movepools[k])
                    form["moves"] = movepools
                pokemon["forms"][vname] = form
            else:
                print(f"Error: {response.status_code} (Pokemon Variation)")
                break

        ALLDATA[speciesdata["name"]] = pokemon
    else:
        print(f"Error: {response.status_code}")
        break
with open("data/allpokemon.json", "w") as file:
    json.dump(ALLDATA, file, indent=4)
