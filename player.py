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