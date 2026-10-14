#!/usr/bin/env python3


def print_last_digit(number):
    """Imprime el último dígito de number y lo devuelve."""
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last

