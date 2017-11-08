from exceptions import NoStockException


class VendingAction:
    """Actions that can be made on a vending machine.

    Args:
         vending_machine: An instantiated vending machine
    """

    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def purchase(self, product, money_objects):
        """Perform necessary actions on the vending machine to purchase a
        product with a certain amount of money"""

        # check that there is enough money for the purchase
        total_money = self._calculate_total_money(money_objects)
        self._check_enough_money(product.price, total_money)

        # remove the product from the vending machine if there is enough stock. Otherwise fail.
        try:
            self.vending_machine.remove_product(product)
        except NoStockException as e:
            raise e

        # add the money to the vending machine
        for m in money_objects:
            self.vending_machine.add_to_money_stock(m)

        change = self._calculate_change(product.price, total_money)

        if change > 0:
            self.vending_machine.decrease_money_stock_by_amount(change)

    def refund(self, product):
        pass

    def _check_enough_money(self, min_amount, total_money):
        """Check that the amount of money is greated than a minimum amount."""
        if total_money < min_amount:
            raise Exception("Insufficient funds")

    @staticmethod
    def _calculate_total_money(money_objects):
        amount = 0
        for m in money_objects:
           amount += m.value

        return amount

    @staticmethod
    def _calculate_change(item_value, money):
        """Work out how much change should be returned in the transaction"""
        return money - item_value
