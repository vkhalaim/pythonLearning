"""

Write a program that asks the user to enter a word and prints out whether that word contains
any vowels.

"""

word = input("Enter a word: ")

vowels = "aeuoiy"

for i in vowels:
    if i in word:
        print("There are vowels in your word!")
        break