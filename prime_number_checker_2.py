n = int(input("What number would you like to check?"))

def prime_number_checker(number):
 is_prime = True
 for i in range(2, number):
  if number % i == 0:
   is_prime = False
   break 

 if is_prime:
   print("This is a prime number.")
 else:
   print("This is not a prime number.")

prime_number_checker(number = n)