"""
Module for rendering a given chess game in SVG format, and for displaying and printing the game state.
"""

import io
import os
import webbrowser
import subprocess
from bs4 import BeautifulSoup
import chess
import chess.svg
import chess.pgn


def print_parsed_svg(file_path="renders/BoardVisualisedFromPGN.svg"):
    """
    Prints the parsed SVG file content, if any.
    """
    with open(file_path, 'r') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    pre_tags = soup.find_all('pre')
    for tag in pre_tags:
        print(tag.text)


def show_in_browser(file_path="renders/BoardVisualisedFromPGN.svg"):
    """
    Opens the SVG file in the user's default web browser.
    """
    cwd = os.getcwd()
    full_path = os.path.join(cwd, file_path)
    webbrowser.open('file://' + full_path)

def show_in_preview(file_path="renders/BoardVisualisedFromPGN.svg"):
    """
    Opens the SVG file in the Mac's Preview application.
    """
    cwd = os.getcwd()
    full_path = os.path.join(cwd, file_path)
    subprocess.run(['open', '-a', 'Preview', full_path])

def pgn_to_svg(pgn_string, flipped=False):
    """
    Converts a given PGN (Portable Game Notation) string to SVG (Scalable Vector Graphics) format.
    If 'flipped' is True, the SVG represents the board from Black's perspective.
    """

    print(pgn_string)
    pgn = io.StringIO(pgn_string)
    game = chess.pgn.read_game(pgn)
    #Go to the end of the game and create a chess.Board() from it:
    game = game.end()
    board = game.board()
    boardsvg = chess.svg.board(board=board, flipped=flipped)
    f = open("renders/BoardVisualisedFromPGN.svg", "w")
    f.write(boardsvg)
    f.close()

if __name__ == "__main__":
    pgn_to_svg("1. e4 e5 2. Nf3 *")
    print_parsed_svg('renders/BoardVisualisedFromPGN.svg')
    show_in_browser('renders/BoardVisualisedFromPGN.svg')