from math import floor
import json
from textwrap import indent
statnames = ["hp", "attack", "defense", "spattack", "spdefense", "speed"]
with open("data/natures.json", "r") as file:
    natures = json.load(file)
def calc3(pokemon):
    final = {}
    alignment_stats = natures[pokemon["nature"]]

    for stat in pokemon["stats"]:
        if stat == "hp":
            final[stat] = (
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
            final[stat] = (
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
    return final


def calcchamp(pokemon):
    final = {}
    alignment_stats = natures[pokemon["nature"]]
    for stat in pokemon["stats"]:
        if stat == "hp":
            final[stat] = (pokemon["stats"]["hp"]["base"] + pokemon["stats"]["hp"]["points"] + 75)
        else:
            alignment = 1
            if alignment_stats[0] == stat:
                alignment += .1
            if alignment_stats[1] == stat:
                alignment -= .1
            final[stat] = (
                floor((pokemon["stats"][stat]["base"] + pokemon["stats"][stat]["points"] + 20) * alignment)
            )
    return final
