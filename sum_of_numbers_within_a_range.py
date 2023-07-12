range_of_numbers = input("What is your range of values?\n").split()

for n in range(0, len(range_of_numbers)):
 range_of_numbers[n] = int(range_of_numbers[n])

first_value = range_of_numbers[0]

position_of_last_value = len(range_of_numbers)
last_value = range_of_numbers[position_of_last_value - 1]

total = 0
for n in range(first_value, last_value + 1):
 total += n
print(total)

even_numbers_total = 0
odd_numbers_total = 0
for n in range(first_value, last_value + 1):
 if n % 2 == 0:
  even_numbers_total += n
 elif n % 2 != 0:
  odd_numbers_total += n

print(f"Sum of even numbers within the range is {even_numbers_total}")
print(f"Sum of odd numbers within the range is {odd_numbers_total}")