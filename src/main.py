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
            case "stat" | "3":
                search.search_min_stat()
            case "multi" | "4":
                search.search_multiple()
            case "stop" | "5":
                break
if __name__ == "__main__":
    main()
