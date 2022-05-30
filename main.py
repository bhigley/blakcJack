from Deck import Deck
from game import Game
from Player import Player

game = Game()
game.deck.shuffle()

# print("Welcome to balckjack")
# game.playerTurn()
# deck = Deck()
# deck.shuffle()
# players = []

player1 = Player("player1")
dealer = Player("Dealer")
game.players.append(player1)
game.players.append(dealer)
game.startingDeal()
for player in game.players:
    print(player.playerName)
    player.showHand()
# players.append(player1)
# players.append(dealer)
# for _ in range(2):
#     for player in players:
#         player.draw(deck)

# dealer.showHand()
# player1.showHand()

# # dealer.draw(deck, 2)
# # dealer.showHand()
# # player1.draw(deck, 2)

# play = True
# while play:
#     player1.showHand()
#     player1.showScore()
#     choice = input("1 to draw 0 to check: ")
#     if choice == "1":
#         player1.draw(deck)
#     else:
#         play = False
#     if player1.showScore() > 21:
#         play = False
    

    
