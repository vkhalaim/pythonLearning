"""

Use a for loop to print a box like the one below

"""

width = eval(input("How wide should be the box?: "))
height = eval(input("How high should be the box?: "))

print("*" * width)

for i in range(height - 2):
	print("*", " " * (width - 2), "*", sep="")

print("*" * width)