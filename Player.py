
class Player:
    playerName = ""
    bust = False
    hand = []
    bank = 0
    bet = 0


    def __init__(self, name, startingBank=3000):
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

    def showHand(self, isDealer=False):
        # print("{}'s hand: {}".format(self.playerName, self.hand))
        if isDealer:
            for i in range(len(self.hand) - 1):
               print(self.hand[i].show()) 
        else:
            for card in self.hand:
                print(card.show())
        return self

    def showScore(self, isDealer=False):
        currentScore = 0
        for card in self.hand:
            currentScore += card.getValue()
        for card in self.hand:
            if currentScore > 21 and card.value == 1: # checking if there is an ace in hand
                currentScore = currentScore - 10
        # if isDealer is False:
        #     if currentScore > 21:
        #         self.bust = True
        #         print("current score", currentScore, " you busted")
        #     else:
        #         print("current score", currentScore)
        if currentScore > 21:
            self.bust = True
        return currentScore

