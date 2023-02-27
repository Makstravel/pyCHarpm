class Animal:
    pass


class Dog(Animal):
    pass


class Fish:
    pass

print(issubclass(Animal, Dog))
print(issubclass(Dog, Animal))
print(issubclass(Fish, Dog))
print(issubclass(Dog, Fish))