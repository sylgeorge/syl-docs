print("Welcome to the love calculator!")

name_1 = input("what is your name?\n").lower()
name_2 = input("What is his/her name?\n").lower()

t_1 = name_1.count("t")
r_1 = name_1.count("r")
u_1 = name_1.count("u")
e_1 = name_1.count("e")
l_1 = name_1.count("l")
o_1 = name_1.count("o")
v_1 = name_1.count("v")
ee_1 = name_1.count("e")

t_2 = name_2.count("t")
r_2 = name_2.count("r")
u_2 = name_2.count("u")
e_2 = name_2.count("e")
l_2 = name_2.count("l")
o_2 = name_2.count("o")
v_2 = name_2.count("v")
ee_2 = name_2.count("e")

t = t_1 + t_2
r = r_1 + r_2
u = u_1 + u_2
e = e_1 + e_2
l = l_1 + l_2
o = o_1 + o_2
v = v_1 + v_2
ee = ee_1 + ee_2

true = str(t + r + u + e)
love = str(l + o + v + ee)

percent = int(true + love)

if percent <= 10 or percent >= 90:
 print(f"Your score is {percent}%, You go together like coke and mentos.")
elif percent >= 40 and percent <= 50:
 print(f"Your score is {percent}%, You are alright together.")
else:
 print(f"Your score is {percent}%, Well you might have to rethink.")