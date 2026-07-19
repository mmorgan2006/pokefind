import pprint

from main import ALL_POKEMON,ALL_MOVES

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
    results = []
    for i in ALL_POKEMON:
        for f in ALL_POKEMON[i]["forms"]:
            if ALL_POKEMON[i]["forms"][f]["stats"][stat] >= choice:
                results.append(f.title())
    if len(results) > 0:
        for i in results:
            print(f"> {i}")
    else:
        print("No Pokémon matched the query")
