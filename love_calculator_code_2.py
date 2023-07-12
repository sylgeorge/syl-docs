print("Welcome to the love calculator!")

name_1 = input("what is your name?\n").lower()
name_2 = input("What is his/her name?\n").lower()

t = 0
r = 0
u = 0
e = 0
l = 0
o = 0
v = 0
ee = 0

t += name_1.count("t")
r += name_1.count("r")
u += name_1.count("u")
e += name_1.count("e")
l += name_1.count("l")
o += name_1.count("o")
v += name_1.count("v")
ee += name_1.count("e")

t += name_2.count("t")
r += name_2.count("r")
u += name_2.count("u")
e += name_2.count("e")
l += name_2.count("l")
o += name_2.count("o")
v += name_2.count("v")
ee += name_2.count("e")

true = str(t + r + u + e)
love = str(l + o + v + ee)

percent = int(true + love)

if percent <= 10 or percent >= 90:
 print(f"Your score is {percent}%, You go together like coke and mentos.")
elif percent >= 40 and percent <= 50:
 print(f"Your score is {percent}%, You are alright together.")
else:
 print(f"Your score is {percent}%, Well you might have to rethink.")