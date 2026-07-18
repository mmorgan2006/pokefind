import getpokemon

def main():
    response = str(input().lower())
    getpokemon.get(response)

if __name__ == "__main__":
    main()
