class Counter:

    def start_from(self, name=0):
        self.name= name

    def increment(self):
        self.name +=1

    def display(self):
        print(f'Текущее значение счетчика ={self.name}')
    def reset(self):
        self.name = 0

c1 = Counter()
c1.start_from()
c1.increment()
c1.display()
c1.increment()
c1.display()
c1.reset()
c1.display()

