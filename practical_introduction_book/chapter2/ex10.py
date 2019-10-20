"""

Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be

"""

width = eval(input("How wide should be the box?: "))
height = eval(input("How high should be the box?: "))

for i in range(height):
	print("*" * width)