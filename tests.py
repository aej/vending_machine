import pytest

from exceptions import InvalidMoneyTypes, MoneyTypeNotInStock
from machine import MoneyBox
from money import OneCent, FiveCent, TenCent


def assert_list_instances_equal(list_one, list_two):
    for i, j in zip(list_one, list_two):
        if not i.__class__ is j.__class__:
            assert False
    assert True


def test_money_box_reject_invalid_money_types():
    money_store = [OneCent()]
    valid_money = [FiveCent, TenCent]

    with pytest.raises(InvalidMoneyTypes):
        MoneyBox(money_store=money_store, valid_money=valid_money)


def test_money_box_valid_money_types():
    money_store = [OneCent()]
    valid_money = [OneCent, FiveCent]

    assert MoneyBox(money_store=money_store, valid_money=valid_money)


def test_add_money_to_money_box():
    money_store = [OneCent()]
    valid_money = [OneCent, FiveCent]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
    assert_list_instances_equal(money_box.money_store, [OneCent()])
    money_box.add_to_money_store(FiveCent())
    assert_list_instances_equal(money_box.money_store, [OneCent(), FiveCent()])


def test_add_invalid_money_to_money_box():
    money_store = [OneCent()]
    valid_money = [OneCent, FiveCent]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)

    with pytest.raises(InvalidMoneyTypes):
        money_box.add_to_money_store(TenCent())

    assert_list_instances_equal(money_box.money_store, [OneCent()])


def test_remove_money_from_money_box():
    money_store = [OneCent()]
    valid_money = [OneCent, FiveCent]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)

    money_box.remove_from_money_store(OneCent())

    assert money_box.money_store == []


def test_remove_money_from_empty_money_store():
    money_store = []
    valid_money = [OneCent, FiveCent]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)

    with pytest.raises(MoneyTypeNotInStock):
        money_box.remove_from_money_store(OneCent())

def test_remove_money_from_money_store_without_money_type():
    money_store = [OneCent()]
    valid_money = [OneCent, FiveCent]

    money_box = MoneyBox(money_store=money_store, valid_money=valid_money)

    with pytest.raises(MoneyTypeNotInStock):
        money_box.remove_from_money_store(FiveCent())
