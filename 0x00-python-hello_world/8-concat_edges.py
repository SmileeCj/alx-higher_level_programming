#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split(',')[2][1:29] + str.split(maxsplit=12)[12][:5] + str.split()[0]
print(str)
