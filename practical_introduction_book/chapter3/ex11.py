"""

Write a program that asks the user to enter a weight in kilograms. The program should
convert it to pounds, printing the answer rounded to the nearest tenth of a pound.

"""

weight = eval(input("Enter your weight, please (kg): "))
kiloToPounds = 2.2
print("You weight is ", round(weight * kiloToPounds, 1), "pounds", sep=" ")