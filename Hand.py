class Hand:
    def __init__(self, bet):
        self.bet = bet
        self.cardsInHand = {}
        self.handValue = 0
        self.maxCardsInHand = 7

    def setCard(self, card):
        if len(self.cardsInHand) < self.maxCardsInHand:
            self.cardsInHand[len(self.cardsInHand)] = card
            self.handValue += card.value

    def doubleDown(self):
        self.bet += self.bet

    def aceFlip(self):
        cardIndex = 0
        for card in self.cardsInHand.values():
            if card.face == 14 and card.value == 11:
                self.handValue -= 10
                self.cardsInHand.get(cardIndex).value -= 10
                break
            cardIndex += 1

    def removeCard(self, cardToRemove):
        for index in range(len(self.cardsInHand.values())):
            if self.cardsInHand.get(index) == cardToRemove:
                self.handValue -= self.cardsInHand.get(index).value
                del self.cardsInHand[index]
                break
