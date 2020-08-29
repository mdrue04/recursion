import numpy as np


def get_grid(input="recursion/sudoku/example_input/example1.txt"):
    in_file = open(input, "r").readlines()
    grid = np.array([[int(num) for num in line.split(",")]
                     for line in in_file if line])
    print(f"Input sudoku: \n{grid}")
    return grid
