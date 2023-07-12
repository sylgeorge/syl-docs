print("Welcome to the rollercoaster!")

height = int(input("What is your height in centimetres? "))
bill = 0

if height >= 120:
   print("Great! You can ride the rollercoaster.")

   comfort = input("What ticket would you like? regular or premium\n")

   if comfort == "regular":
      age = int(input("What is your age? "))
      if age < 12:
       bill += 5
       print("Child tickets are $5.")
      elif age <= 18:
       bill += 7
       print("Youth tickets are $7.")
      elif age >= 45 or age <= 55:
       print("The ticket is free for you.")
       exit() 
      elif age <= 56:
       bill += 12
       print("Adult tickets are $12.")
      else:
        print("Sorry, taking this ride at your age is a risk.")
        exit()
      wants_photo = input("Would you like a photo taken? It would cost an extra $3. yes or no\n")
      if wants_photo == "yes":
       bill += 3
      print(f"Your total bill is ${bill}")

   elif comfort == "premium":
      age = int(input("What is your age? "))
      if age < 12:
       bill += 7
       print("Child tickets are $7.")
      elif age <= 18:
       bill += 10
       print("Youth tickets are $10.")
      elif age >= 45 and age <= 55:
       print("The ticket is free for you.")
       exit()  
      elif age <= 56:
       bill += 18
       print("Adult tickets are $18.")
      else:
        print("Sorry, taking this ride at your age is a risk.")
        exit()
      wants_photo = input("Would you like a photo taken? It would cost an extra $3. yes or no\n") 
      if wants_photo == "yes":
       bill += 3
      print(f"Your total bill is ${bill}")
      

else:
    print("Sorry, You are too short to ride the rollercoaster.")