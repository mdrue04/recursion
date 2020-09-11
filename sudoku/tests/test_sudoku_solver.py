import pytest
import numpy as np

import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dir_path, "../src"))
from sudoko_solver_no_recursion import SudokuSolver


@pytest.fixture
def get_grids():
    grids = {}
    grids["input"] = np.array(
        [[1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 5, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 9, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0]])
    # This is only one possible solution
    grids["result"] = np.array(
        [[1, 2, 4, 3, 6, 5, 7, 8, 9],
         [5, 6, 3, 7, 8, 9, 1, 2, 4],
         [7, 9, 8, 1, 2, 4, 3, 5, 6],
         [2, 1, 6, 4, 5, 3, 8, 9, 7],
         [3, 4, 5, 8, 9, 7, 2, 6, 1],
         [9, 8, 7, 2, 1, 6, 4, 3, 5],
         [8, 3, 9, 5, 4, 1, 6, 7, 2],
         [6, 7, 1, 9, 3, 2, 5, 4, 8],
         [4, 5, 2, 6, 7, 8, 9, 1, 3]])
    return grids


def test_sudoku_solver_no_recursion(get_grids):
    sudoku_solver = SudokuSolver(get_grids["input"])
    sudoku_solver.solve()
    assert((sudoku_solver.grid == get_grids["result"]).all())
