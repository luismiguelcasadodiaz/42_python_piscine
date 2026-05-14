import sys

NESTED_MORSE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/'
}


def main(data):
    """Print the data's Morse code translation separated by spaces."""
    n = len(data)
    for i in range(0, n - 1):
        print(NESTED_MORSE[data[i]], ' ', end="")
    print(NESTED_MORSE[data[n - 1]])


if __name__ == "__main__":
    sys.tracebacklimit = 0
    assert len(sys.argv) == 2, "the arguments are bad"
    assert all(c.isalnum() or c.isspace()
               for c in sys.argv[1]), "the arguments are bad"
    main(sys.argv[1].upper())
