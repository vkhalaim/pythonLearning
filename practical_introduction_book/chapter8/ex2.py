"""

Write a censoring program. Allow the user to enter some text and your program should print
out the text with all the curse words starred out. The number of stars should match the length
of the curse word. For the purposes of this program, just use the“curse” words darn, dang,
freakin, heck, and shoot. Sample output is below:

"""

curseWords = ['darn', 'dang', 'freakin', 'heck', 'shoot']

message = input("Enter the message for censoring: ")

newMessage = " ".join(['*' * len(word) if word in curseWords else word for word in message.split(" ")])

print(newMessage)