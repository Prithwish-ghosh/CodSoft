import math

# Constants for the players
HUMAN = -1
AI = 1
EMPTY = 0


def evaluate(board):
    # Evaluate the current state of the board
    # Positive value for AI's advantage, negative for human's advantage
    # 0 for a draw
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for line in lines:
        a, b, c = line
        if board[a] == board[b] == board[c]:
            if board[a] == AI:
                return 1
            elif board[a] == HUMAN:
                return -1
    return 0


def minimax(board, depth, is_maximizing, alpha, beta):
    if evaluate(board) != 0:
        return evaluate(board)

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval


def best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            move_score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = EMPTY
            if move_score > best_score:
                best_score = move_score
                best_move = i
    return best_move


def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], board[i + 1], board[i + 2])


def main():
    board = [EMPTY] * 9
    while True:
        print_board(board)
        move = int(input("Enter your move (0-8): "))
        if board[move] != EMPTY:
            print("Invalid move. Try again.")
            continue
        board[move] = HUMAN

        if evaluate(board) == -1:
            print("You win!")
            break

        ai_move = best_move(board)
        board[ai_move] = AI

        if evaluate(board) == 1:
            print("AI wins!")
            break

        if all(cell != EMPTY for cell in board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()
