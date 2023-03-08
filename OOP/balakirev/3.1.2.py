class Product:
    _id_instanse = 1
    attrs = {'name': (str,), 'weight': (int, float), 'price': (int, float)}

    def __init__(self, name, weight, price):
        self.id = Product._id_instanse
        Product._id_instanse += 1

        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key in self.attrs and type(value) in self.attrs[key]:
            if (key == 'price' or key == 'weight') and value <=0:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key in self.attrs:
            raise TypeError("Неверный тип присваиваемых данных.")

        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


class Shop:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
