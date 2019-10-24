"""

Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
1.


"""
counter = 0

for i in range(1, 101):
    if (i ** 2) % 10 == 1:
        counter += 1

print("There are ", counter, " numbers which square ends with 1")