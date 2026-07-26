def clamp(number, min, max):
    if number > max:
        return max
    elif number < min:
        return min
    else:
        return number

def format_stat(stat):
    match stat:
        case "hp": return "HP"
        case "attack": return "Atk"
        case "defense": return "Def"
        case "special-attack": return "Sp. Atk"
        case "special-defense": return "Sp. Def"
        case "speed": return "Speed"
