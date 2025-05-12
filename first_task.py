import math
from abc import ABC, abstractmethod
from typing import Union

class Shape(ABC):
  @abstractmethod
  def area(self) -> float:
    pass

class Circle(Shape):
  def __init__(self, radius: float):
    if radius <= 0:
      raise ValueError('Радиус должен быть положительным')
    self.radius = radius

  def area(self) -> float:
    return math.pi * self.radius ** 2

class Triangle(Shape):
  def __init__(self, a: float, b: float, c: float):
    sides = [a, b, c]
    if any(side <= 0 for side in sides):
      raise ValueError('Все строны должны быть положительными')
    sides.sort()
    if sides[2] >= sides[0] + sides[1]:
      raise ValueError('Нарушено неравенство треугольника')
    self.a = a
    self.b = b
    self.c = c

  def area(self) -> float:
    s = (self.a + self.b + self.c) / 2
    return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

  def is_right_angled(self, tolerance: float = 1e-6) -> bool:
    sides = [self.a, self.b, self.c]
    sides.sort()
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < tolerance

def calculate_area(shape: Union[Circle, Triangle]) -> float:
  return shape.area()

# Пример добавления новой фигуры (прямоугольник)
class Rectangle(Shape):
  def __init__(self, width: float, height: float):
    if width <= 0 or height <= 0:
      raise ValueError('Ширина и высота должны быть положительными.')
    self.width = width
    self.height = height

  def area(self) -> float:
    return self.width * self.height
