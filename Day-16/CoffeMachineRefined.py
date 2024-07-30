from Menu import Menu, MenuItem
from coffeMaker import CoffeeMaker
from money_Machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


coffee_maker.report()
money_machine.report()
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What Would u Like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == ("report"):
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # print(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)





# is_on = True
# while is_on:
#     choice = input(f"​What would you like? {menu.get_items()}: ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#        coffeeMaker.report()
#     else:
#         drink = menu.find_drink(choice)
#         if coffeeMaker.is_resource_sufficient(choice):
#             paymentt = payment.process_coins()
#             if payment.make_payment(paymentt):
#                 coffeeMaker.make_coffee(choice)


