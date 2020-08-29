
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
    solve_hanoi(3, "A", "C", "B")
