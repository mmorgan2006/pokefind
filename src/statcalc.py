from math import floor
import json
statnames = ["hp", "attack", "defense", "spattack", "spdefense", "speed"]
with open("data/natures.json", "r") as file:
    natures = json.load(file)
def calc3(pokemon):
    final = []
    pokemon = {
        "nature": "quirky",
        "level": 78,
        "stats":{
            "hp": {
                "base": 108,
                "iv": 24,
                "ev": 74
            },
            "attack": {
                "base": 130,
                "iv": 12,
                "ev": 190
            },
            "defense": {
                "base": 95,
                "iv": 30,
                "ev": 91
            },
            "special-attack": {
                "base": 80,
                "iv": 16,
                "ev": 48
            },
            "special-defense": {
                "base": 85,
                "iv": 23,
                "ev": 84
            },
            "speed": {
                "base": 102,
                "iv": 5,
                "ev": 23
            }
        }
    }
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
