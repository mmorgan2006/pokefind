import load
import search
ALL_POKEMON,ALL_MOVES = load.load_data()
def main():

    while True:
        response = str(input().lower())
        match response:
            case "search" | "1":
                search.search(str(input().lower()))
            case "movepools" | "2":
                search.moves(str(input().lower()))
            case "stop" | "3":
                break
if __name__ == "__main__":
    main()
