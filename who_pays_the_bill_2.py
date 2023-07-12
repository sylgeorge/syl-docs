import random

all_names = input("Give me everybody's name in this format\nname1, name2, name3, ...\n")
names = all_names.split(", ")

length = len(names)

random_choice = random.randint(0, length - 1)
payer_name = names[random_choice]

print(payer_name + " is going to buy the mean today")