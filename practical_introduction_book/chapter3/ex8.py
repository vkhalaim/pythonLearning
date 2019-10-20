"""

Write a program that asks the user for a number of seconds and prints out how many minutes
and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds.

"""

seconds = eval(input("Enter number of seconds: "))

print(seconds // 60, "minutes", seconds % 60, "seconds", sep=" ")