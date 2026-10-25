#!/usr/bin/env python3
"""Modulo para anadir texto al final de un archivo UTF-8."""


def append_write(filename="", text=""):
    """Anade text al final de filename y devuelve los caracteres."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
