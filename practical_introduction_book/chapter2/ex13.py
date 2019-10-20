"""

Use a for loop to print a triangle like the one below. Allow the user to specify how high the
triangle should be.

"""

height = eval(input("How high should be the pyramid?: "))

for i in range(0, height):
	print("*" * (height - i))