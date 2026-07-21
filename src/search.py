import pprint
import copy
import statsearch
from load import ALL_MOVES,ALL_POKEMON
def search(name):
    pprint.pprint(ALL_POKEMON[name])


def search_move(move,validpokemon,game):
    newvalidpokemon = copy.deepcopy(validpokemon)
    results = set()
    game = game.lower()
    move = move.replace(" ","-").lower()
    for i in validpokemon:
        for f in validpokemon[i]["forms"]:
            if validpokemon[i]["forms"][f]["moves"].get(game) is not None:
                if move in validpokemon[i]["forms"][f]["moves"][game]:
                    results.add(f)
    for i in validpokemon:
        for f in validpokemon[i]["forms"]:
            if f not in results:
                newvalidpokemon[i]["forms"].pop(f)
        if len(newvalidpokemon[i]["forms"]) == 0:
            newvalidpokemon.pop(i)
    return newvalidpokemon




def search_stats(queue,validpokemon):
    for q in queue:

        newvalidpokemon = copy.deepcopy(validpokemon)

        mode = queue[q]["mode"]
        match mode:
            case "minimum":
                results = statsearch.search_min(validpokemon,q,queue[q]["value"])
            case "exact":
                results = statsearch.search_exact(validpokemon,q,queue[q]["value"])
            case "maximum":
                results = statsearch.search_max(validpokemon,q,queue[q]["value"])
            case _:
                results = []
        for i in validpokemon:
            for f in validpokemon[i]["forms"]:
                if f.title() not in results:
                    newvalidpokemon[i]["forms"].pop(f)
            if len(newvalidpokemon[i]["forms"]) == 0:
                newvalidpokemon.pop(i)
        validpokemon = newvalidpokemon
    results = []
    if len(validpokemon) > 0:
        for i in validpokemon:
            for f in validpokemon[i]["forms"]:
                results.append(f"> {f.title()}")
    else:
        print("No Pokémon matched the query")
    return results


def search_ability(ability,validpokemon):
    newvalidpokemon = copy.deepcopy(validpokemon)
    ability = ability.replace(" ","-")
    ability = ability.lower()
    results = []
    for i in validpokemon:
        for form in validpokemon[i]["forms"]:
            for current_ability in validpokemon[i]["forms"][form]["abilities"]:
                if ability == current_ability["name"]:
                    results.append(form)
    for i in validpokemon:
        for f in validpokemon[i]["forms"]:
            if f not in results:
                newvalidpokemon[i]["forms"].pop(f)
        if len(newvalidpokemon[i]["forms"]) == 0:
            newvalidpokemon.pop(i)
    return newvalidpokemon


def search_type(type,validpokemon):
    results = []
    newvalidpokemon = copy.deepcopy(validpokemon)
    for i in validpokemon:
        for form in validpokemon[i]["forms"]:
            if type in validpokemon[i]["forms"][form]["types"]:
                results.append(form)
    for i in validpokemon:
        for f in validpokemon[i]["forms"]:
            if f not in results:
                newvalidpokemon[i]["forms"].pop(f)
        if len(newvalidpokemon[i]["forms"]) == 0:
            newvalidpokemon.pop(i)
    return newvalidpokemon
