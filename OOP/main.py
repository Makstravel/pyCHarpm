class MyCallable:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1

c = MyCallable()
c()
c()
c()
print(c.count)