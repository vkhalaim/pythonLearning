"""

Write a program that asks the user to enter a power and how many digits they want.
Find the last that many digits of 2 raised to the power the user entered.

"""

power = eval(input("Enter a power: "))
digits = eval(input("How many digits of the powered 2 you want to see?: "))

print((2 ** power) % (10 ** digits))