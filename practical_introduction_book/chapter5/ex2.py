"""

Write a program to compute the sum 1 − 2 + 3 − 4 + ··· + 1999 − 2000.

"""

sum = 0

for i in range(1, 2001):
    if i % 2 == 0:
        sum += i * (-1)
    else:
        sum += i

print("Sum is: ", sum)