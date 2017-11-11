# Vending Machine Challenge

You need to design a Vending Machine which follows following requirements
Accepts coins of 1,5,10,25, 50 Cents i.e. penny, nickel, dime, and quarter as well as 1 and 2 dollar note

 - Allow user to select products e.g. CANDY(10), SNACK(50), NUTS(90), Coke(25), Pepsi(35), Soda(45)
 - Return selected product and remaining change if any
 
 
 ## Instructions on how to run

 Create a new money box with money objects inside
 
```python
from money import TenCent, FiveCent, TenCent
from machine import MoneyBox
 
money_store = [TenCent()]
valid_money = [FiveCent, TenCent]
money_box = MoneyBox(money_store=money_store, valid_money=valid_money)
```
 
 Create some products to add to your vending machine
 
```python
from products import Candy, Snack, Nuts

products = [Candy(), Snack(), Nuts()]
```

Initialize the vending machine

```python
from machine import VendingMachine

vending_machine = VendingMachine(products=products, money_box=money_box)
```


To perform transactions you should create a `VendingAction` class with your vending machine. For example to purchase a Candy, with Ten Cents you do the following

```python
from transactions import VendingAction

vending_action = VendingAction(vending_machine=vending_machine)
vending_action.purchase(Candy(), [TenCent()])
```

Or to purchase Nuts with a One dollar bill do the following

```python
vending_action = VendingAction(vending_machine=vending_machine)
vending_action.purchase(Nuts(), [OneDollarBill()])
```

# Testing

To run the test suite run 

```bash
pytest .
```
