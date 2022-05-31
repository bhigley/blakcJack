from Card import Card
from random import randint

class Deck():

    cards = []
    currentCard = 0
    cardCount = 0

    def __init__(self):
        for i in range(4):
            for j in range(13):
                card = Card(i, j)
                self.cards.append(card)

    def newDeck(self):
        self.cards = []
        self.cardCount = 0
        for i in range(4):
            for j in range(13):
                card = Card(i, j)
                self.cards.append(card)


    def shuffle(self):
        # TODO: add ability to shuffle multiple decks
        for i in range(52):
            tempCard = self.cards[i]
            randIndex = randint(0, 51)
            self.cards[i] = self.cards[randIndex]
            self.cards[randIndex] = tempCard
        self.currentCard = 0 # reset currentCard

    def draw(self):
        card = self.cards.pop()
        if card.value < 7 and card.value > 1:
            self.cardCount += 1
        elif card.value == 1 or card.value > 9:
            self.cardCount -= 1
        return card
