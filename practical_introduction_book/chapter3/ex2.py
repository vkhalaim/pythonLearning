"""

Write a program that generates a random number, x, between 1 and 50, a random number y
between 2 and 5, and computes x ** y

"""

from random import randint

x = randint(1, 50)
y = randint(2, 5)

print(x, "to power of", y, "is", x ** y, sep=" ")