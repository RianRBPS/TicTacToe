def display_board(board):
    # clear_output()  # Remember, this only works in jupyter!
    print(board[7] + '║' + board[8] + '║' + board[9])
    print('═╬═╬═')
    print(board[4] + '║' + board[5] + '║' + board[6])
    print('═╬═╬═')
    print(board[1] + '║' + board[2] + '║' + board[3])


def player_input():
    marker = ''

    # KEEP ASKING PLAYER 1 to choose X or O

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose X or O: ').upper()

    # ASSIGN PLAYER 2, the opposite marker

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    # ALL ROWS, and check to see if they all share the same markers?
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom

            # ALL Columns, check to se if marker matches
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side

            # 2 diagnoals, check to see match
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    from random import randint
    if randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
