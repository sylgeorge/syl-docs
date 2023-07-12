print("Leap year checker.")

year = int(input("What year woukld you like to check? "))
result = year % 4

if result == 0:

     if result % 100 != 0:
         print("It is a leap year.")
     elif result % 100 == 0:
         if result % 400 == 0:
             print("It is a leap year.")
         else:
             print("It is not a leap year.")
     else:
         print("It is not a leap year.")

else:
    print("It is not a leap year.")