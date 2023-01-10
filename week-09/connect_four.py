
player = 'X'

board = [
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', 'X', '-', '-', '-'],
    ['-', '-', '-', 'O', '-', '-', '-'],
    ['-', '-', '-', 'X', '-', '-', '-']
]

def display_board(b):
    for row in range(6):
        for col in range(7):
            print(b[row][col], end=' ')
        print()


def change_player():
    if player == 'X':
        player = 'O'
    else:
        player = 'X'


display_board(board)

# loop
# ask user to play (ask column number)
# if play is valid
#   add user mark in proper position
#   check for winner
#   change player
#   display board
