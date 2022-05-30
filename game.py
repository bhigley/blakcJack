from Player import Player
from Deck import Deck

class Game:
    deck = None
    players = []
    currentPlayer = 0
    deckPoisition = 0

    def __init__(self, players: list=None):
        self.deck = Deck()
        if players is not None:
            for i in range(len(players)):
                self.players.append(players[i])
        else: # only one player no name
            self.players.append('Player1')
    
    def updateCurrentPlayer(self):
        if self.currentPlayer < len(self.players): # not at the last player
            self.currentPlayer += 1
        else:
            self.currentPlayer = 0

    def checkDeckPosition(self):
        if self.deckPoisition < 8 * len(self.players):
            return False # reshuffle
        else:
            return True # keep playing

    def dealerTurn(self):
        dealer = Player('Dealer', None)
        