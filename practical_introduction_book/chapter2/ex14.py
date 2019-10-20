"""

Use for loops to print a diamond like the one below. 

"""

height = eval(input("How high should be the diamond?: "))

for i in range(height):
	print(" " * (height - i - 1), "*" * (i + 1), end="")
	print("*" * i)
for j in range(height - 1, 0, -1):
	print(" " * (height - j), "*" * (j + 1), end="")
	print("*" * ( j - 2))