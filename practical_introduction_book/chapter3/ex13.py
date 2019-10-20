"""

Write a program that asks the user for a number and then prints out the sine, cosine, and
tangent of that number.

"""
from math import sin, cos, tan
number = eval(input("Enter a number: "))

print("sin of the number = ", sin(number))
print("cos of the number = ", cos(number))
print("tan of the number = ", tan(number))