dictionary = {"Vasyl" : "M", "Anastasia" : "F", "Dog" : "O", "Car" : "O"}

d_items = dictionary.items()

# items method
for item in d_items:
	print(item)

print("------------------------")

for key, item in dictionary.items():
	print(key, " : ", item)

print("------------------------")
# iterating through keys

for key in dictionary.keys():
	print(key, "->", dictionary[key])