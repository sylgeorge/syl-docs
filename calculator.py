import math
import os
def calculator():
 logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
 """

 def add(n1, n2):
  return n1 + n2

 def subtract(n1, n2):
  return n1 - n2

 def multiply(n1, n2):
  return n1 * n2

 def divide(n1, n2):
  return n1 / n2

 def power(n1, n2):
  return n1 ** n2
 
 def root(n1, n2):
  return n1 ** (1 / n2)

 operators = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "**": power,
  "||": root,
 }

 print(logo)
 num1 = float(input("What is the the first number? "))

 for operator in operators:
  print(operator)

 again = True
 while again:
  operator_symbol = input("Pick an operator: ")
 
  num2 = float(input("What is the the next number? "))

  calculation_operation = operators[operator_symbol]
  answer = calculation_operation(num1, num2)

  print(f"{num1} {operator_symbol} {num2} = {answer}")

  another_calc = input(f"Type 'yes' to continue with {answer} or 'no' to start a new calculation. ").lower()
  if another_calc == "yes":
   num1 = answer
  elif another_calc == "no":
   again = False
   os.system('cls||clear')
   calculator()

calculator()