from exceptions import NoStockException, InsufficientFundsForPurchase, CalculateChangeError


class VendingAction:
    """Actions that can be made on a vending machine.

    Args:
         vending_machine: An instantiated vending machine
    """

    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def add_money_objects_to_money_stock(self, money_objects):
        for m in money_objects:
            self.vending_machine.add_to_money_stock(m)

    def remove_money_objects_to_money_stock(self, money_objects):
        for m in money_objects:
            self.vending_machine.remove_from_money_stock(m)

    def calculate_change(self, provided_amount, product_price, money_objects):
        """Return a lsit of money objects to give as change"""
        change_amount = provided_amount - product_price
        try:
            change_to_give = self.vending_machine.money_box.calculate_change(change_amount)
            return change_to_give
        except CalculateChangeError as e:
            # if there is a calculate change error then return the money
            self.remove_money_objects_to_money_stock(money_objects)
            raise e

    def remove_product(self, product, money_objects):
        try:
            self.vending_machine.remove_product(product)
        except NoStockException as e:
            self.remove_money_objects_to_money_stock(money_objects)
            raise e

    def purchase(self, product, money_objects):
        """Perform necessary actions on the vending machine to purchase a
        product with a certain amount of money"""

        # check that there is enough money for the purchase
        total_money = self._calculate_total_money(money_objects)
        self._check_enough_money(product.price, total_money)

        self.add_money_objects_to_money_stock(money_objects)

        change_to_give = self.calculate_change(total_money, product.price, money_objects)

        self.remove_product(product, money_objects)

        # if all is good then give the change
        for change in change_to_give:
            self.vending_machine.remove_from_money_stock(change)

    @staticmethod
    def _check_enough_money(min_amount, total_money):
        """Check that the amount of money is greater than a minimum amount."""
        if total_money < min_amount:
            raise InsufficientFundsForPurchase("Insufficient funds")

    @staticmethod
    def _calculate_total_money(money_objects):
        amount = 0
        for m in money_objects:
           amount += m.value

        return amount
