"""

Write a program that asks the user to enter some text and then counts how many articles are
in the text. Articles are the words 'a', 'an', and 'the'.

"""

articles = ["a", "an", "the"]
articlesInSentence = 0

userInput = input("Enter a sentence: ")

# simple solution 
for word in userInput.split(" "):
	if word in articles:
		articlesInSentence += 1

print("There are", articlesInSentence, "articles in the sentence!")

# list comprehansion solution
art = [word for word in userInput.split(" ") if word in articles]

print(art)