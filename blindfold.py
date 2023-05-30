"""
Module for practicing chess openings in a blindfolded manner.
The user plays along a randomly selected opening line, receiving hints or viewing the played moves as needed.
"""

from generate_lines import generate_game, convert_to_pgn
from render import show_in_browser, pgn_to_svg, print_parsed_svg

def test_chess_lines():
    """
    Main function that enables user to play along a randomly chosen opening line.
    Offers commands to assist with move selection and to view the current game state.
    """
    while True:
        color = input("What color would you like to play? ").strip().lower()
        while color not in ["white", "black", "exit"]:
            print(">>> Please choose 'white' or 'black'")
            color = input("What color would you like to play? ").strip().lower()

        if color.lower() == "exit":
            return
        
        if color == "white":
            chosen_line = generate_game("white_games")
        else:
            chosen_line = generate_game("black_games")

        moves = chosen_line.split()
        print(">>> Play the first move")

        played_moves = []
        i = 0
        player_input = ""
        while i < len(moves):
            # Strip off move numbers, if present, from the recorded move
            recorded_move = moves[i].split('.')[-1]

            if color == "white" and i % 2 == 0 or color == "black" and i % 2 != 0:  # Player's move
                while True:
                    player_input = input().strip()

                    if player_input.lower() == "exit":
                        return

                    # Strip off move numbers, if present, from the player's move
                    player_move = player_input.split('.')[-1]

                    if player_move.lower() == recorded_move.lower():
                        played_moves.append(recorded_move)
                        break

                    elif player_input.lower() == "hint":
                        print(f">>> The piece that should be moved is {recorded_move[0]}")
                    elif player_input.lower() == "show":
                        print(f">>> The full next move is {recorded_move}")
                    elif player_input.lower() == "finish":
                        break
                    elif player_input.lower() == "moves":
                        print(f">>> Moves played so far: {convert_to_pgn(played_moves)}")
                    elif player_input.lower() == "view":
                        flipped = False if color=="white" else True
                        pgn=convert_to_pgn(played_moves)
                        pgn_to_svg(pgn, flipped)
                        show_in_browser()
                    elif player_input.lower() == "print":
                        flipped = False if color=="white" else True
                        pgn=convert_to_pgn(played_moves)
                        pgn_to_svg(pgn, flipped)
                        print_parsed_svg()
                    elif player_input.lower() == "help":
                        print(f">>> Commands - hint, show, moves, view, print, finish, exit")
                    else:
                        print(">>> Incorrect, try another move")

                if player_input.lower() == "finish":
                    break

            else:  # Program's move
                played_moves.append(recorded_move)
                print(f">>> {recorded_move}")

            i += 1

        print(f"Line Complete. Full line: {chosen_line}")
        flipped = False if color=="white" else False
        pgn_to_svg(chosen_line, flipped)
        print_parsed_svg()

if __name__ == "__main__":    
    test_chess_lines()
