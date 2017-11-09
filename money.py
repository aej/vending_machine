from abc import ABC

COIN_TYPE = 0
NOTE_TYPE = 1


class BaseMoney(ABC):
    """Base money is an abstract money object which represents
    something that can be used as a unit of exchange."""
    money_type = None
    value = None


class Coin(BaseMoney):
    money_type = COIN_TYPE


class Note(BaseMoney):
    money_type = NOTE_TYPE


class OneCent(Coin):
    value = 1


class FiveCent(Coin):
    value = 5


class TenCent(Coin):
    value = 10


class TwentyFiveCent(Coin):
    value = 25


class FiftyCent(Coin):
    value = 50


class OneDollarBill(Note):
    value = 100


class TwoDollarBill(Note):
    value = 200

