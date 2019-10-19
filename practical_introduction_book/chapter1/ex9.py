"""

A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
the percent tip they want to leave. Then print both the tip amount and the total bill with the
tip included.

"""

price = eval(input("What's the price of the meal?: "))
percent = eval(input("Percent of tip you would like to leave?: ")) / 100

print("Tip amount: ", price * percent)
print("Total bill: ", price + price * percent)