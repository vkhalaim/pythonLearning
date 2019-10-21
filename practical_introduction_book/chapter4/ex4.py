"""

Write a program that lets the user play Rock-Paper-Scissors against the computer. There
should be five rounds, and after those five rounds, your program should print out who won
and lost or that there is a tie.

"""
from random import randint

t = ["Rock", "Paper", "Scissors"]
pointsHuman = 0
pointsComputer = 0
rounds = 10

for i in range(1, rounds + 1):
	print(i, "round!")
	humanChoice = input("Enter Rock/Paper/Scissors: ")
	computerChoice = t[randint(0, 2)]
	print("computer turn: ", computerChoice)

	if (humanChoice == computerChoice):
		print("Tie in this round")
	elif (humanChoice == "Rock"):
		if (computerChoice == "Paper"):
			print("computer win!")
			pointsComputer += 1
		else:
			print("human win!")
			pointsHuman += 1
	elif (humanChoice == "Paper"):
		if (computerChoice == "Scissors"):
			print("computer win!")
			pointsComputer += 1
		else:
			print("human win!")
			pointsHuman += 1
	else:
		if (computerChoice == "Rock"):
			print("computer win!")
			pointsComputer += 1
		else:
			print("human win!")
			pointsHuman += 1

print("Final result! Human: ", pointsHuman, ", computer: ", pointsComputer,
 ", ties: ", rounds - pointsComputer - pointsHuman)

