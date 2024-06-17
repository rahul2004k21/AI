import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Function to evaluate the board
def evaluate(board):
    if check_winner(board, "X"):
        return 1
    elif check_winner(board, "O"):
        return -1
    else:
        return 0

# Minimax algorithm with Alpha-Beta Pruning
def minimax_alpha_beta(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, "X"):
        return 1
    elif check_winner(board, "O"):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax_alpha_beta(board, depth + 1, alpha, beta, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax_alpha_beta(board, depth + 1, alpha, beta, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for AI using Alpha-Beta Pruning
def find_best_move_alpha_beta(board):
    best_eval = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval = minimax_alpha_beta(board, 0, alpha, beta, False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Main function to play the game
def play_game_alpha_beta():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Let's play Tic-Tac-Toe!\n")
    print_board(board)

    while True:
        # Player's move
        while True:
            row = int(input("Enter the row number (0, 1, or 2): "))
            col = int(input("Enter the column number (0, 1, or 2): "))
            if board[row][col] == " ":
                board[row][col] = "O"
                break
            else:
                print("That position is already taken!")
        print_board(board)

        # Check if player wins
        if check_winner(board, "O"):
            print("Congratulations! You win!")
            break

        # Check for a draw
        if is_full(board):
            print("It's a draw!")
            break

        # AI's move
        print("AI is making its move...")
        ai_move = find_best_move_alpha_beta(board)
        board[ai_move[0]][ai_move[1]] = "X"
        print_board(board)

        # Check if AI wins
        if check_winner(board, "X"):
            print("AI wins! Better luck next time!")
            break

        # Check for a draw
        if is_full(board):
            print("It's a draw!")
            break

# Start the game
play_game_alpha_beta()
