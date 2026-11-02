#!/usr/bin/env python3
"""Modulo que define la clase Square."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Clase que representa un cuadrado y hereda de Rectangle."""

    def __init__(self, size):
        """Inicializa el cuadrado validando size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Devuelve el area del cuadrado."""
        return self.__size ** 2

    def __str__(self):
        """Devuelve la descripcion [Square] width/height."""
        return "[Square] {}/{}".format(self.__size, self.__size)
