from change import calculate_change
from exceptions import NoStockException, InvalidMoneyTypes, MoneyTypeNotInStock, InvalidMoneyBox


class VendingMachine:
    """A vending machine object holds products and accepts different
    types of money. The vending machine tracks how many of each type of product
    is inside it. Each vending machine must have a money_box declared."""

    def __init__(self, products, money_box):
        self.products = products
        self.money_box = money_box

        if not isinstance(self.money_box, MoneyBox):
            raise InvalidMoneyBox("A avalid money box has not been declared")

    def add_product(self, product):
        """A product is added to the vending machine."""
        self.products.append(product)

    def remove_product(self, product):
        """A product is removed from the vending machine."""
        if not type(product) in self.product_types():
            raise NoStockException("Stock has run out")

        product_to_remove = self.get_product_of_type(type(product))
        self.products.remove(product_to_remove)

    def add_to_money_stock(self, money_type):
        """Instruct the money box to add new money amount."""
        try:
            self.money_box.add_to_money_store(money_type)
        except InvalidMoneyTypes as e:
            raise e

    def remove_from_money_stock(self, money_type):
        """Instruct the money box to remove money amount."""
        try:
            self.money_box.remove_from_money_store(money_type)
        except MoneyTypeNotInStock as e:
            raise e

    def product_types(self):
        """Return all the product types in the vending machine"""
        return set(p.__class__ for p in self.products)

    def get_product_of_type(self, product_type):
        """Get a product of a particular type from a list of products."""
        for p in self.products:
            if p.__class__ is product_type:
                return p


class MoneyBox:
    """A money box is a container that holds money. It knows about the money inside it, is able to add or remove money
    to itself. It only accepts the predefined valid money types."""

    def __init__(self, money_store, valid_money):
        self.money_store = money_store
        self.valid_money = valid_money
        self._check_money_is_valid(money_store)

    @property
    def valid_money_types(self):
        """Return a set of valid money types"""
        return {m for m in self.valid_money}

    @property
    def money_store_types(self):
        """Return the a set of money types within the money store."""
        return {m.__class__ for m in self.money_store}

    def _check_money_is_valid(self, money_store):
        """Check that the money in the money box is valid when the money box is initially created."""
        if not len(money_store) == 0:
            for m in money_store:
                if m.__class__ not in self.valid_money_types:
                    raise InvalidMoneyTypes("Money type not allowed in money box")

    def add_to_money_store(self, money_type):
        """Add a money amount to the money stock."""
        self._check_money_is_valid([money_type])
        self.money_store.append(money_type)

    def remove_from_money_store(self, money_type):
        """Take away money amount from the money stock, firstly checking
        whether the money type exists in the money stock."""
        if len(self.money_store) == 0 or money_type.__class__ not in self.money_store_types:
            raise MoneyTypeNotInStock("There are no coins or notes of this amount in the machine")

        for m in self.money_store:
            if m.__class__ == money_type.__class__:
                self.money_store.remove(m)
                return
    @property
    def total_money(self):
        """Returns the total monetary value of all money in the money box.

        Return:
            balance: Amount of money in pence.

        """
        balance = 0
        for m in self.money_store:
            balance += m.value

        return balance

    @property
    def available_amounts(self):
        available = []
        for m in self.money_store:
            available.append(m.value)
        return available

    def calculate_change(self, target):
        """Returns a list of coins or notes that match the target change amount."""
        money_to_return = []

        if target == 0:
            return money_to_return

        change = calculate_change(target, self.available_amounts)

        remaining_change = change

        for m in self.money_store:
            if m.value in remaining_change:
                money_to_return.append(m)
                remaining_change.remove(m.value)

            if len(remaining_change) == 0:
                return money_to_return

