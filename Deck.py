from Card import Card
from random import randint

class Deck():

    cards = []
    currentCard = 0

    def __init__(self):
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
        # print(self.cards[self.currentCard].value, self.cards[self.currentCard].suit)
        self.currentCard += 1
        return self.cards[self.currentCard - 1]

# deck = Deck()
# deck.shuffle()
# for i in range(52):
#     deck.draw()
