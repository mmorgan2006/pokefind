import json

def load_data():
    with open("data/allpokemon.json", "r") as file:
        ALL_POKEMON = json.load(file)
    with open("data/allmoves.json", "r") as file:
        ALL_MOVES = json.load(file)
    return ALL_POKEMON,ALL_MOVES
