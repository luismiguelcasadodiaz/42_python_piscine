def count_in_list(data: list[str], target: str) -> int:
    """Count the number of occurrences of target in data."""
    count = 0
    for elem in data:
        count += elem == target
    return count
