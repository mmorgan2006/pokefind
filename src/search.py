import pprint
import copy
from main import ALL_POKEMON,ALL_MOVES
import statsearch
def search(name):
    pprint.pprint(ALL_POKEMON[name])


def moves(name):
    forms = list()
    blocked = ["-mega", "-g-max", "-terastal", "-stellar"]
    for form in ALL_POKEMON[name]["forms"]:
        if all(x not in form.lower() for x in blocked):
            forms.append(form)
    if len(forms) > 1:
        while True:
            print("Please choose a form")
            for form_name in forms:
                print(f"> {form_name.title()}")
            choice = input()
            choice = choice.replace(" ","-")
            if choice in forms:
                break
    else:
        choice = next(iter(ALL_POKEMON[name]["forms"]))
    for move in ALL_POKEMON[name]["forms"][choice]["moves"]["scarlet-violet"]:
        print(ALL_MOVES[move])



def search_min_stat():
    valid = ["hp", "attack", "defense", "special-attack","special-defense","speed","spattack","spdefense","sp-attack","sp-defense","atk","def","sp-atk","spatk","sp-def","spdef","spe"]
    while True:
        print("Please choose a stat")
        choice = input()
        choice = choice.replace(" ","-")
        choice = choice.replace(".","")
        if choice in valid:
            break
    match choice:
        case "atk":
            choice = "attack"
        case "def":
            choice = "defense"
        case "spattack":
            choice = "special-attack"
        case "spatk":
            choice = "special-attack"
        case "sp-atk":
            choice = "special-attack"
        case "spdefense":
            choice = "special-defense"
        case "spdef":
            choice = "special-defense"
        case "sp-def":
            choice = "special-defense"
        case "spe":
            choice = "speed"
    stat = choice
    while True:
        print("Choose the minimum value")
        choice = input()
        try:
            choice = int(choice)
            break
        except Exception:
            pass
    results = statsearch.search_min(ALL_POKEMON, stat, choice)
    if len(results) > 0:
        for i in results:
            print(f"> {i}")
    else:
        print("No Pokémon matched the query")



def search_multiple():
    validpokemon = ALL_POKEMON
    queue = dict()
    valid = ["hp", "attack", "defense", "special-attack","special-defense","speed","spattack","spdefense","sp-attack","sp-defense","atk","def","sp-atk","spatk","sp-def","spdef","spe"]
    while True:
        while True:
            print("Please choose a stat")
            choice = input()
            choice = choice.replace(" ","-")
            choice = choice.replace(".","")
            if choice in valid:
                break
            elif choice == "end" or choice == "0":
                break
        match choice:
            case "atk":
                choice = "attack"
            case "def":
                choice = "defense"
            case "spattack":
                choice = "special-attack"
            case "spatk":
                choice = "special-attack"
            case "sp-atk":
                choice = "special-attack"
            case "spdefense":
                choice = "special-defense"
            case "spdef":
                choice = "special-defense"
            case "sp-def":
                choice = "special-defense"
            case "spe":
                choice = "speed"
        stat = choice
        while True:
            if choice == "end" or choice == "0":
                break
            print("Choose the minimum value")
            choice = input()
            try:
                choice = int(choice)
                if choice > 0:
                    queue[stat] = choice
                choice = -1
                break
            except Exception:
                pass
        if choice == "end" or choice == "0":
            break
    for q in queue:

        newvalidpokemon = copy.deepcopy(validpokemon)
        results = statsearch.search_min(validpokemon, q, queue[q])
        for i in validpokemon:
            for f in validpokemon[i]["forms"]:
                if f.title() not in results:
                    newvalidpokemon[i]["forms"].pop(f)
            if len(newvalidpokemon[i]["forms"]) == 0:
                newvalidpokemon.pop(i)
        validpokemon = newvalidpokemon
    results = []
    for i in validpokemon:
        for f in validpokemon[i]["forms"]:
            print(f"> {f.title()}")
