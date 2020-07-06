from random import choice

WORDS = [
    'Clowns', 'Python', 'Developer', 'Synthes', 'Wolf',
    'Australia', 'Ukraine', 'Paradise', 'Programming'
]

TRIES = 10


def get_random_word():
    return choice(WORDS).lower()


def handle_user_input():
    while True:
        user_input = input('Guess letter: ').lower()

        if user_input.isalpha() and len(user_input) == 1:
            return user_input


def is_game_finished(masked, guess):
    return "".join(masked) == guess


def check_guess(guessed_word, masked_word, guess, tries):
    if guess in masked_word:
        print('Letter is already used!')
    elif guess in guessed_word:
        for ind, value in enumerate(guessed_word):
            if value == guess:
                masked_word[ind] = guess

        print('Good job!')
    else:
        tries -= 1
        print('Not in the word!')

    return masked_word, tries


def print_masked_word(mask):
    print("".join(mask))


def main():
    guessed_word = get_random_word()
    masked_word = ['-'] * len(guessed_word)
    tries = TRIES

    while not is_game_finished(masked_word, guessed_word):
        guess = handle_user_input()

        masked_word, tries = check_guess(
            guessed_word, masked_word, guess, tries
        )

        print_masked_word(masked_word)
        print('Tries remaining: ', tries)
    if tries > 0:
        print('You won!')
    else:
        print('Try again later')


if __name__ == '__main__':
    main()
