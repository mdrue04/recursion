from util.data import get_grid
from util.insertion import number_can_be_inserted


class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
        self.num_columns, self.num_rows = grid.shape
        self.num_fields = self.num_columns * self.num_rows
        self.rewinding = False
        self.ns_of_original_grid = []
        for n in range(self.num_columns * self.num_rows):
            i, j = self._convert_n_to_i_j(n)
            if self.grid[i][j] > 0:
                self.ns_of_original_grid.append(n)

    def _convert_n_to_i_j(self, n):
        i = int(n / 9)
        j = n % 9
        return i, j

    def _get_next_idx(self, n):
        if self.rewinding:
            return n - 1
        else:
            return n + 1

    def _handle_field(self, n):
        if n in self.ns_of_original_grid:
            # don't change original fields
            return
        i, j = self._convert_n_to_i_j(n)
        for m in range(self.grid[i][j] + 1, 10):
            if number_can_be_inserted(self.grid, m, i, j):
                self.grid[i][j] = m
                self.rewinding = False
                return
        # no number can be inserted in field
        self.grid[i][j] = 0
        self.rewinding = True

    def solve(self):
        field_idx = 0
        while field_idx < self.num_fields:
            self._handle_field(field_idx)
            field_idx = self._get_next_idx(field_idx)
        print("Solution of sudoku:")
        print(self.grid)


if __name__ == "__main__":
    sudoku_solver = SudokuSolver(get_grid())
    sudoku_solver.solve()
