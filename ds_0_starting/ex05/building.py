import sys


def is_punctuation(c) -> bool:
    """Returns true it c is a punctuation mark"""
    return c.isprintable() and not c.isalnum() and not c.isspace()


def stats(data: str):
    """
    Count and print upper, lower, punctuation, spaces and digits in data.

    Parameters:
        data (str): The string to made stats from.

    Returns:
        Nothing

    Raises:
        Nothing

    """
    upp = 0
    low = 0
    pun = 0
    spa = 0
    dig = 0
    num = len(data)
    for char in data:
        upp += char.isupper()
        low += char.islower()
        pun += is_punctuation(char)
        spa += char.isspace()
        dig += char.isdigit()
    print(f"The text contains {num} characters:")
    print(upp, "upper letters")
    print(low, "lower letters")
    print(pun, "punctuation marks")
    print(spa, "spaces")
    print(dig, "digits")


def main():
    """Entry point: parse args and run stats"""
    sys.tracebacklimit = 0
    argc = len(sys.argv)

    if argc > 2:
        raise AssertionError("Too many arguments") from None

    if argc == 1 or len(sys.argv[1]) == 0:
        print("What is the text to count?")
        stats(sys.stdin.readline())
    else:
        stats(sys.argv[1])


if __name__ == "__main__":
    main()
