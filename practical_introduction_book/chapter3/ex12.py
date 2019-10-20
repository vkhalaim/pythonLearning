"""

Write a program that asks the user for a number and prints out the factorial of that number

"""

number = eval(input("Enter the number: "))

factorial = 1

for i in range(number, 0, -1):
	factorial *= i

print("factorial is: ", factorial)