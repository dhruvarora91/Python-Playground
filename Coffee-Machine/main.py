from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_coffee_machine_on = True

while is_coffee_machine_on:

	user_choice = input(f"What would you like? {menu.get_items()}: ").lower()

	if user_choice == 'report':
		coffee_maker.report()
	elif user_choice == 'off':
		is_coffee_machine_on = False
	else:
		drink = menu.find_drink(user_choice)
		if coffee_maker.is_resource_sufficient(drink):
			if money_machine.make_payment(drink.cost):
				coffee_maker.make_coffee(drink)
