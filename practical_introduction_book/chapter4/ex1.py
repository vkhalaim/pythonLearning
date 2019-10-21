"""

Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an
inch.

"""

length = eval(input("Enter a length in cm: "))

inch = 2.54

if (length < 0):
	print("Your input is invalid!")
else:
	print("There is ", round(length / inch, 2), " inches in ", length, " cantimiters.")