from math import floor
import json
statnames = ["hp", "attack", "defense", "spattack", "spdefense", "speed"]
with open("data/natures.json", "r") as file:
    natures = json.load(file)
def calc3():
    final = []
    pokemon = {
        "base": [108, 130, 95, 80, 85, 102],
        "ivs": [24, 12, 30, 16, 23, 5],
        "evs": [74, 190, 91, 48, 84, 23],
        "level": 78,
        "nature": "adamant",
    }
    final.append(
        floor(
            (2 * pokemon["base"][0] + pokemon["ivs"][0] + floor(pokemon["evs"][0] / 4))
            * pokemon["level"]
            / 100
        )
        + pokemon["level"]
        + 10
    )

    for i in range(1, 6):
        alignment = natures[pokemon["nature"]]
        if alignment[0] == statnames[i]:
            alignment = 1.1
        elif alignment[1] == statnames[i]:
            alignment = 0.9
        else:
            alignment = 1
        final.append(
            floor(
                (
                    floor(
                        (
                            2 * pokemon["base"][i]
                            + pokemon["ivs"][i]
                            + floor(pokemon["evs"][i] / 4)
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


def calcchamp():
    final = []
    pokemon = {
        "base": [95, 65, 65, 110, 130, 60],
        "points": [2, 0, 0, 32, 0, 32],
        "nature": "modest",
    }
    final.append(pokemon["base"][0] + pokemon["points"][0] + 75)
    for i in range(1, 6):
        alignment = natures[pokemon["nature"]]
        if alignment[0] == statnames[i]:
            alignment = 1.1
        elif alignment[1] == statnames[i]:
            alignment = 0.9
        else:
            alignment = 1
        final.append(
            floor((pokemon["base"][i] + pokemon["points"][i] + 20) * alignment)
        )
    print(final)


calc3()
