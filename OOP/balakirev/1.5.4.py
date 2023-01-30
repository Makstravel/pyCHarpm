class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        line = (self.a, self.b, self.c)
        if type(line) not in (int, float) or line<=0:
            return 1
        if sum(self.a, self.b) > self.c or sum(self.b, self.c) > self.a or sum(self.a, self.c) > self.b:
            return 2
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
        

