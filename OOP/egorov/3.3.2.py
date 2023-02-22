class Order:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __add__(self, other):
        ncart = self.cart + [other]
        return Order(ncart, self.customer)

    def __radd__(self, other):
        return self+other

    def __sub__(self, other):
        if isinstance(other, Order):
            return self.cart - other.cart
        if isinstance(other, str):
            return self.cart - other
        raise NotImplemented

    def __rsub__(self, other):
        return self + other


# Ниже код для проверки методов класса Order

order = Order(['banana', 'apple'], 'Гена Букин')

order_2 = order + 'orange'
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']

order = 'mango' + order
assert order.cart == ['mango', 'banana', 'apple']
order = 'ice cream' + order
assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

order = order - 'banana'
assert order.cart == ['ice cream', 'mango', 'apple']

order = order - 'mango'
assert order.cart == ['ice cream', 'apple']
order = 'lime' - order
assert order.cart == ['ice cream', 'apple']
print('Good')