import sys
sys.path.append("../ex05")
from building import is_punctuation  # noqa: E402
from ft_filter import ft_filter      # noqa: E402


def goodchar(c) -> bool:
    return not (is_punctuation(c) or not c.isprintable())


def main():
    assert len(sys.argv) == 3 and sys.argv[2].isdigit(), \
        "the arguments are bad"
    cleanstring = "".join(
        [c for c in sys.argv[1].encode().decode('unicode_escape')
         if goodchar(c)])
    print(list(ft_filter(lambda x: len(x) >= int(sys.argv[2]),
                         cleanstring.split())))


if __name__ == "__main__":
    sys.tracebacklimit = 0
    main()
