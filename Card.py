class Card:
    def __init__(self, suit, index, cardBack):
        self.face = index
        self.suit = suit
        if not index > 10:
            self.value = index
        elif index > 10 and not index == 14:
            self.value = 10
        elif index == 14:
            self.value = 11
        self.image = "PlayingCards/" + str(suit) + "/" + str(index) + ".png"
        self.backImage = "PlayingCards/4/" + str(cardBack) + ".png"
