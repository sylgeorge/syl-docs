set_of_values = input("What is the set of values you would like to find the maximum and minimum value of?\n").split()

for n in range(0, len(set_of_values)):
 set_of_values[n] = int(set_of_values[n])

maximum_value = 0
for value in set_of_values:
 if value > maximum_value:
  maximum_value = value
print(f"The maximum value is {maximum_value}")

minimum_value = maximum_value
for value in set_of_values:
 if value < minimum_value:
  minimum_value = value
print(f"The minimum value is {minimum_value}")