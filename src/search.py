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
            if choice in forms or choice:
                break
    else:
        choice = next(iter(ALL_POKEMON[name]["forms"]))
    for move in ALL_POKEMON[name]["forms"][choice]["moves"]["scarlet-violet"]:
        print(ALL_MOVES[move])
