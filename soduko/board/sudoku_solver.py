from copy import deepcopy

from prettytable import PrettyTable

from .board_options_manager import BoardOptionsManager


class SudokuSolver:
    def __init__(self, board):
        self.board = deepcopy(board)
        self.options = self.board
        self.empty_cells = []
        self.init_empty_cells()
        self.solutions = []

    def init_empty_cells(self):
        rows = [0 for _ in range(9)]
        cols = [0 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    rows[i] += 1
                    cols[j] += 1
                    self.empty_cells.append((i, j))

    def check_uniqueness(self):
        if not self.solutions:
            self.solve()
        return len(self.solutions) == 1

    def only_value_in_row(self, row, value):
        return len([k for k in range(9) if value == self.board[row][k]]) == 1

    def only_value_in_col(self, col, value):
        return len([k for k in range(9) if value == self.board[k][col]]) == 1

    def only_value_in_square(self, row, col, value):
        square_start_row = row - (row % 3)
        square_start_col = col - (col % 3)
        return (
            len(
                [
                    (k, p)
                    for p in range(3)
                    for k in range(3)
                    if value == self.board[square_start_row + p][square_start_col + k]
                ]
            )
            == 1
        )

    def only_value(self, row, col, value):
        return (
            self.only_value_in_row(row, value)
            and self.only_value_in_col(col, value)
            and self.only_value_in_square(row, col, value)
        )

    def solve(self, idx=0):
        if len(self.solutions) > 1:
            if self.solutions[0] == self.solutions[1]:
                print("solutions are equal! WTF?")
            return
        if idx == len(self.empty_cells):
            print("found solution: ")
            self.print_options()
            self.solutions.append(deepcopy(self.board))
            return
        i, j = self.empty_cells[idx]
        for new_val in range(1, 10):
            self.board[i][j] = new_val
            if self.only_value(i, j, new_val):
                self.solve(idx + 1)
            self.board[i][j] = 0

    def print_options(self):
        x = PrettyTable()
        x.field_names = ["", 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i, row in enumerate(self.board):
            x.add_row([str(i + 1), *row])
        print(x)


class SudokuSuggester:
    def __init__(self, board, board_options_handler=None):
        self.board = board
        self.solved = False
        self.options_handler = board_options_handler or BoardOptionsManager(self.board)
        self.options_handler.init_board_options(self.board)
        self.options_handler.update_board_options(self.board)

    def stringify(self):
        return "".join(
            [str(self.board[i][j]) for i in range(9) for j in range(9)]
        ).replace("0", ".")

    def solve(self):
        while True:
            next_steps = self.options_handler.next_step()
            if not next_steps:
                return
            for (i, j), val in next_steps:
                self.options_handler.options[i][j] = set()
                self.board[i][j] = val
                yield self
                self.update_board_options_according_to_cell(i, j)

    def update_board_options_according_to_cell(self, row, col):
        val = self.board[row][col]
        return self.options_handler.update_board_options_according_to_cell(
            row, col, val
        )

    def print_options(self):
        self.options_handler.print_options()

    def get_options(self):
        return self.options_handler.options

    def get_options_list(self):
        options = deepcopy(self.get_options())
        for i in range(9):
            for j in range(9):
                options[i][j] = list(options[i][j])
        return options
