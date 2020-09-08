import pytest
import test_utils
from hanoi_solver import solve_hanoi
from hanoi_solver_no_recursion import Hanoi


@pytest.fixture
def expected_moves():
    moves = ["AB", "AC", "BC"]
    return [f"Move from {move[0]} to {move[1]}." for move in moves]


def test_solve_hanoi(expected_moves):
    moves = []
    moves = solve_hanoi(2, "A", "C", "B", moves)
    assert(moves == expected_moves)


def test_solve_hanoi_no_recursion(expected_moves):
    hanoi = Hanoi(2)
    hanoi.solve()
    assert(hanoi.return_moves() == expected_moves)
