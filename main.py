from Deck import Deck
from game import Game
from Player import Player

# game = Game()
# game.deck.shuffle()

# print("Welcome to balckjack")
# game.playerTurn()
deck = Deck()
deck.shuffle()

player1 = Player("player1")
player1.draw(deck, 2)
player1.showHand()
player1.showScore()
