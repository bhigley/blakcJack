# class Player(object):
#     def __init__(self, name):
#         self.name = name
#         self.hand = []

#     def sayHello(self):
#         print("Hi! My name is {}".format(self.name))
#         return self

#     # Draw n number of cards from a deck
#     # Returns true in n cards are drawn, false if less then that
#     def draw(self, deck, num=1):
#         for _ in range(num):
#             card = deck.deal()
#             if card:
#                 self.hand.append(card)
#             else: 
#                 return False
#         return True

#     # Display all the cards in the players hand
#     def showHand(self):
#         print("{}'s hand: {}".format(self.name, self.hand))
#         return self

#     def discard(self):
#         return self.hand.pop()


class Player:
    playerName = ""
    hand = []
    bank = 0


    def __init__(self, name, startingBank=0):
        self.playerName = name
        self.bank = startingBank

    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.draw()
            if card:
                self.hand.append(card)
            else: 
                return False
        return True
    

    def updateBank(self, wager, blackJack, won):
        if blackJack:
            self.bank = self.bank + (wager * (2/3))
        elif won:
            self.bank = self.bank + wager
        else:
            self.bank = self.bank - wager

    def showHand(self):
        # print("{}'s hand: {}".format(self.playerName, self.hand))
        for card in self.hand:
            print(card.show())
        return self

    def showScore(self):
        currentScore = 0
        for card in self.hand:
            currentScore += card.getValue()
        if currentScore > 21:
            print("current score", currentScore, " you busted")
        else:
            print("current score", currentScore)
        return currentScore

