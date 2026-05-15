def count_in_list(data: list[str], target: str) -> int :
    count = 0
    for elem in data:
        count += elem == target
    return count