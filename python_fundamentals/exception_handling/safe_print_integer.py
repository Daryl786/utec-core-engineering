#!/usr/bin/env python3


def safe_print_integer(value):
    """Imprime value si es entero y devuelve True; si no, False."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
