#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):

        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            c = "{:c}".format(ord(str[i]) - 32)
        else:
            c = "{:c}".format(ord(str[i]))

        print(f"{c}", end="")

    print("")
