"""

 Write a program that asks the user to enter an angle between −180◦ and 180◦ Using an
expression with the modulo operator, convert the angle to its equivalent between 0◦ and 360◦

"""

angle = eval(input("Enter the angle between -180 and 180: "))

print("Your angle between 0 to 360 is: ", angle % 360)