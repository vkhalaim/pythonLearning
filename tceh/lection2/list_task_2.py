objectList = ["Pokemon", "Digimon", "Dragon", "Cat", "Dog"]

# first method
for i in objectList:
    print("Element of list -> " + i + "[" + str(objectList.index(i)) + "]"
          + "(in square braces index of element)")

# enumarate
print("-------------------")
for index, element in enumerate(objectList):
    print(str(element + "[" + str(index) + "]"))
