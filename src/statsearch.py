def search_min(pokemondata,stat, min):
    results = []
    for i in pokemondata:
        for f in pokemondata[i]["forms"]:
            if pokemondata[i]["forms"][f]["stats"][stat] >= min:
                results.append(f.title())
    return results

def search_max(pokemondata,stat, min):
    results = []
    for i in pokemondata:
        for f in pokemondata[i]["forms"]:
            if pokemondata[i]["forms"][f]["stats"][stat] <= min:
                results.append(f.title())
    return results

def search_exact(pokemondata,stat, min):
    results = []
    for i in pokemondata:
        for f in pokemondata[i]["forms"]:
            if pokemondata[i]["forms"][f]["stats"][stat] == min:
                results.append(f.title())
    return results
