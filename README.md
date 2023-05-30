
---

# Blindfold Chess Training Tool

Blindfold Chess Training Tool is a Python program designed to help chess players practice and improve their memory of chess openings and their overall blindfold chess skills. The program guides the user through randomly chosen opening lines, offering a variety of commands to assist with move selection and to view the current game state.

## Requirements

This application requires Python 3.8 (or higher) and a few Python packages 


## How to Run the Program

To start the program, simply navigate to the directory where you have cloned the repository and run:

```bash
git clone chess_blind_openings
cd chess_blind_openings
pip install -r requirements.txt
# Add your pgn files as described in "Adding Your Opening database"
python3 blindfold.py
```

The program will then prompt you to choose a color (white or black) for the opening game. After choosing the color, you will be asked to play the first move of a randomly selected opening line. 

## Adding Your Opening Database

The program needs an opening database to work properly. You will need to create two PGN files, one for white and one for black, which will contain your opening lines. 

Copy these files to:

```bash
pgn/white_games.pgn
pgn/black_games.pgn
```

Example files can be found at `pgn/white_games_example.pgn` and `pgn/black_games_example.pgn`. 

You can build your own opening database using online tools such as [ChessTempo](https://chesstempo.com/opening-training). To export your database from ChessTempo, follow the instructions given in this [forum post](https://old.chesstempo.com/chess-forum/help_and_support/converting_opening_repertoire_to_pgn_file_format-t8720.0.html#:~:text=Click%20on%20the%20blue%20menu,of%20your%20repertoire(s)).

Another useful resource to fetch your online games is [OpeningTree](https://www.openingtree.com/), which allows you to download all of your games from Lichess or Chess.com.


## Commands

During the game, you can enter the following commands:

- `hint`: The program gives a hint about the piece that should be moved next.
- `show`: The program shows the full next move.
- `moves`: The program displays all the moves that have been played so far in PGN format.
- `view`: The program generates an SVG representation of the current game state and opens it in the browser.
- `print`: The program generates an SVG representation of the current game state and prints the game state to the console.
- `finish`: The program stops the current game and prints the full opening line. A new random game will then start.
- `exit`: The program exits.


---
