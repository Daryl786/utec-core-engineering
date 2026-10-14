#!/usr/bin/env python3


def pow(a, b):
    """Devuelve a elevado a la potencia b, sin usar el operador **."""
    result = 1
    if b >= 0:
        for _ in range(b):
            result *= a
    else:
        for _ in range(-b):
            result *= a
        result = 1 / result
    return result
