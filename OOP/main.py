class MyClass:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, MyClass) and self.x == other.x

a = MyClass(1)
b = MyClass(1)

print(a == b)