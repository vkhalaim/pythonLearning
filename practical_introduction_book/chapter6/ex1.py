"""

(a) The total number of characters in the string
(b) The string repeated 10 times
(c) The first character of the string (remember that string indices start at 0)
(d) The first three characters of the string
(e) The last three characters of the string
(f) The string backwards
(g) The seventh character of the string if the string is long enough and a message otherwise
(h) The string with its first and last characters removed
(i) The string in all caps

"""

str1 = input("Enter a string: ")

# (a) total number of chars in the string
print("There are ", len(str1), " chars in the string.")

# (b) repeat string 10 times
for i in range(10):
	print(str1)

# (c) the first character of the string
print("The first character of the string is: ", str1[0])

# (d) the first 3 characters of the string
print("The first three characters of the string are: ", str1[0:3])

# (e) the last three characters of the string is
print("The last three characters of the string are: ", str1[-3:])

# (f) reverse string
print(str1[::-1])

# (g) seventh character or the message
if len(str1) >= 7:
	print(str1[:7])
else:
	print("String length is less than 7 characters!")

# (h) The string with its first and last characters removed 
print(str1[1:-1])

# (i) The string in all caps
print(str1.upper())