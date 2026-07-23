import json
import requests


def pokemon():
    with open("data/allmoves.json", "r") as file:
        ALL_MOVES = json.load(file)
    with open("data/allabilities.json", "r") as file:
        ALL_ABILITIES = json.load(file)

    ALLDATA = dict()
    blocked = ["-gmax","-cap","-rock-star","-belle","-pop-star","-phd","-libre","-cosplay","-totem","-power-construct","-battle-bond","minior","-busted","-original","-gulping","-gorging","-dada","-build","-mode"]
    for i in range(1, 1026):
        url = f"https://pokeapi.co/api/v2/pokemon-species/{i}/"
        response = requests.get(url)
        if response.status_code == 200:
            speciesdata = response.json()
            pokemon = dict()
            pokemon["forms"] = dict()
            for v in speciesdata["varieties"]:
                vname = v["pokemon"]["name"]
                if any(str(item).lower() in vname.lower() for item in blocked):
                    if vname not in ["minior-red","minior-red-meteor"]:
                        continue
                vurl = v["pokemon"]["url"]
                response = requests.get(vurl)
                if vname == "minior-red":
                    vname = "minior-core"
                if vname == "minior-red-meteor":
                    vname = "minior-meteor"
                if vname == "pyroar-male":
                    vname = "pyroar"
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

                    form["abilities"] = []
                    for a in vdata["abilities"]:
                        form["abilities"].append({"name": a["ability"]["name"], "slot": a["slot"]})
                        ALL_ABILITIES[a["ability"]["name"]]["pokemon"].append(vname)


                    vmoves = vdata["moves"]
                    movepools = dict()
                    for move in vmoves:
                        movename = move["move"]["name"]
                        for gamedetails in move["version_group_details"]:
                            game = gamedetails["version_group"]["name"]
                            if game not in movepools:
                                movepools[game] = set()
                            if game not in ALL_MOVES[movename]["learned_by_pokemon"]:
                                ALL_MOVES[movename]["learned_by_pokemon"][game] = list()
                            movepools[game].add(movename)
                            ALL_MOVES[movename]["learned_by_pokemon"][game].append(vname)


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
    with open("data/allmoves.json", "w") as file:
        json.dump(ALL_MOVES, file, indent=4)
    with open("data/allabilities.json", "w") as file:
        json.dump(ALL_ABILITIES, file, indent=4)
