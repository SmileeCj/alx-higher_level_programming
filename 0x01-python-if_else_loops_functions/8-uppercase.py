#!/usr/bin/python3
def uppercase(str):
    for i in range(0,len(str)):

        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            c = f"{ord(str[i]) - 32:c}"
        else:
            c = f"{ord(str[i]):c}"

        print(f"{c}", end="")
    
        if i == len(str) - 1:
            print("\n")
