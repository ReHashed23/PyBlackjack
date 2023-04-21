import random
import Deck


class Shoe:
    def __init__(self, shoeSize, cardBack):
        self.shoeSize = shoeSize
        self.numberOfCardsInShoe = 52 * shoeSize
        self.decks = {}
        for index in range(shoeSize):
            self.decks[index] = Deck.Deck(cardBack)

    def hit(self):
        randomDeck = random.randrange(self.shoeSize)
        randomSuit = random.randrange(4)
        randomCard = random.randrange(2, len(self.decks[randomDeck].suits[randomSuit].cardsInSuit)+2)
        card = self.decks[randomDeck].suits.get(randomSuit).cardsInSuit.get(randomCard)
        self.decks[randomDeck].suits.get(randomSuit).removeCard(card)
        return card
