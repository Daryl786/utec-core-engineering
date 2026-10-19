#!/usr/bin/env python3


def print_matrix_integer(matrix=[[]]):
    """Imprime una matriz de enteros, una fila por linea."""
    for row in matrix:
        print(" ".join("{:d}".format(n) for n in row))
