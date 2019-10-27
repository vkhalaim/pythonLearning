"""

An integer is called squarefree if it is not divisible by any perfect squares other than 1. For
instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those
numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is
divisible by 9, which is a perfect square. Write a program that asks the user for an integer and
tells them if it is squarefree or not.

"""
state = False
num = eval(input("Enter a number: "))

for i in range(2, 10):
	if (num % (i * i) == 0):
		state = True
		break

if state:
	print("The number isn't squarefree!")
else:
	print("The number is squarefree!")