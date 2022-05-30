from unittest import case


class Card():

    suit = ""
    value = None

    def __init__(self, suit, value):
        if suit is 0:
            self.suit = 'heart'
        elif suit is 1:
            self.suit = 'club'
        elif suit is 2:
            self.suit = 'diamond'
        else:
            self.suit = 'spade'
        self.value = value + 1

    def getValue(self):
        if self.value == 1:
            val = 11
        elif self.value == 11:
            val = 10
        elif self.value == 12:
            val = 10
        elif self.value == 13:
            val = 10
        else:
            val = self.value
        return val

    # def print(self):
    #     if self.value <= 10:
    #         print(self.value, self.suit)
    #     elif self.value is 11:
    #         print('jack', self.suit)
    #     elif self.value is 12:
    #         print('queen', self.suit)
    #     elif self.value is 13:
    #         print('king', self.suit)

    def show(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return "{} of {}".format(val, self.suit)

