from Menu import Menu, MenuItem
from coffeMaker import CoffeeMaker
from money_Machine import MoneyMachine


menu = Menu()
coffeeMaker = CoffeeMaker()
payment = MoneyMachine()


is_on = True
while is_on:
    choice = input(f"​What would you like? {menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
       coffeeMaker.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(choice):
            paymentt = payment.process_coins()
            if payment.make_payment(paymentt):
                coffeeMaker.make_coffee(choice)


