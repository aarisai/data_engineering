import random

# Function to display the current game board
def display_board(board):
    # Clears the output (this is primarily used in Jupyter Notebooks, but it is optional)
    print("\n" * 10)
    
    # Print the current state of the board
    print('   |   |')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('   |   |')

# Function to let Player 1 choose their marker (X or O)
def player_input():
    marker = ''
    
    # Loop until the player enters either 'X' or 'O'
    while marker not in ['X', 'O']:
        marker = input('Player 1, choose your marker (X or O): ').upper()
    
    # Assign markers to Player 1 and Player 2 accordingly
    if marker == 'X':
        return ('X', 'O')  # Player 1 = X, Player 2 = O
    else:
        return ('O', 'X')  # Player 1 = O, Player 2 = X

# Function to place a marker on the board
def place_marker(board, marker, position):
    board[position] = marker

# Function to check if a player has won
def win_check(board, marker):
    # Check all possible winning combinations (rows, columns, diagonals)
    return (
        (board[7] == board[8] == board[9] == marker) or  # Top row
        (board[4] == board[5] == board[6] == marker) or  # Middle row
        (board[1] == board[2] == board[3] == marker) or  # Bottom row
        (board[7] == board[4] == board[1] == marker) or  # Left column
        (board[8] == board[5] == board[2] == marker) or  # Middle column
        (board[9] == board[6] == board[3] == marker) or  # Right column
        (board[7] == board[5] == board[3] == marker) or  # Diagonal 1
        (board[9] == board[5] == board[1] == marker)     # Diagonal 2
    )

# Function to randomly choose which player goes first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# Function to check if a position on the board is available
def space_check(board, position):
    return board[position] == ' '

# Function to check if the board is full
def full_board_check(board):
    # If any space is still available, return False (board is not full)
    return all(space != ' ' for space in board[1:])

# Function to get the player's next move (validating if the position is free)
def player_choice(board):
    position = 0
    
    # Loop until the player selects a valid and available position (1-9)
    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input('Choose your next position (1-9): '))
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
        
    return position

# Function to ask if players want to play again
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# Main function to play the game
def play_game():
    print('Welcome to Tic Tac Toe!')

    while True:
        # Reset the board
        the_board = [' '] * 10
        
        # Get player markers
        player1_marker, player2_marker = player_input()
        
        # Determine who goes first
        turn = choose_first()
        print(f'{turn} will go first.')
        
        # Check if players are ready
        play_game = input('Are you ready to play? Enter Yes or No: ').lower().startswith('y')
        
        game_on = play_game

        # Main game loop
        while game_on:
            if turn == 'Player 1':
                # Player 1's turn
                display_board(the_board)
                print("Player1 Turn: ")
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)
                
                # Check if Player 1 wins
                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print('Congratulations! Player 1 has won the game!')
                    game_on = False
                else:
                    # Check for a draw
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('The game is a draw!')
                        break
                    else:
                        # Switch turn to Player 2
                        turn = 'Player 2'
            else:
                # Player 2's turn
                display_board(the_board)
                print("Player 2 Turn: ")
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)
                
                # Check if Player 2 wins
                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('Congratulations! Player 2 has won the game!')
                    game_on = False
                else:
                    # Check for a draw
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('The game is a draw!')
                        break
                    else:
                        # Switch turn to Player 1
                        turn = 'Player 1'
        
        # Ask if they want to play again
        if not replay():
            break

# Start the game
play_game()
