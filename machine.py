from exceptions import NoStockException, InvalidMoneyTypes, MoneyTypeNotInStock


class VendingMachine:
    """A vending machine object holds products and accepts different
    types of money. The vending machine tracks how many of each type of product
    is inside it as well as the money inside it."""

    def __init__(self, products, money_stock, money_types, money_box):

        self.validate_money_stock(money_stock, money_types)

        self.products = products

        self.money_box = money_box
        self.money_stock = money_stock
        self.money_types = money_types

    def add_product(self, product):
        """A product is added to the vending machine."""
        self.product.append(product)

    def remove_product(self, product):
        """A product is removed from the vending machine."""
        if not type(product) in self.product_types():
            raise NoStockException("Stock has run out")

        product_to_remove = self.get_product_of_type(type(product))
        self.products.remove(product_to_remove)

    def add_to_money_stock(self, money_type):
        """Add a money amount to the money stock."""
        self.money_stock.append(money_type)

    def remove_from_money_stock(self, money_type):
        """Take away money amount from the money stock."""
        if money_type not in self.money_stock:
            raise MoneyTypeNotInStock("There are no coins or notes of this amount in the machine")
        self.money_stock.pop(money_type)

    def decrease_money_stock_by_amount(self, amount):
        """Reduce the money stock by a given penny amount."""
        available_money_types = set(self.money_stock)

        money_to_remove_from_stock = []

        while amount > 0:
            highest_money_amount = self.get_highest_money_amount(available_money_types, amount)
            money_to_remove_from_stock.append(highest_money_amount)
            amount -= highest_money_amount.value

        for money_amount in money_to_remove_from_stock:
            self.remove_from_money_stock(money_amount)

    @staticmethod
    def get_highest_money_amount(available_money_types, amount_threshold):
        """Given a list of available money types, it will return the highest value type that lies below
        the threshold."""
        types_below_threshold = [type for t in available_money_types if t.value <= amount_threshold]

        # return types_below_threshold.sort(#TODO)

    @property
    def total_money(self):
        """Returns the total monetary value of all money in the vending machine.

        Return:
            balance: Amount of money in pence.

        """
        balance = 0
        for m in self.money_stock:
            balance += m.value

        return balance

    def product_types(self):
        """Return all the product types in the vending machine"""
        return set(type(p) for p in self.products)

    def get_product_of_type(self, product_type):
        for p in self.products:
            if type(p) is product_type:
                return p

    @staticmethod
    def validate_money_stock(money_stock, money_types):
        for m in money_stock:
            if type(m) not in money_types:
                raise InvalidMoneyTypes("Initialized money types invalid.")


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
        """Take away money amount from the money stock."""
        if len(self.money_store) == 0 or money_type.__class__ not in self.money_store_types:
            raise MoneyTypeNotInStock("There are no coins or notes of this amount in the machine")

        for m in self.money_store:
            if m.__class__ == money_type.__class__:
                self.money_store.remove(m)
                return

    # TODO: Check that the money added is also valid
