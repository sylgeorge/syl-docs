range_of_numbers = input("What is your range of values?").split()

for n in range(0, len(range_of_numbers)):
 range_of_numbers[n] = int(range_of_numbers[n])

first_value = range_of_numbers[0]

position_of_last_value = len(range_of_numbers)
last_value = range_of_numbers[position_of_last_value - 1]

for n in range(first_value, last_value + 1):
 if n % 3 == 0 and n % 5 == 0:
  print("fizzbuzz")
 elif n % 3 == 0:
  print("fizz")
 elif n % 5 == 0:
  print("buzz")
 else:
  print(n)