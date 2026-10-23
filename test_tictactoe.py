"""Plays every possible sequence of human moves against the AI and checks the AI never loses."""
from tictactoe import winner, free_squares, best_move

counts = {"X": 0, "O": 0, "draw": 0}


def explore(board):
    """Human (X) tries every free square; the AI (O) answers with best_move."""
    for sq in free_squares(board):
        b = board[:]
        b[sq] = "X"
        if winner(b) == "X":
            counts["X"] += 1
            continue
        if not free_squares(b):
            counts["draw"] += 1
            continue
        b[best_move(b)] = "O"
        if winner(b) == "O":
            counts["O"] += 1
        elif not free_squares(b):
            counts["draw"] += 1
        else:
            explore(b)


def test_ai_never_loses():
    explore([" "] * 9)
    total = sum(counts.values())
    print(f"Games played: {total}")
    print(f"Human wins: {counts['X']}, AI wins: {counts['O']}, draws: {counts['draw']}")
    assert counts["X"] == 0


if __name__ == "__main__":
    test_ai_never_loses()