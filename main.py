from requests import delete
from Deck import Deck
from game import Game
from Player import Player

deck = Deck()
deck.shuffle()
# players = []
player1 = Player("player1")
dealer = Player("Dealer")


def printHands(player, dealer):
    print("Dealer score and hand:", dealer.showScore(True))
    dealer.showHand()
    print("Your score and hand:", player.showScore(True))
    player.showHand()


def play():
    if (len(deck.cards) < 15):
        print("shuffling")
        deck.newDeck()
        deck.shuffle()
    dealer.hand = []
    player1.hand = []
    dealer.draw(deck, 2)
    player1.hand = []
    player1.draw(deck, 2)
    if dealer.showScore(True) > 20 and player1.showScore(True) < 21:
        print("dealer has 21, you lose")
        print("Dealer hand:")
        dealer.showHand()
        print("Your hand:")
        player1.showHand()
    else:
        print("Dealer hand:")
        dealer.showHand(True)
        # player1.showHand()
        play = True
        while play:
            print("Your Hand:")
            player1.showHand()
            print("currentScore:", player1.showScore(True))
            choice = input("1 to draw 0 to check: ")
            if choice == "1":
                player1.draw(deck)
            else:
                play = False
            if player1.showScore(True) >= 21:
                play = False
        while dealer.showScore() < 17:
            dealer.draw(deck)
        if player1.bust is True:
            print("you busted")
            printHands(player1, dealer)
        elif dealer.bust is True:
            print("Dealer busted, you win")
            printHands(player1, dealer)
        elif (dealer.showScore() < player1.showScore()):
            print("you win")
            printHands(player1, dealer)
        else:
            print("you lose:")
            printHands(player1, dealer)
                      
def checkReplay():
    while True:      
        opt2=input("do you want to play again...?YES or NO :-")
        if opt2.lower()=='yes' or opt2.lower()=='no':
            break
    if opt2.lower()=='yes':
        return True
    elif opt2.lower()=='no':
        print("Current count:", deck.cardCount)
        print("Thanks for playing...")
        return False


print("Welcome to blackJack")
play()
while checkReplay() is True:
    play()
    

    
