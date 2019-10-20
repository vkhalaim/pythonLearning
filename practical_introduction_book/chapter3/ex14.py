"""

Write a program that asks the user to enter an angle in degrees and prints out the sine of that
angle

"""
from math import sin, radians

degrees = radians(eval(input("Enter an angle: ")))

print("sin of the number = ", sin(degrees))


