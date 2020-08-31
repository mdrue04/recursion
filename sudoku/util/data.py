import numpy as np
import os


def get_grid(input=os.path.dirname(
        os.path.abspath(__file__)) + "/../example_input/input_sudoku.txt"):
    in_file = open(input, "r").readlines()
    grid = np.array([[int(num) for num in line.split(",")]
                     for line in in_file if line])
    print(f"Input sudoku: \n{grid}")
    return grid
