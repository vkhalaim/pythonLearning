"""

The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
number thereafter is the sum of the two preceding numbers. Write a program that asks the
user how many Fibonacci numbers to print and then prints that many.

"""

howMany = eval(input("How many Fibonacci numbers do you want?"))

num1 = 1
num2 = 0

for i in range(howMany):
	temp = num1
	num1 += num2
	num2 = temp

	print(num2, end=", ")