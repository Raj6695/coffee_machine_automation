from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

menu = Menu()

while is_on:
    options = menu.get_items()
    user_input = input(f"select:{options}: ")
    if user_input == "off":
        is_on = False

    elif user_input == "report":
        money_machine.report()
        coffee_maker.report()

    else:
        drink = menu.find_drink(user_input)
        is_enough_ingredients = CoffeeMaker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)
