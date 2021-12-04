import csv

f = open('./input.txt', 'r')
boards = f.read().splitlines()
f.close()

reader = csv.reader(boards, delimiter=" ")
rows = list(reader)

generator = rows[0]
generator = [int(num) for num in generator[0].split(',')]
rows = rows[2:]

class Board:
    SIZE = 5
    def __init__(self, rows):
        self.rows = rows
        self.SIZE = 5
        self.MARK = 'X'

    def is_in_board(self, draw):
        for row in range(self.SIZE):
            for col in range(self.SIZE):
                if draw == self.rows[row][col]:
                    self.rows[row][col] = self.MARK
                    return True
        return False

    def is_winning_board(self):
        for row in self.rows:
            if row == [self.MARK] * self.SIZE:
                return True
        for col in [list(i) for i in zip(*self.rows)]:
            if col == [self.MARK] * self.SIZE:
                return True
        return False

    def sum_unmarked(self):
        unmarked = 0
        for row in range(self.SIZE):
            for col in range(self.SIZE):
                if self.rows[row][col] == self.MARK:
                    continue
                else:
                    unmarked += self.rows[row][col]
        return unmarked

boards = []
board = []
for row in rows:
    row = [int(num) for num in row if num != '']
    if row != []:
        board.append(row)
        continue
    boards.append(Board(board))
    board = []
boards.append(Board(board))

for draw in generator:
    for board in boards:
        if board.is_in_board(draw):
            if board.is_winning_board():
                break
    else:
        continue
    break

print(f'Prva cast vysledok: {board.sum_unmarked() * draw}')

i = 0
while len(boards) != 1:
    draw = generator[i]
    for e, board in enumerate(boards):
        if board.is_in_board(draw):
            if board.is_winning_board():
                boards = [b for b in boards  if b != board]

    i += 1

print(f'Druha cast vysledok: {(boards[0].sum_unmarked() - generator[i]) * generator[i]}')
