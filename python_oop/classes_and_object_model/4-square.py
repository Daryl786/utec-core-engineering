#!/usr/bin/env python3
"""Modulo que define la clase Square."""


class Square:
    """Clase que representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa el cuadrado usando el setter de size."""
        self.size = size

    @property
    def size(self):
        """Obtiene el tamano del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamano validando tipo y valor."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Devuelve el area del cuadrado."""
        return self.__size ** 2
