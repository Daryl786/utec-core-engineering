#!/usr/bin/env python3
"""Modulo de demostracion de herencia y polimorfismo."""


class Animal:
    """Clase padre con el comportamiento comun de los animales."""

    def speak(self):
        """Devuelve el sonido generico de un animal."""
        return "Some sound"


class Dog(Animal):
    """Clase hija que representa a un perro."""

    def speak(self):
        """Devuelve el sonido de un perro."""
        return "Woof"


class Cat(Animal):
    """Clase hija que representa a un gato."""

    def speak(self):
        """Devuelve el sonido de un gato."""
        return "Meow"


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    print(dog.speak())
    print(cat.speak())

    animals = [Dog(), Cat(), Dog()]
    for animal in animals:
        print(animal.speak())

    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(issubclass(Dog, Animal))
