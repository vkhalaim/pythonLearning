"""

Write a program that asks the user for an hour between 1 and 12 and for how many hours in
the future they want to go. Print out what the hour will be that many hours into the future.

"""

hour = eval(input("Enter hour between 1 to 12: "))
howManyHours = eval(input("Enter how many hours: "))

print((hour + howManyHours) % 12)
