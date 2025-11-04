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
            return 4 # always pick the center of the board in the first move
        else:
            return self.minimax(game, self.letter)
    
    def minimax(self, game, player):
        return 0