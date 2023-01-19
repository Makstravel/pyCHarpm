class Point:

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, obj):
        if isinstance(obj, Point):
            dist = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2)**0.5
            return dist
        else:
            print('Передана не точка')


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2) # вернёт 5.0
p1.get_distance(10)

