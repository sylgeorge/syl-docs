print("You have accessed the even or odd number checker.")

number = abs(int(input("What number would you like to check? ")))

new_number = number % 2

if new_number == 0:
 print("This is an even number.")
elif new_number != 0:
 print("This is an odd number.")