def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()
    match unit.lower():
        case "packets":
            print(seed, "seeds:", quantity, "packets available")
        case "grams":
            print(seed, "seeds:", quantity, "grams total")
        case "area":
            print(seed, "seeds: covers", quantity, "square meters")
        case _:
            print("Unknown unit type")
