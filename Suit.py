import Card


class Suit:
    def __init__(self, suit, cardBack):
        self.cardsInSuit = {}
        for index in range(2, 15):
            self.cardsInSuit[index] = Card.Card(suit, index, cardBack)

    def removeCard(self, cardToRemove):
        index = 2
        for card in self.cardsInSuit:
            if card == cardToRemove:
                self.cardsInSuit.pop(index)
            index += 1