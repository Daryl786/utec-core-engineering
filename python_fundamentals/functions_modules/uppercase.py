#!/usr/bin/env python3


def uppercase(str):
    """Imprime la cadena en mayúsculas, seguida de una nueva línea."""
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
