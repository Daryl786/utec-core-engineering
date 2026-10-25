#!/usr/bin/env python3
"""Modulo para escribir texto en un archivo UTF-8."""


def write_file(filename="", text=""):
    """Escribe text en filename y devuelve los caracteres escritos."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
