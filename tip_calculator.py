print("Welcome to the Tip calculator.")

total_bill = input("What is the total bill you wish to split? $")
percentage = input("What percentage tip would you like to give 10, 12 or 15? ")
people = input("How many people to split the bill? ")

total_bill_int = float(total_bill)
percentage_int = int(percentage)
people_int = int(people)

percentage_used = percentage_int / 100
total_tip_on_bill = total_bill_int * percentage_used
new_total_bill = total_bill_int + total_tip_on_bill
split_bill = round(new_total_bill / people_int, 2)

print(f"Each person should pay: ${split_bill}")