"""

Write a program that asks the user to enter three numbers (use three separate input statements). 
Create variables called total and average that hold the sum and average of the
three numbers and print out the values of total and average

"""

num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))
num3 = eval(input("Enter third number: "))

total = num1 + num2 + num3
average = total / 3

print("Sum of three numbers is:", total, ",", "average is:", average, sep=" ")