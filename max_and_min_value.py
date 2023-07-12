set_of_values = input("What is the set of values you would like to find the maximum and minimum value of?\n").split()

for n in range(0, len(set_of_values)):
 set_of_values[n] = int(set_of_values[n])

maximum = max(set_of_values)
print(f"The maximum value is {maximum}")

minimum = min(set_of_values)
print(f"The minimum value is {minimum}")