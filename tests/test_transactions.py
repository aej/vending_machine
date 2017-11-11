import pytest

from machine import MoneyBox, VendingMachine
from money import OneCent, FiveCent, TenCent, FiftyCent, OneDollarBill
from products import Candy, Snack, Nuts
from tests.helpers import assert_list_instances_equal
from transaction import VendingAction


@pytest.mark.transactions
def test_add_to_money_stock():
    products = [Candy(), Snack(), Nuts()]
    money_store = [TenCent()]
    valid_money = [FiveCent, TenCent]
    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    vending_machine = VendingMachine(products=products, money_box=money_box)

    vending_action = VendingAction(vending_machine=vending_machine)
    money_to_add = [TenCent()]
    vending_action.add_money_objects_to_money_stock([TenCent()])

    assert len(money_box.money_store) == 2
    assert_list_instances_equal(money_box.money_store, [TenCent(), TenCent()])


@pytest.mark.transactions
def test_remove_from_money_stock():
    products = [Candy(), Snack(), Nuts()]
    money_store = [TenCent(), FiveCent()]
    valid_money = [FiveCent, TenCent]
    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    vending_machine = VendingMachine(products=products, money_box=money_box)

    vending_action = VendingAction(vending_machine=vending_machine)
    money_to_add = [TenCent()]
    vending_action.remove_money_objects_to_money_stock([TenCent()])

    assert len(money_box.money_store) == 1
    assert_list_instances_equal(money_box.money_store, [FiveCent()])



@pytest.mark.transactions
def test_purchase_product():
    products = [Candy(), Snack(), Nuts()]
    money_store = [TenCent()]
    valid_money = [FiveCent, TenCent]
    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    vending_machine = VendingMachine(products=products, money_box=money_box)

    vending_action = VendingAction(vending_machine=vending_machine)
    vending_action.purchase(Candy(), [TenCent()])

    assert vending_machine.products == products
    assert_list_instances_equal(money_box.money_store, [TenCent(), TenCent()])


def test_purchase_product_case_two():
    products = [Candy(), Snack(), Nuts(), Candy(), Snack(), Nuts()]
    money_store = [OneCent(), TenCent(), TenCent(), FiveCent(), TenCent(), TenCent(), TenCent(), FiftyCent()]
    valid_money = [FiveCent, TenCent, OneCent, FiftyCent, OneDollarBill]
    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    vending_machine = VendingMachine(products=products, money_box=money_box)

    vending_action = VendingAction(vending_machine=vending_machine)
    vending_action.purchase(Nuts(), [OneDollarBill()])

    assert vending_machine.products == products
