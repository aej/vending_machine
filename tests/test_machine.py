import mock
import pytest

from exceptions import InvalidMoneyTypes, MoneyTypeNotInStock, InvalidMoneyBox, NoStockException
from machine import MoneyBox, VendingMachine
from money import OneCent, FiveCent, TenCent
from products import Candy, Snack
from tests.helpers import assert_list_instances_equal


@pytest.mark.money_box
def test_money_box_reject_invalid_money_types():
    money_store = [OneCent()]
    valid_money = [FiveCent, TenCent]

    with pytest.raises(InvalidMoneyTypes):
        MoneyBox(money_store=money_store, valid_money=valid_money)


@pytest.mark.money_box
def test_money_box_valid_money_types():
    money_store = [OneCent()]
    valid_money = [OneCent, FiveCent]

    assert MoneyBox(money_store=money_store, valid_money=valid_money)


@pytest.mark.money_box
def test_add_money_to_money_box():
    money_store = [OneCent()]
    valid_money = [OneCent, FiveCent]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    assert_list_instances_equal(money_box.money_store, [OneCent()])
    money_box.add_to_money_store(FiveCent())
    assert_list_instances_equal(money_box.money_store, [OneCent(), FiveCent()])


@pytest.mark.money_box
def test_add_invalid_money_to_money_box():
    money_store = [OneCent()]
    valid_money = [OneCent, FiveCent]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)

    with pytest.raises(InvalidMoneyTypes):
        money_box.add_to_money_store(TenCent())

    assert_list_instances_equal(money_box.money_store, [OneCent()])


@pytest.mark.money_box
def test_remove_money_from_money_box():
    money_store = [OneCent()]
    valid_money = [OneCent, FiveCent]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)

    money_box.remove_from_money_store(OneCent())

    assert money_box.money_store == []


@pytest.mark.money_box
def test_remove_money_from_empty_money_store():
    money_store = []
    valid_money = [OneCent, FiveCent]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)

    with pytest.raises(MoneyTypeNotInStock):
        money_box.remove_from_money_store(OneCent())


@pytest.mark.money_box
def test_remove_money_from_money_store_without_money_type():
    money_store = [OneCent()]
    valid_money = [OneCent, FiveCent]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)

    with pytest.raises(MoneyTypeNotInStock):
        money_box.remove_from_money_store(FiveCent())


@pytest.mark.money_box
def test_total_money_in_money_box():
    money_store = [OneCent(), FiveCent(), FiveCent()]
    valid_money = [OneCent, FiveCent]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)

    amount = money_box.total_money

    assert amount == 11


@pytest.mark.money_box
def test_available_amounts():
    money_store = [OneCent(), FiveCent(), FiveCent()]
    valid_money = [OneCent, FiveCent]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)

    available_amounts = money_box.available_amounts

    assert available_amounts == [1, 5, 5]


@pytest.mark.money_box
def test_calculate_change():
    money_store = [OneCent(), FiveCent(), FiveCent()]
    valid_money = [OneCent, FiveCent]
    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    change_to_give = money_box.calculate_change(6)

    assert change_to_give == money_store[0:2]


@pytest.mark.vending_machine
def test_vending_machine_wihtout_moneybox():
    money_store = []
    valid_money = []
    products = []

    with pytest.raises(InvalidMoneyBox):
        VendingMachine(products=products, money_box=[])


@pytest.mark.vending_machine
def test_vending_machine_add_product():
    money_store = []
    valid_money = []
    products = []
    product_to_add = Candy()

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    vending_machine = VendingMachine(products=products, money_box=money_box)

    assert vending_machine.products == []

    vending_machine.add_product(Candy())
    assert_list_instances_equal(vending_machine.products, [product_to_add])


@pytest.mark.vending_machine
def test_vending_machine_remove_product():
    money_store = []
    valid_money = []
    products = [Candy()]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    vending_machine = VendingMachine(products=products, money_box=money_box)

    assert_list_instances_equal(vending_machine.products, products)

    vending_machine.remove_product(Candy())

    assert_list_instances_equal(vending_machine.products, [])


@pytest.mark.vending_machine
def test_vending_machine_remove_product_not_in_stock():
    money_store = []
    valid_money = []
    products = []

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    vending_machine = VendingMachine(products=products, money_box=money_box)

    assert_list_instances_equal(vending_machine.products, products)

    with pytest.raises(NoStockException):
        vending_machine.remove_product(Candy())

@pytest.mark.vending_machine
@mock.patch('machine.MoneyBox.add_to_money_store')
def test_add_to_money_stock(mock_add_to_money_store):
    money_store = []
    valid_money = []
    products = []
    money_to_add = FiveCent()

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    vending_machine = VendingMachine(products=products, money_box=money_box)

    vending_machine.add_to_money_stock(money_to_add)
    mock_add_to_money_store.assert_called_with(money_to_add)


@pytest.mark.vending_machine
@mock.patch('machine.MoneyBox.add_to_money_store')
def test_add_to_money_stock_catches_exception(mock_add_to_money_stock):
    money_store = []
    valid_money = []
    products = []
    money_to_add = FiveCent()
    mock_add_to_money_stock.side_effect = InvalidMoneyTypes

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    vending_machine = VendingMachine(products=products, money_box=money_box)

    with pytest.raises(InvalidMoneyTypes):
        vending_machine.add_to_money_stock(money_to_add)


@pytest.mark.vending_machine
@mock.patch('machine.MoneyBox.remove_from_money_store')
def test_remove_from_money_stock(mock_remove_from_money_store):
    money_store = [FiveCent()]
    valid_money = [FiveCent]
    products = []
    money_to_remove = FiveCent()

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    vending_machine = VendingMachine(products=products, money_box=money_box)

    vending_machine.remove_from_money_stock(money_to_remove)
    mock_remove_from_money_store.assert_called_with(money_to_remove)


@pytest.mark.vending_machine
@mock.patch('machine.MoneyBox.remove_from_money_store')
def test_remove_from_money_stock_catches_exception(mock_remove_from_money_store):
    money_store = [FiveCent()]
    valid_money = [FiveCent]
    products = []
    money_to_remove = FiveCent()
    mock_remove_from_money_store.side_effect = MoneyTypeNotInStock

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    vending_machine = VendingMachine(products=products, money_box=money_box)

    with pytest.raises(MoneyTypeNotInStock):
        vending_machine.remove_from_money_stock(money_to_remove)


@pytest.mark.vending_machine
def test_vending_machine_product_types():
    money_store = []
    valid_money = []
    products = [Candy(), Snack(), Snack()]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    vending_machine = VendingMachine(products=products, money_box=money_box)

    product_types = vending_machine.product_types()
    assert product_types == set([Candy, Snack])


@pytest.mark.vending_machine
def test_get_product_of_type():
    money_store = []
    valid_money = []
    products = [Candy(), Snack(), Snack()]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    vending_machine = VendingMachine(products=products, money_box=money_box)

    assert vending_machine.get_product_of_type(Snack) == products[1]
    assert vending_machine.get_product_of_type(Candy) == products[0]
