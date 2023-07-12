print("Welcome to your BMI calculator!")

weight = input("Please input your weight?: ")
height = input("Please input your height?: ")

new_weight = float(weight)
new_height = float(height)

BMI = round(new_weight / new_height**2)
new_BMI = str(BMI)

if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI <= 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI <= 30:
    print(f"Your BMI is {BMI}, you are overweight.")
elif BMI <= 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")