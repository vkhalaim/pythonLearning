matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# print rows

for i in matrix:
    for elem in i:
        print(str(elem) + ' ', end='')
    print()

print("---------------")
# print columns

for i in range(0, len(matrix)+1):
    for elem in matrix:
        print(str(elem[i]) + ' ', end='')
    print()
