from unittest import case


class Card():

    suit = ""
    value = None

    def __init__(self, suit, value):
        if suit is 0:
            self.suit = 'hearts'
        elif suit is 1:
            self.suit = 'clubs'
        elif suit is 2:
            self.suit = 'diamonds'
        else:
            self.suit = 'spades'
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

