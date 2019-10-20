"""

Write a program that asks the user for their name and how many times to print it. 
The program should print out the user’s name the specified number of times.

"""
try:
	name = input("What's your name?: ")
	howMany = eval(input("How many times print it?: "))

	if (howMany <= 0):
		print("How many times should be greater than zero, your input changed to 1")
		howMany = 1

finally:
	pass

for i in range(howMany):
	print(name)