#!/usr/bin/env python3
"""Modulo que define la clase Rectangle."""


class Rectangle:
    """Clase que representa un rectangulo."""

    def __init__(self, width=0, height=0):
        """Inicializa el rectangulo con width y height validados."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtiene el ancho del rectangulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece el ancho validando tipo y valor."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Obtiene el alto del rectangulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece el alto validando tipo y valor."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
