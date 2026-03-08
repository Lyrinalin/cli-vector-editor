from dataclasses import dataclass
from typing import List

@dataclass
class Shape:
    """Base class for all shapes."""
    pass

@dataclass
class Point(Shape):
    x: float
    y: float

    def __str__(self):
        return f"Point({self.x}, {self.y})"

@dataclass
class Line(Shape):
    x1: float
    y1: float
    x2: float
    y2: float

    def __str__(self):
        return f"Line(start=({self.x1}, {self.y1}), end=({self.x2}, {self.y2}))"

@dataclass
class Circle(Shape):
    x: float
    y: float
    radius: float

    def __str__(self):
        return f"Circle(center=({self.x}, {self.y}), radius={self.radius})"

@dataclass
class Square(Shape):
    x: float
    y: float
    side: float

    def __str__(self):
        return f"Square(center=({self.x}, {self.y}), side={self.side})"
