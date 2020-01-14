import turtle as t


def square(turtl, length):
	for i in range(4):
		turtl.fd(length)
		turtl.lt(90)

bob = t.Turtle()

square(bob, 200)