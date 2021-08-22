from TicTacToe.libraries import *
# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac Toe')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No: ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    ## Gameplay

    while game_on:
        if turn == 'Player 1':
            # Player 1 turn

            # Show the board
            display_board(theBoard)

            # Choose a position
            position = player_choice(theBoard)

            # Place the marker on the position
            place_marker(theBoard, player1_marker, position)

            # Check if they won
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('TIE GAME!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # PLAYER 2 TURN

            # Show the board
            display_board(theBoard)

            # Choose a position
            position = player_choice(theBoard)

            # Place the marker on the position
            place_marker(theBoard, player2_marker, position)

            # Check if they won
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('TIE GAME!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
