import random

all_names = input("Give me everybody's name in this format\nname1, name2, name3, ...\n")
names = all_names.split(", ")

payer_name = random.choice(names)

print(payer_name + " is going to buy the mean today")