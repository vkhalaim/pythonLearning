riddles = {"What language do we learn?" : "python", 
	"Which version of python we learn?" : "3.6",
	"An element, feature, or factor that is liable to vary or change." : "variable",
	"Which loop should we use with evaluation after iteration?" : "do-while",
	"In python everything is ..." : "object"
}

rightAnswers = 0

for key in riddles:
	print(key)
	answer = input("Enter your answer: ")

	if answer.lower() == riddles.get(key):
		print("Your answer is right")
		rightAnswers += 1
	else:
		print("Answer is wrong :(")

print("You have {} right answers!".format(rightAnswers))