import math
import random

class Player():

    def __init__(self, letter):
        self.letter = letter

    def get_move(self,  game): # abstract method
        pass


class RandomBot(Player):
    def __init__(self, letter):
        super().__init__(self, letter)

    def get_move(self, game):
        return random.choice(game.available_moves())
    
class AiPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return random.choice(game.available_moves())
        else:
            return self.minimax(game, self.letter)
    
    def minimax(self, game, player):
        max_player = self.letter # AiPlayer
        other_player = 'O' if player == 'X' else 'X' # max_player can be equal to other_player

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize

        for possible_move in game.available_moves():
            game.make_move(possible_move, player)
            if game.is_winner: 
                if player == max_player:
                    score = 1 + len(game.available_moves())
                else:
                    score = - 1 - len(game.available_moves())
            elif len(game.available_moves()) == 0:
                score = 0
            else:
                score = self.minimax(game, other_player)

            if player == max_player:
                if score > best['score']:
                    best['score'] = score
                    best['position'] = possible_move
            else:
                if score < best['score']:
                    best['score'] = score
                    best['position'] = possible_move

            #undo move
            game.board[possible_move] = ' '
            game.current_winner = None
        
        return best['position']
    

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_position = False
        val = None
        while not valid_position:
            position = input('Your Turn. Input move (1-9): ')
            try:
                val = int(position)
                val -= 1
                if val not in game.available_moves():
                    raise ValueError
                valid_position = True
            except ValueError:
                print('Invalid square. Try again.')
        
        return val