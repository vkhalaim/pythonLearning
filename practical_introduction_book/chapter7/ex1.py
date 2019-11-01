"""

Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list.

"""

from random import randint

myList = []

for i in range(0, 20):
    myList.append(randint(1, 100))

# (a)

print(myList)

# (b)
sum = 0

for i in range(0, len(myList)):
    sum += myList[i]

print("Average of the list is: ", sum / len(myList))

# (c)

print("The largest element in the list is: ", max(myList))
print("The smallest element in the list is: ", min(myList))

# (d)

copyList = myList[:]

copyList.remove(max(copyList))
copyList.remove(min(copyList))

print("The second to largest element in the list is: ", max(copyList))
print("The second to smallest element in the list is: ", min(copyList))

# (e)

even = 0

for i in range(0, len(myList)):
    if myList[i] % 2 == 0:
        even += 1

print("There are ", even, " elements in the list!")