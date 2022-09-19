# create a vector in python

from typing import Tuple


class Vector:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        Subtract two vectors
        """
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: 'Vector') -> 'Vector':
        """
        Multiply two vectors
        """
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other: 'Vector') -> 'Vector':
        """
        Divide two vectors
        """
        return Vector(self.x / other.x, self.y / other.y)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other: 'Vector') -> bool:
        return self.x == other.x and self.y == other.y


vector = Vector(1, 2)
vector2 = Vector(1, 2)
vector3 = Vector(2, 3)

vector4 = vector.__add__(vector3)
print(vector4)


print(isinstance(vector, Tuple))