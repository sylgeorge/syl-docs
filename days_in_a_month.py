def is_leap(year):
 result = year % 4

 if result == 0:

     if result % 100 != 0:
         return True
     elif result % 100 == 0:
         if result % 400 == 0:
             return True
         else:
             return False
     else:
         return False

 else:
     return False 

def days_in_month(y, m):
 month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 if m == 2:
  if is_leap(y) is True:
   return month_days[m-1] + 1
  elif is_leap(y) is False: 
   return month_days[m-1]
 elif m > 12 or m < 1:
  return "This is not a valid month"
 else:
  return month_days[m-1]
 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)