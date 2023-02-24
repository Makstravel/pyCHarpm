class Fruit:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.price == other
        elif isinstance(other, Fruit):
            return self.price == other

    def __ne__(self, other):
        if isinstance(other, (int, float)):
            return self.price != other
        elif isinstance(other, Fruit):
            return self.price != other

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.price < other
        elif isinstance(other, Fruit):
            return self.price < other

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return self.price <= other
        elif isinstance(other, Fruit):
            return self.price <= other

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.price > other
        elif isinstance(other, Fruit):
            return self.price > other

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return self.price >= other
        elif isinstance(other, Fruit):
            return self.price >= other


apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)

assert banana > 1.2
assert banana >= 1.2
assert not banana == 1.2
assert banana != 1.2
assert not banana < 1.2
assert not banana <= 1.2

assert not apple > orange
assert not apple >= orange
assert not apple == orange
assert apple != orange
assert apple < orange
assert apple <= orange

assert orange == lime
assert not orange != lime
assert not orange > lime
assert not orange < lime
assert orange <= lime
assert orange >= lime
print('Good')