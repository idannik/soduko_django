import random
from copy import deepcopy

import requests
from bs4 import BeautifulSoup

sudoku_boards = {
    "easy": {"min": 1000, "max": 1977},
    "medium": {"min": 2000, "max": 2590},
    "hard": {"min": 3000, "max": 3484},
    "extra_hard": {"min": 4000, "max": 4722},
}

LEVEL = "medium"


def get_a_random_board(level="easy"):
    min = sudoku_boards[level]["min"]
    max = sudoku_boards[level]["max"]
    return random.randint(min, max)


class Sudoku:
    def __init__(self, board_idx):
        print(f"Picked {LEVEL} board: {board_idx}")
        data = requests.get(
            f"https://sugoku.herokuapp.com/board?difficulty=medium"
        ).json()
        self.board = deepcopy(data["board"])
