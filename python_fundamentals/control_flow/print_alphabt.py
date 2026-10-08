#!/usr/bin/env python3
result = ""
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter != "e" and letter != "q":
        result += letter
print("{}".format(result), end="")
