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
