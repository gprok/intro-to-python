def check_row(row):
    if row[0] == row[1] and row[0] == row[2] and row[0] != '-':
        return row[0]
    else:
        return None

def check_winner(result):
    if result is not None:
        print(result, "WINS!")
        return True
    else:
        return False

player = 'X'

board = [ ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-'] ]

game_over = False
while not game_over:
    # Print the board
    for row in board:
        for value in row:
            print(value, end=' ')
        print()

    r = int(input("Row:"))
    c = int(input("Col:"))

    board[r][c] = player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

    # Check ROWS
    for row in board:
        result = check_row(row)
        if check_winner(result):
            game_over = True
            break
    # Check COLUMNS
    for i in range(0, 3):
        list = [board[0][i], board[1][i], board[2][i]]
        result = check_row(list)
        if check_winner(result):
            game_over = True
            break
    # Check Diagonals
    list = [board[0][0], board[1][1], board[2][2]]
    result = check_row(list)
    if check_winner(result):
        break
    list = [board[2][0], board[1][1], board[0][2]]
    result = check_row(list)
    if check_winner(result):
        break
