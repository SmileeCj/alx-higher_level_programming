#!/usr/bin/python3
def print_last_digit(number):
    if number > 10:
        n = abs(number % 10)
    else:
        n = abs(number % -10)

    print("{:d}".format(n), end="")
    return n
