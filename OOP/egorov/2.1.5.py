class Constructor:
    def add_atribute(self, name, namex):
        setattr(self, name, namex)
    def display(self):
        print(self.__dict__)


obj1 = Constructor()
obj1.display()
obj1.add_atribute('color', 'red')
obj1.add_atribute('width', 20)
obj1.display()

