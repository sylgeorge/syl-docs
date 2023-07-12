print("wondering how long you have if you were to die at 90?")

age = input("What is your current age?")

age_int = int(age)

year_left = 90 - age_int

days_left = year_left * 365
weeks_left = year_left * 52
months_left = year_left * 12

rounded_days = round(days_left)
rounded_weeks = round(weeks_left)
rounded_months = round(months_left)

print(f"you have {rounded_days}days, {rounded_weeks}weeks and {rounded_months}months left.")