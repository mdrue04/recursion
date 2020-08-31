import sys
from util.input import get_args


def move(start, target):
    print(f"Move from {start} to {target}.")


def solve_hanoi(num_plates, start, target, intermediate):
    if num_plates == 0:
        pass
    else:
        solve_hanoi(num_plates-1, start, intermediate, target)
        move(start, target)
        solve_hanoi(num_plates-1, intermediate, target, start)


if __name__ == "__main__":
    args = get_args(sys.argv[1:])
    solve_hanoi(args.num_plates, "A", "C", "B")
