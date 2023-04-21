import Suit


class Deck:
    def __init__(self, cardBack):
        self.suits = {}
        for i in range(4):
            self.suits[i] = Suit.Suit(i, cardBack)
