print("Welcome to the love calculator!")

name_1 = input("what is your name?\n").lower()
name_2 = input("What is his/her name?\n").lower()

combined_name = name_1 + name_2

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u") 
e = combined_name.count("e")
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
ee = combined_name.count("e")

true = str(t + r + u + e)
love = str(l + o + v + ee)

percent = int(true + love)

if percent <= 10 or percent >= 90:
 print(f"Your score is {percent}%, You go together like coke and mentos.")
elif percent >= 40 and percent <= 50:
 print(f"Your score is {percent}%, You are alright together.")
else:
 print(f"Your score is {percent}%, Well you might have to rethink.")