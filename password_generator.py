import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '/', '-', '*', '+', '.', ',']

print("Welcome to the syl Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

letters_in_password = random.sample(letters, nr_letters)
numbers_in_password = random.sample(numbers, nr_numbers)
symbols_in_password = random.sample(symbols, nr_symbols)

l_in_p = ''.join(letters_in_password)
n_in_p = ''.join(numbers_in_password)
s_in_p = ''.join(symbols_in_password)

password = l_in_p + n_in_p + s_in_p

answer = input("Would you like it arranged or scattered?\n").lower()
if answer == "arranged":
 print(f"Your password is: {password}")
elif answer == "scattered":
 password_as_list = list(password)
 random.shuffle(password_as_list)
 password = ''.join(password_as_list)
 print(f"Your password is: {password}")