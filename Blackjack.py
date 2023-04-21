import Shoe
import Hand


class Blackjack:
    def blackjackCheck(self, handIndex):
        if self.playerHands.get(handIndex).handValue == 21 and len(self.playerHands.get(handIndex).cardsInHand) == 2:
            return True
        else:
            return False

    def hitHand(self, index):
        self.playerHands.get(index).setCard(self.gameShoe.hit())

    def splitCheck(self, playerHand):
        prevCardFace = 0
        prevCardValue = 0
        if not len(self.playerHands) >= self.maxHands:
            for card in playerHand.cardsInHand.values():
                if (card.face == prevCardFace) or (card.value == prevCardValue):
                    return True
                if prevCardFace == 0:
                    prevCardFace = card.face
                    prevCardValue = card.value
            return False

    def playerBustCheck(self, index):
        if self.playerHands.get(index).handValue > 21:
            cardIndex = 0
            for card in self.playerHands.get(index).cardsInHand.values():
                if card.face == 14 and card.value == 11:
                    self.playerHands.get(index).aceFlip()
                    if self.playerHands.get(index).handValue < 21:
                        return False
                    else:
                        return True
                cardIndex += 1
            if cardIndex == len(self.playerHands.get(index).cardsInHand):
                return True
        else:
            return False

    def dealerBustCheck(self):
        if self.dealerHand.handValue > 21:
            cardIndex = 0
            for card in self.dealerHand.cardsInHand.values():
                if card.face == 14 and card.value == 11:
                    self.dealerHand.cardsInHand.get(cardIndex).aceFlip()
                    if self.dealerHand.handValue < 21:
                        return False
                    else:
                        return True
                cardIndex += 1
                if cardIndex == len(self.dealerHand.cardsInHand):
                    return True
        else:
            return False

    def doubleDown(self, index):
        self.playerHands.get(index).setCard(self.gameShoe.hit())

    def __init__(self, numberOfDecks, cardBack):
        self.gameShoe = Shoe.Shoe(numberOfDecks, cardBack)
        self.blackjacks = 0
        self.dealerBusted = 0
        self.vsWins = 0
        self.vsPushes = 0
        self.vsLoss = 0
        self.handsPlayed = 0
        self.playerBusted = 0
        self.maxHands = 4
        self.playerHands = {}
        self.dealerHand = Hand.Hand(0)

    def dealGame(self, bet):
        self.bet = bet
        self.playerHands[0] = Hand.Hand(self.bet)
        self.playerHands.get(0).setCard(self.gameShoe.hit())

        self.dealerHiddenCard = self.gameShoe.hit()
        self.dealerHand.setCard(self.dealerHiddenCard)

        self.playerHands.get(0).setCard(self.gameShoe.hit())

        self.dealerHand.setCard(self.gameShoe.hit())

    def enableDouble(self, playerHand):
        if len(playerHand.cardsInHand) == 2:
            return True
        else:
            return False

    def enableSplit(self):
        for index in range(self.maxHands):
            if not self.playerHands.get(index) is None:
                if len(self.playerHands.get(index).cardsInHand) == 2:
                    if self.playerHands.get(index).handValue >= 3:
                        if self.splitCheck(self.playerHands.get(index)):
                            return True
        return False
