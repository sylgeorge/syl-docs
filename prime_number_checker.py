print("You have accessed the prime number checker.")

number = abs(int(input("What number would you like to check? ")))

is_prime = True
for i in range(2, number):
 if number % i == 0:
  is_prime = False
  break 

if is_prime:
   print("This is a prime number.")
else:
   print("This is not a prime number.")