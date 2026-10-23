"""Tic-Tac-Toe in the terminal: you (X) vs an unbeatable computer (O) using minimax."""

WIN_LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
             (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
             (0, 4, 8), (2, 4, 6)]              # diagonals


def winner(board):
    """Return 'X' or 'O' if someone has won, otherwise None."""
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def free_squares(board):
    return [i for i, v in enumerate(board) if v == " "]


def minimax(board, player):
    """Score the position for O: +1 O wins, 0 draw, -1 X wins."""
    w = winner(board)
    if w == "O":
        return 1
    if w == "X":
        return -1
    if not free_squares(board):
        return 0
    scores = []
    for sq in free_squares(board):
        board[sq] = player
        scores.append(minimax(board, "X" if player == "O" else "O"))
        board[sq] = " "
    return max(scores) if player == "O" else min(scores)


def best_move(board):
    """Pick the square with the best minimax score for O."""
    best_sq, best_score = None, -2
    for sq in free_squares(board):
        board[sq] = "O"
        score = minimax(board, "X")
        board[sq] = " "
        if score > best_score:
            best_sq, best_score = sq, score
    return best_sq


def show(board):
    rows = [" | ".join(board[i:i + 3]) for i in (0, 3, 6)]
    print("\n" + "\n---------\n".join(rows) + "\n")


def play():
    board = [" "] * 9
    print("You are X, computer is O. Squares are numbered 1-9, left to right, top to bottom.")
    show(board)
    while True:
        try:
            sq = int(input("Your move (1-9): ")) - 1
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue
        if sq not in free_squares(board):
            print("That square is not available.")
            continue
        board[sq] = "X"
        if winner(board) or not free_squares(board):
            break
        board[best_move(board)] = "O"
        show(board)
        if winner(board) or not free_squares(board):
            break
    show(board)
    w = winner(board)
    print(f"{w} wins!" if w else "It's a draw.")


if __name__ == "__main__":
    play()