#!/usr/bin/env python3
"""Modulo que define la clase Square."""


class Square:
    """Clase que representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa el cuadrado validando su tamano."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Devuelve el area del cuadrado."""
        return self.__size ** 2
