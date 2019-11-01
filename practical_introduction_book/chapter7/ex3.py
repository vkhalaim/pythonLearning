"""

Using a for loop, create the list below, which consists of ones separated by increasingly many
zeroes. The last two ones in the list should be separated by ten zeroes.


"""

zeroList = [0]
resultList = [1]
for i in range(0, 11):
    resultList.extend(zeroList * i)
    resultList.append(1)

print(resultList)