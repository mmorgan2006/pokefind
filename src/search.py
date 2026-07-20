import pprint
import copy
import statsearch
import load
ALL_POKEMON,ALL_MOVES,ALL_ABILITIES = load.load_data()
def search(name):
    pprint.pprint(ALL_POKEMON[name])


def moves(name):
    forms = list()
    blocked = ["-mega", "-g-max", "-terastal", "-stellar", "-eternamax"]
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


def search_stats(queue):
    validpokemon = ALL_POKEMON
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
                print(f"> {f.title()}")
                results.append(f"> {f.title()}")
    else:
        print("No Pokémon matched the query")
    return results
