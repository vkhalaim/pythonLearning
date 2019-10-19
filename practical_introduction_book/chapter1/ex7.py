""" 

Write a program that asks the user for a weight in kilograms and converts it to pounds. There
are 2.2 pounds in a kilogram.

"""

weight = eval(input("Enter your weight, please (kg): "))
kiloToPounds = 2.2
print("You weight is ", weight * kiloToPounds, "pounds", sep=" ")