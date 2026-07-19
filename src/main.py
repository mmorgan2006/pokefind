import getpokemon

def main():

    while True:
        response = str(input().lower())
        match response:
            case "search" | "1":
                response = str(input().lower())
                getpokemon.get(response)
            case "stop" | "2":
                break
if __name__ == "__main__":
    main()
