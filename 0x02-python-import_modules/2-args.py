#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1

    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(n - 1))
    for x in range(1, n):
        print("{}: {}".format(x, sys.argv[x]))
