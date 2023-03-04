from dataclasses import dataclass

@dataclass
class Point:
    x: (int, float)
    y: int


point1 = Point(5.6, 7)
point2 = Point(-10, 12)
print(point1, point2, sep='\n')