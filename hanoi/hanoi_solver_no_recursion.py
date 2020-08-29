class Single_plate_move:
    def __init__(self, start, target):
        self.start = start
        self.target = target

    def __str__(self):
        return f"Move from {self.start} to {self.target}."


class Multi_plate_move:
    def __init__(self, num_plates, start='A', target='C', intermediate='B'):
        self.start = start
        self.target = target
        self.intermediate = intermediate
        self.num_plates = num_plates


class Hanoi:
    def __init__(self, num_plates):
        self.moves = []
        self.num_plates = num_plates

    def print_moves(self):
        for move in self.moves:
            print(move)

    def _insert_move(self, idx, start, target,
                     intermediate=None, num_plates=1):
        if num_plates == 0:
            return
        elif num_plates == 1:
            self.moves.insert(idx, Single_plate_move(start, target))
        else:
            self.moves.insert(idx, Multi_plate_move(
                num_plates, start, target, intermediate))

    def _resolve_multimove(self, idx, move):
        self.moves.pop(idx)
        self._insert_move(
            idx, move.start, move.intermediate, move.target, move.num_plates-1)
        self._insert_move(
            idx, move.start, move.target)
        self._insert_move(
            idx, move.intermediate, move.target, move.start, move.num_plates-1)

    def solve(self):
        self.moves.append(Multi_plate_move(self.num_plates))
        move_list_contains_multi_moves = True
        while move_list_contains_multi_moves:
            current_moves = self.moves.copy()
            move_list_contains_multi_moves = False
            idx = 0
            for move in current_moves:
                if type(move) == Multi_plate_move:
                    move_list_contains_multi_moves = True
                    self._resolve_multimove(idx, move)
                    idx += 3
                else:
                    idx += 1
        self.print_moves()


if __name__ == "__main__":
    hanoi = Hanoi(1)
    hanoi.solve()
