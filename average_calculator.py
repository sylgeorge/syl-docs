set_of_values = input("What is the set of values you would like to find the average of?\n").split()

for n in range(0, len(set_of_values)):
 set_of_values[n] = int(set_of_values[n])

addition_of_set_of_values = sum(set_of_values)
number_of_values = len(set_of_values)

print(f"Total sum = {addition_of_set_of_values}")
print(f"number of values is {number_of_values}")

average = (addition_of_set_of_values / number_of_values)
print(f"the average is {average}")