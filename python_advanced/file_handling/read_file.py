#!/usr/bin/env python3
"""Modulo para leer un archivo de texto UTF-8 e imprimirlo."""


def read_file(filename=""):
    """Lee un archivo UTF-8 y lo imprime en stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
