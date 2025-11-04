from player import HumanPlayer, AiPlayer
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

    def available_moves(self):
        ret = []
        for i in self.board:
            if i == ' ' :
                ret.append(i)
        return ret

    def make_move(self, square, letter):
        self.board[square] = letter
        if self.is_winner(letter):
            self.current_winner = letter

    def is_winner(self, letter):
        # check the rows
        for i in range(3):
            ret = True
            for j in range(3):
                if self.board[(i*3)+j] != letter:
                    ret = False
            if ret == True:
                return ret
        # check the columns
        for i in range(3):
            ret = True
            for j in range(3):
                if self.board[i+(j*3)] != letter:
                    ret = False
            if ret == True:
                return ret
        # check diagonals
        ret = True
        for i in self.board[0, 4, 8]:
            if i != letter:
                ret = False
        if ret == True:
            return ret
        
        # check second diagonals
        ret = True
        for i in self.board[2, 4, 6]:
            if i != letter:
                ret = False
        if ret == True:
            return ret
        
        return False


def play(game, x, o):
    print('''Welcome to Tic-Tac-Toe!
    | 1 | 2 | 3 |
    | 4 | 5 | 6 |
    | 7 | 8 | 9 |''')

    letter = 'X'

    while len(game.available_moves()) != 0:
        if letter == 'X':
            position = x.get_move(game)
        else:
            position = o.get_move(game)

        if game.make_move(position, letter):
            game.print_board()

            if game.current_winner:
                print(letter + ' wins!!!')
                return letter
            
        letter = 'O' if letter == 'X' else 'X'  # switches player
    
    print('It\'s a tie!')


if __name__ == '__main__':
    x = AiPlayer('X')
    o = HumanPlayer('O')
    game = TicTacToe()
    play(game, x, o)