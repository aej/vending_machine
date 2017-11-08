from abc import ABC


class Product(ABC):
    """A generic product object. A product has a price, in pence."""
    price = None

    def __init__(self):
        if self.price is None:
            raise AttributeError


class Candy(Product):
    price = 10


class Snack(Product):
    price = 50


class Nuts(Product):
    price = 90


class Coke(Product):
    price = 25


class Pepsi(Product):
    price = 35


class Soda(Product):
    price = 45
