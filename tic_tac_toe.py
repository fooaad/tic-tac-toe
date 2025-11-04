class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # Print a 3x3 Tic-Tac-Toe board
        for row_index in range(3):
            # Get one row (3 cells) from the board
            start = row_index * 3
            end = start + 3
            row = self.board[start:end]
            # ' | '.join(row) joins all elements in the row with " | " between them.
            print('| ' + ' | '.join(row) + ' |')
