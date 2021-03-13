from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operators = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide,
}

def calculator():
  print(logo)
  num1 = float(input('Enter 1st number: '))
  should_contiue = True

  while should_contiue:
    for symbol in operators:
      print(symbol)
    symbol = input('Choose the operation: ')
    num2 = float(input('Enter another number: '))
    calculation_function = operators[symbol]
    answer = calculation_function(num1, num2)
    print(f'{num1} {symbol} {num2} = {answer}')
    choice = input(f"Type 'y' to continue operation with {answer} or 'n' to start a new calculation: ").lower()

    if choice == 'y':
      num1 = answer
      should_contiue = True
    else:
      should_contiue = False
      break
  calculator()   

calculator()