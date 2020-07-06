from random import randint


def handle_user_input():
    while True:
        user_input = input("Guess the number between 0 and 100: ")

        if user_input.isdigit():
            return int(user_input)

        print("Please enter a number!")


def main():
    random_number = randint(0, 100)

    while True:
        guess = handle_user_input()

        if guess == random_number:
            print("Congrats! You guessed the number!")
            break
        else:
            if random_number > guess:
                print("You are wrong! Number is bigger!")
            else:
                print("You are wrong! Number is lower!")


if __name__ == "__main__":
    main()
