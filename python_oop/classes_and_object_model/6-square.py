#!/usr/bin/env python3
"""Modulo que define la clase Square."""


class Square:
    """Clase que representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado con size y position validados."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Obtiene la posicion del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posicion validando que sea una tupla valida."""
        message = "position must be a tuple of 2 positive integer"
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(message)
        for coordinate in value:
            if type(coordinate) is not int or coordinate < 0:
                raise TypeError(message)
        self.__position = value

    def area(self):
        """Devuelve el area del cuadrado."""
        return self.__size ** 2

    def __str__(self):
        """Devuelve el cuadrado como cadena, usando position."""
        if self.__size == 0:
            return ""
        x, y = self.__position
        line = " " * x + "#" * self.__size
        return "\n" * y + "\n".join([line] * self.__size)

    def my_print(self):
        """Imprime el cuadrado con el caracter # y su posicion."""
        print(self)
