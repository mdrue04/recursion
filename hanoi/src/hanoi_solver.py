import sys
from util.input import get_args


def get_move(start, target):
    return f"Move from {start} to {target}."


def solve_hanoi(num_plates, start, target, intermediate, moves):
    if num_plates == 0:
        pass
    else:
        solve_hanoi(num_plates-1, start, intermediate, target, moves)
        moves.append(get_move(start, target))
        solve_hanoi(num_plates-1, intermediate, target, start, moves)
    return moves


if __name__ == "__main__":
    args = get_args(sys.argv[1:])
    moves = []
    moves = solve_hanoi(args.num_plates, "A", "C", "B", moves)
    for move in moves:
        print(move)
