"""
Module for generating random chess opening lines from a set of PGN files.
"""

import random
import chess.pgn

def get_random_integer(max_value):
    """
    Returns a random integer between 0 and max_value (inclusive).
    """
    return random.randint(0, max_value)

def get_first_move(game):
    """
    Returns the first move of a given game, if any.
    """
    if game.mainline_moves():
        return str(game.mainline_moves()).split(" ")[1]
    else:
        return
    
def convert_to_pgn(move_list):
    """
    Converts a list of moves into PGN (Portable Game Notation) format.
    """
    pgn_moves = []
    for i in range(0, len(move_list), 2):
        move_number = i // 2 + 1
        white_move = move_list[i]
        black_move = move_list[i+1] if i+1 < len(move_list) else ""
        pgn_moves.append(f"{move_number}.{white_move} {black_move}".strip())
    return " ".join(pgn_moves)

def generate_game(pgn_file):
    """
    Generates a random game line from a specified PGN file.
    """
    png_folder = open(f'pgn/{pgn_file}.pgn')
    base_pgn = chess.pgn.read_game(png_folder)

    move_list = []

    if len(base_pgn.variations) > 1:
        line_choice = get_random_integer(len(base_pgn.variations)-1)
        base_pgn.promote_to_main(line_choice)

    move_list.append(get_first_move(base_pgn))

    index = base_pgn.next()
    i=0
    while index:
        if len(index.variations) > 1:
            line_choice = get_random_integer(len(index.variations)-1)
            index.promote_to_main(line_choice)
        if (first_move := get_first_move(index)):
            move_list.append(first_move)
        index = index.next()
        i=i+1

    return convert_to_pgn(move_list)

if __name__ == "__main__":
    print(generate_game("white_games"))

