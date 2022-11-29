
board = [
    ['X', 'O', 'O'],
    ['-', 'X', '-'],
    ['O', 'X', '-']
]

for row in board:
    for value in row:
        print(value, end=' ')
    print()
