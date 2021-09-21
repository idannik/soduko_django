import os


from config.settings.base import STATICFILES_DIRS
from soduko.board.sudoku_solver import SudokuSolver

LEVEL = "easy"
LEVEL_PATH = os.path.join(STATICFILES_DIRS[0], "sudoku", "{level}")


class Sudoku:
    def __init__(self):
        self.board = []
        dir_path = LEVEL_PATH.format(level=LEVEL)
        print(dir_path)

        with open(os.path.join(dir_path, "0.txt")) as f:
            for line in f:
                self.board.append([])
                for i in range(9):
                    self.board[-1].append(int(line[i]))

        print("got board : ")
        print(self.board)
        solver = SudokuSolver(self.board)
        if solver.check_uniqueness():
            print(solver.solutions)
            return
        print("found multiple solutions, trying again :(")
