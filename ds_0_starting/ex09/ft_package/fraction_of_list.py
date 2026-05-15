def fraction_of_list(data: list[str], target: str) -> float :
    count = 0
    for elem in data:
        count += elem == target
    return count / len(data)