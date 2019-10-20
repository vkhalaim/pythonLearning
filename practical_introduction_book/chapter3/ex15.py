"""

Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦ in 15◦
increments. Each result should be rounded to 4 decimal places. 

"""
from math import sin, cos, radians

for i in range(0, 350, 15):
	print(i, "---", round(sin(radians(i)), 4), round(cos(radians(i)), 4))