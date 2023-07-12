import math

h = int(input("Height of wall in meters:"))
w = int(input("Width of wall in meters:"))
coverage = int(input("coverage of can of paint in square meters:"))

def paint_calc(height, width, cover):
 print(f"You'll need {math.ceil((height * width)/cover)} cans of paint.")

paint_calc(height = h, width = w, cover = coverage)
