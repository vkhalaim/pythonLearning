"""

In calculus, the derivative of x
4
is 4x
3
. The derivative of x
5
is 5x
4
. The derivative of x
6
is
6x
5

"""

inp = input("Enter expression: ")

index = inp.index("^")
number  = int(inp[index+1:])

print("Derivative is: ", number, "x^", number - 1)