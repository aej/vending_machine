from machine import VendingMachine
from money import OneCent, FiveCent, TenCent, TwentyFiveCent, FiftyCent, TwoDollarBill
from products import Candy, Snack, Nuts, Coke, Pepsi, Soda
from transaction import VendingAction

money_types = [
    OneCent,
    FiveCent,
    TenCent,
    TwentyFiveCent,
    FiftyCent,
    TwoDollarBill
]

products = [
    Candy(),
    Snack(),
    Nuts(),
    Coke(),
    Pepsi(),
    Soda()
]

money_stock = [
    OneCent(),
    FiveCent(),
    TenCent(),
    TwentyFiveCent(),
    FiftyCent(),
    TwoDollarBill()
]


if __name__ == '__main__':

    vending_machine = VendingMachine(products=products, money_stock=money_stock,
                                     money_types=money_types)

    number_of_products = len(vending_machine.products)
    money_in_stock = vending_machine.total_money
    print(f'vending machine has {number_of_products} products and {money_in_stock} pence in money')

    action = VendingAction(vending_machine)
    action.purchase(Candy(), [TenCent()])

    number_of_products = len(vending_machine.products)
    money_in_stock = vending_machine.total_money
    print(f'vending machine has {number_of_products} products and {money_in_stock} pence in money stock')

    action.purchase(Nuts(), [FiftyCent(), TenCent(), TenCent(), TenCent(), TenCent()])

    number_of_products = len(vending_machine.products)
    money_in_stock = vending_machine.total_money
    print(f'vending machine has {number_of_products} products and {money_in_stock} pence in money stock')

