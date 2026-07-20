import json
import sys
import os

def resource_path(relative_path):
    # If running as a PyInstaller EXE
    if hasattr(sys, '_MEIPASS'):
        base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
        return os.path.join(base_path, relative_path)

    # If running normally (IDE, terminal)
    return os.path.join(os.path.abspath("."), relative_path)

def load_data():
    pokemon_path = resource_path("data/allpokemon.json")
    moves_path = resource_path("data/allmoves.json")
    abilities_path = resource_path("data/allabilities.json")

    with open(pokemon_path, "r") as file:
        ALL_POKEMON = json.load(file)
    with open(moves_path, "r") as file:
        ALL_MOVES = json.load(file)
    with open(abilities_path, "r") as file:
        ALL_ABILITIES = json.load(file)

    return ALL_POKEMON, ALL_MOVES, ALL_ABILITIES
