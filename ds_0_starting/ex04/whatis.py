import sys
sys.tracebacklimit = 0

if len(sys.argv) == 1:
    sys.exit(0)

assert len(sys.argv) == 2 , "more than one argument is provided"
try:
    n = int(sys.argv[1])
    print("I'm Even." if (n % 2 ) == 0 else "I'm Odd.")
except ValueError:
    raise AssertionError("argument is not an integer") from None

    

