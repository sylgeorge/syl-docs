print("Welcome to syl's pizza delivery.\nOur order list is as follows\nSmall pizza: $15\nMedium pizza: $20\nLarge pizza: $25")
print("Pepperoni for small pizza is +$2\nPepperoni for both medium and large pizza is +$3")
print("Extra cheese for any size of pizza is +$1")

size = input("What size of pizza would you like? small, medium or large?\n")
add_pepperoni = input("Would you like to add pepperoni to your pizza? yes or no\n")
extra_cheese = input("How about some extra cheese? yes or no\n")

pizza = 0
pepperoni = 0
cheese = 0

if size == "small":
 pizza += 15
elif size == "medium":
 pizza += 20
else:
 pizza += 25

if add_pepperoni == "yes":
 if size == "small":
  pepperoni += 2
 else:
  pepperoni += 3
 
if extra_cheese == "yes":
 cheese += 1

final_bill = pizza + pepperoni + cheese 

print(f"Your final bill is ${final_bill}.")