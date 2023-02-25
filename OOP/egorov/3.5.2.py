class Quadrilateral:

    def __init__(self, width, height=None):
        self.width = width
        self.height = (width if height is None else height)

    def __str__(self):
        if self.width == self.height:
            return f'Куб размером {self.width}х{self.height}'
        else:
            return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height


q1 = Quadrilateral(10)
print(q1)
assert q1.height == 10
assert q1.width == 10
assert bool(q1)
assert q1.__str__() == "Куб размером 10х10"
assert isinstance(q1, Quadrilateral)

q2 = Quadrilateral(3, 5)
print(q2)
assert q2.__str__() == "Прямоугольник размером 3х5"
assert q2 != True
assert isinstance(q2, Quadrilateral)

q3 = Quadrilateral(4, 7)
print(q3)
assert not q3 == True
assert q3.__str__() == "Прямоугольник размером 4х7"
assert isinstance(q3, Quadrilateral)