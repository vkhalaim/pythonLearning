# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
from random import choice

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'
INITIAL_FIELD = [i for i in range(1, 16)] + [EMPTY_MARK]
# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = INITIAL_FIELD[:]

    for i in range(50):
        try:
            key = choice(list(MOVES.keys()))
            field = perform_move(field, key)
        except IndexError:
            continue

    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for i in range(4):
        print('{:2} {:2} {:2} {:2}'.format(*field[i * 4:i * 4 + 4]))


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    return INITIAL_FIELD == field


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """

    empty = field.index(EMPTY_MARK)

    if 0 <= empty + MOVES[key] <= 15:
        if key in ['w', 's']:
            field[empty], field[empty + MOVES[key]] = field[empty + MOVES[key]], field[empty]
        elif key in ['a', 'd'] and 0 <= (empty % 4) + MOVES[key] <= 3:
            field[empty], field[empty + MOVES[key]] = field[empty + MOVES[key]], field[empty]
        else:
            raise IndexError
        return field

    raise IndexError


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    user_input = ''

    while user_input not in ['w', 'a', 's', 'd']:
        user_input = input('_').lower()

    return user_input


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    game_field = shuffle_field()
    moves = 0

    try:
        while not is_game_finished(game_field):
            print_field(game_field)
            move = handle_user_input()
            game_field = perform_move(game_field, move)
            moves += 1
    except EOFError:
        print('Moves done: ', moves)
        print('shutting down...')

    if is_game_finished(game_field):
        print('Congrats!')
        print('Moves: ', moves)


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()
