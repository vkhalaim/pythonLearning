import turtle as t


def polygon(turtl, length, n):
    angle = 360 / n
    
    for i in range(n):
        turtl.fd(length)
        turtl.lt(angle)

bob = t.Turtle()

polygon(bob, 100, 5)