from math import floor
import json
statnames = ["hp", "attack", "defense", "spattack", "spdefense", "speed"]
with open("data/natures.json", "r") as file:
    natures = json.load(file)
def calc3(pokemon):
    final = []
    alignment_stats = natures[pokemon["nature"]]

    for stat in pokemon["stats"]:
        if stat == "hp":
            final.append(
                floor(
                    (2 * pokemon["stats"][stat]["base"] + pokemon["stats"][stat]["iv"] + floor(pokemon["stats"][stat]["ev"] / 4))
                    * pokemon["level"]
                    / 100
                )
                + pokemon["level"]
                + 10
            )
        else:
            alignment = 1
            if alignment_stats[0] == stat:
                alignment += .1
            if alignment_stats[1] == stat:
                alignment -= .1
            final.append(
                    floor(
                        (
                            floor(
                                (
                                    2 * pokemon["stats"][stat]["base"]
                                    + pokemon["stats"][stat]["iv"]
                                    + floor(pokemon["stats"][stat]["ev"] / 4)
                                )
                                * pokemon["level"]
                                / 100
                            )
                            + 5
                        )
                        * alignment
                    )
                )
    print(final)


def calcchamp(pokemon):
    pokemon = {
        "nature": "modest",
        "stats":{
            "hp": {
                "base": 95,
                "points": 2,
            },
            "attack": {
                "base": 65,
                "points": 0,
            },
            "defense": {
                "base": 65,
                "points": 0,
            },
            "special-attack": {
                "base": 110,
                "points": 32,
            },
            "special-defense": {
                "base": 130,
                "points": 0,
            },
            "speed": {
                "base": 60,
                "points": 32,
            }
        }
    }
    final = []
    alignment_stats = natures[pokemon["nature"]]
    for stat in pokemon["stats"]:
        if stat == "hp":
            final.append(pokemon["stats"]["hp"]["base"] + pokemon["stats"]["hp"]["points"] + 75)
        else:
            alignment = 1
            if alignment_stats[0] == stat:
                alignment += .1
            if alignment_stats[1] == stat:
                alignment -= .1
            final.append(
                floor((pokemon["stats"][stat]["base"] + pokemon["stats"][stat]["points"] + 20) * alignment)
            )
    print(final)
