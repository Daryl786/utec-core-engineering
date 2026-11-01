#!/usr/bin/env python3
"""Modulo que define la clase Rectangle."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Clase que representa un rectangulo y hereda de BaseGeometry."""

    def __init__(self, width, height):
        """Inicializa el rectangulo validando width y height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Devuelve el area del rectangulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve la descripcion [Rectangle] width/height."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
