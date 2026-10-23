#!/usr/bin/env python3


def read_file(filename=""):
    """Lee un archivo UTF-8 y lo imprime en stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
