MENU = {
	"espresso": {
		"ingredients": {
			"water": 50,
			"coffee": 18,
		},
		"cost": 15,
	},
	"latte": {
		"ingredients": {
			"water": 200,
			"milk": 150,
			"coffee": 24,
		},
		"cost": 25,
	},
	"cappuccino": {
		"ingredients": {
			"water": 250,
			"milk": 100,
			"coffee": 24,
		},
		"cost": 30,
	}
}

RESOURCES = {
	'water': 300,
	'milk': 200,
	'coffee': 100,
}

profit = 0


def show_report():
	print(f"Water: {RESOURCES['water']}ml")
	print(f"Milk: {RESOURCES['milk']}ml")
	print(f"Coffee: {RESOURCES['coffee']}g")
	print(f"Money: Rs {profit}")


def is_resources_sufficient(coffee_ingredients):
	"""Returns True if the resources are sufficient and False if not"""
	for item in coffee_ingredients:
		if RESOURCES[item] <= coffee_ingredients[item]:
			print(f'There is not enough {item}')
			return False
	return True


def process_coins():
	"""Returns the total money inserted"""
	print('Insert coins:')
	total = int(input('Enter Re 1 coins: ')) * 1
	total += int(input('Enter Rs 2 coins: ')) * 2
	total += int(input('Enter Rs 5 coins: ')) * 5
	total += int(input('Enter Rs 10 coins: ')) * 10
	print(f'You inserted: Rs {total}')
	return total


def is_transaction_successful(money_received, coffee_cost):
	"""Returns true if money is accepted and false if money is insufficient"""
	if money_received >= coffee_cost:
		change = money_received - coffee_cost
		if change > 0:
			print(f"Here's the remaining change Rs {change}")
		global profit
		profit += coffee_cost
		return True
	else:
		print(f"Not enough money, here's your money back Rs {money_received}")
		return False


def make_coffee(coffee_name, coffee_ingredients):
	"""Deduct the required ingredients from the resources"""
	for item in coffee_ingredients:
		RESOURCES[item] -= coffee_ingredients[item]
	print(f"Here's your {coffee_name}")


coffee_machine_on = True

while coffee_machine_on:

	user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

	if user_choice == 'report':
		show_report()
	elif user_choice == 'off':
		coffee_machine_on = False
	elif user_choice in MENU:
		drink = MENU[user_choice]
		if is_resources_sufficient(drink['ingredients']):
			payment = process_coins()
			if is_transaction_successful(payment, drink['cost']):
				make_coffee(user_choice, drink['ingredients'])

	else:
		print('Invalid option')
