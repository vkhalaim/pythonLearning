"""

Start with the list [8,9,10]. Do the following:
(a) Set the second entry (index 1) to 17
(b) Add 4, 5, and 6 to the end of the list
(c) Remove the first entry from the list
(d) Sort the list
(e) Double the list
(f) Insert 25 at index 3

The final list should equal [4,5,6,25,10,17,4,5,6,10,17]

"""
resultList = [4,5,6,25,10,17,4,5,6,10,17]
startList = [8,9,10]

startList[1] = 17

startList.append(4)
startList.append(5)
startList.append(6)

startList.remove(startList[0])

startList.sort()

startList.extend(startList)

startList.insert(3, 25)

print(startList == resultList) # returns True