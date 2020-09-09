def _check_row(grid, number, i):
    for idx in range(grid.shape[0]):
        if grid[i, idx] == number:
            return False
    return True


def _check_column(grid, number, j):
    for idx in range(grid.shape[1]):
        if grid[idx, j] == number:
            return False
    return True


def _check_square(grid, number, i, j):
    for i in range(i - i % 3, i - i % 3 + 3):
        for j in range(j - j % 3, j - j % 3 + 3):
            if number == grid[i, j]:
                return False
    return True


def number_can_be_inserted(grid, number, i, j):
    return (_check_row(grid, number, i)
            and _check_column(grid, number, j)
            and _check_square(grid, number, i, j))
