set_of_values = input("What is the set of values you would like to find the average of?\n").split()

for n in range(0, len(set_of_values)):
 set_of_values[n] = int(set_of_values[n])

sum = 0
for value in set_of_values:
 sum += value

number_of_values = 0
for set in set_of_values:
 number_of_values += 1

print(f"Total sum = {sum}")
print(f"number of values is {number_of_values}")

average = sum / number_of_values
print(f"the average is {average}")