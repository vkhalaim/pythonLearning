from functools import reduce


# remain with map


print(map(lambda x: x % 5, [1, 4, 5, 30, 99]))


# to str


print(map(str, [3, 4, 90, -2]))


# filtering 


print(filter(lambda x: type(x) != str,  ['some', 1, 'v', 40, '3a', str]))


# reduce 

print(reduce(lambda x, y: x + len(y), ['some', 'other', 'value'], 0))