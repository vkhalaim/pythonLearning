import turtle as t


def circle(turtl, radius):
    for i in range(360):
        turtl.fd(radius)
        turtl.lt(1)

bob = t.Turtle()

circle(bob, 5)