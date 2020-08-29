from util.data import get_grid
from util.insertion import number_can_be_inserted


class SudokuSolver():
    def __init__(self, grid):
        self.grid = grid
        self.num_columns, self.num_rows = grid.shape

    def solve(self):
        for i in range(self.num_columns):
            for j in range(self.num_rows):
                if self.grid[i, j] == 0:
                    for number in range(1, 10):
                        if number_can_be_inserted(self.grid, number, i, j):
                            grid[i, j] = number
                            self.solve()
                            grid[i, j] = 0
                    return
        print(self.grid)
        input("Show futher solutions?")


if __name__ == "__main__":
    sudokuSolver = SudokuSolver(get_grid())
    sudokuSolver.solve()
