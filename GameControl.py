import Blackjack
import Hand
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time


class GameControl:

    def __init__(self, decks, back):
        self.blackjack = Blackjack.Blackjack(decks, back)  # initializes blackjack
        self.buttonClicked = False
        self.hitTicker = 0

    def splitButtonClicked(self, root, index, bet):
        card = self.blackjack.playerHands.get(index).cardsInHand.get(1)
        if len(self.blackjack.playerHands) < self.blackjack.maxHands:
            self.blackjack.playerHands[len(self.blackjack.playerHands)] = Hand.Hand(self.blackjack.bet)
            self.totalBet += bet
            self.blackjack.playerHands.get(len(self.blackjack.playerHands) - 1).setCard(card)
            self.blackjack.playerHands.get(index).removeCard(card)
            cardToShow = Image.open(card.image)
            cardToShow = cardToShow.resize((80, 120))  # card size for game
            cardToShow = ImageTk.PhotoImage(cardToShow)
            cardToShowLabel = tk.Label(image=cardToShow)
            cardToShowLabel.image = cardToShow
            cardToShowLabel.grid(column=0, row=len(self.blackjack.playerHands) - 1)

            self.blackjack.hitHand(index)
            card = self.blackjack.playerHands.get(index).cardsInHand.get(1)
            cardToShow = Image.open(card.image)
            cardToShow = cardToShow.resize((80, 120))  # card size for game
            cardToShow = ImageTk.PhotoImage(cardToShow)
            cardToShowLabel = tk.Label(image=cardToShow)
            cardToShowLabel.image = cardToShow
            cardToShowLabel.grid(column=1, row=index)
            root.update()
            self.value.set(4)
            self.hitTicker -= 1

    def hitButtonClicked(self, index):
        self.blackjack.playerHands.get(index).setCard(self.blackjack.gameShoe.hit())
        self.value.set(2)

    def doubleButtonClicked(self, index, bet):
        self.blackjack.doubleDown(index)
        self.totalBet += bet
        self.value.set(3)

    def standButtonClicked(self, index):
        self.value.set(1)

    def dealerHitChoice(self):
        if self.blackjack.dealerHand.handValue >= 17:
            return False
        elif self.blackjack.dealerHand.handValue > 21 and 14 in self.blackjack.dealerHand.cardsInHand.values():
            cardIndex = 0
            for card in self.blackjack.dealerHand.cardsInHand.values():
                if card.face == 14 and card.value != 1:
                    self.blackjack.dealerHand.aceFlip()
                    if self.blackjack.dealerHand.handValue >= 17:
                        return False
                    else:
                        return True
                cardIndex += 1
        else:
            return True

    def winConditions(self, handIndex):
        if self.blackjack.blackjackCheck(handIndex):
            return 1
        if self.blackjack.playerBustCheck(handIndex):
            return 6
        if self.blackjack.dealerBustCheck():
            return 2
        if self.blackjack.playerHands.get(handIndex).handValue > self.blackjack.dealerHand.handValue and not \
                self.blackjack.playerBustCheck(handIndex) == True:
            return 3
        elif self.blackjack.playerHands.get(handIndex).handValue < self.blackjack.dealerHand.handValue and not \
                self.blackjack.dealerBustCheck() == True:
            return 5
        elif self.blackjack.playerHands.get(handIndex).handValue == self.blackjack.dealerHand.handValue and not \
                self.blackjack.dealerBustCheck() == True and not self.blackjack.playerBustCheck(handIndex) == True:
            return 4

    def game(self, root, bet, userMoney):
        canvas = tk.Canvas(root, width=root.winfo_screenwidth() * .7, height=root.winfo_screenheight() * .7,
                           bg="green")

        self.blackjack.dealGame(bet)  # plays a game with X amount of decks in play, using Y for card backs


        canvas.grid(columnspan=20, rowspan=8 * 52)
        root.update()

        standButton = tk.Button(root, text="Stand", command=lambda: self.standButtonClicked(0))
        hitButton = tk.Button(root, text="Hit Hand", command=lambda: self.hitButtonClicked(0))
        doubleButton = tk.Button(root, text="Double Down", command=lambda: self.doubleButtonClicked(0, bet),
                                 state="disabled")
        splitButton = tk.Button(root, text="Split Hand", command=lambda: self.splitButtonClicked(root, 0, bet),
                                state="disabled")
        standButton.grid(column=7, row=0)
        hitButton.grid(column=8, row=0)
        doubleButton.grid(column=9, row=0)
        splitButton.grid(column=10, row=0)

        self.value = IntVar()
        self.standClicked = False

        card = self.blackjack.playerHands.get(0).cardsInHand.get(0)
        cardToShow = Image.open(card.image)
        cardToShow = cardToShow.resize((80, 120))  # card size for game
        cardToShow = ImageTk.PhotoImage(cardToShow)
        cardToShowLabel0 = tk.Label(image=cardToShow)
        cardToShowLabel0.image = cardToShow
        cardToShowLabel0.grid(column=0, row=0)
        root.update()
        time.sleep(.5)

        card = self.blackjack.dealerHand.cardsInHand.get(1)
        cardToShow = Image.open(card.backImage)
        cardToShow = cardToShow.resize((80, 120))  # card size for game
        cardToShow = ImageTk.PhotoImage(cardToShow)
        cardToShowLabelD = tk.Label(image=cardToShow)
        cardToShowLabelD.image = cardToShow
        cardToShowLabelD.grid(column=11, row=0)
        root.update()
        time.sleep(.5)

        card = self.blackjack.playerHands.get(0).cardsInHand.get(1)
        cardToShow = Image.open(card.image)
        cardToShow = cardToShow.resize((80, 120))  # card size for game
        cardToShow = ImageTk.PhotoImage(cardToShow)
        cardToShowLabel1 = tk.Label(image=cardToShow)
        cardToShowLabel1.image = cardToShow
        cardToShowLabel1.grid(column=1, row=0)
        root.update()
        time.sleep(.5)

        cardToShow = Image.open(self.blackjack.dealerHand.cardsInHand.get(1).image)
        cardToShow = cardToShow.resize((80, 120))  # card size for game
        cardToShow = ImageTk.PhotoImage(cardToShow)
        cardToShowLabelD = tk.Label(image=cardToShow)
        cardToShowLabelD.image = cardToShow
        cardToShowLabelD.grid(column=11, row=1)
        root.update()
        time.sleep(.5)

        self.hitTicker = 0
        self.totalBet = bet
        while not (self.value.get() == 1 or self.value.get() == 3):
            if self.blackjack.playerBustCheck(0):
                self.value.set(1)
                break
            enableDouble = self.blackjack.enableDouble(self.blackjack.playerHands.get(0))
            enableSplit = self.blackjack.enableSplit()
            if enableDouble and self.hitTicker == 0 and userMoney - (bet + self.totalBet) > 0:
                doubleButton["state"] = "normal"
            if enableSplit and self.hitTicker == 0 and userMoney - (bet + self.totalBet) > 0:
                splitButton["state"] = "normal"
            root.update()
            self.hitTicker += 1

            root.wait_variable(self.value)
            buttonPressed = self.value.get()
            if buttonPressed == 1:
                break

            card = self.blackjack.playerHands.get(0).cardsInHand.get(1 + self.hitTicker)
            cardToShow = Image.open(card.image)
            cardToShow = cardToShow.resize((80, 120))  # card size for game
            cardToShow = ImageTk.PhotoImage(cardToShow)
            cardToShowLabel = tk.Label(image=cardToShow)
            cardToShowLabel.image = cardToShow
            cardToShowLabel.grid(column=1 + self.hitTicker, row=0)
            doubleButton["state"] = "disabled"
            splitButton["state"] = "disabled"
            root.update()
            if buttonPressed == 3:
                self.blackjack.playerHands.get(0).doubleDown()
                break

        doubleButton["state"] = "disabled"
        splitButton["state"] = "disabled"
        standButton["state"] = "disabled"
        hitButton["state"] = "disabled"
        root.update()

        if not self.blackjack.playerHands.get(1) is None:
            self.value.set(0)
            self.blackjack.playerHands.get(1).setCard(self.blackjack.gameShoe.hit())
            card = self.blackjack.playerHands.get(1).cardsInHand.get(1)
            cardToShow = Image.open(card.image)
            cardToShow = cardToShow.resize((80, 120))  # card size for game
            cardToShow = ImageTk.PhotoImage(cardToShow)
            cardToShowLabelD = tk.Label(image=cardToShow)
            cardToShowLabelD.image = cardToShow
            cardToShowLabelD.grid(column=1, row=1)

            standButton = tk.Button(root, text="Stand", command=lambda: self.standButtonClicked(1))
            hitButton = tk.Button(root, text="Hit Hand", command=lambda: self.hitButtonClicked(1))
            doubleButton = tk.Button(root, text="Double Down", command=lambda: self.doubleButtonClicked(1, bet),
                                     state="disabled")
            splitButton = tk.Button(root, text="Split Hand", command=lambda: self.splitButtonClicked(root, 1, bet),
                                    state="disabled")
            standButton.grid(column=7, row=1)
            hitButton.grid(column=8, row=1)
            doubleButton.grid(column=9, row=1)
            splitButton.grid(column=10, row=1)

            root.update()
            time.sleep(.5)

            self.hitTicker = 0

            while not (self.value.get() == 1 or self.value.get() == 3):
                if self.blackjack.playerBustCheck(1):
                    self.value.set(1)
                    break
                enableDouble = self.blackjack.enableDouble(self.blackjack.playerHands.get(1))
                enableSplit = self.blackjack.enableSplit()
                if enableDouble and self.hitTicker == 0 and userMoney - (bet + self.totalBet) > 0:
                    doubleButton["state"] = "normal"
                if enableSplit and self.hitTicker == 0 and userMoney - (bet + self.totalBet) > 0:
                    splitButton["state"] = "normal"
                root.update()
                self.hitTicker += 1

                root.wait_variable(self.value)
                buttonPressed = self.value.get()
                if buttonPressed == 1:
                    break

                card = self.blackjack.playerHands.get(1).cardsInHand.get(1 + self.hitTicker)
                cardToShow = Image.open(card.image)
                cardToShow = cardToShow.resize((80, 120))  # card size for game
                cardToShow = ImageTk.PhotoImage(cardToShow)
                cardToShowLabel = tk.Label(image=cardToShow)
                cardToShowLabel.image = cardToShow
                cardToShowLabel.grid(column=1 + self.hitTicker, row=1)
                doubleButton["state"] = "disabled"
                splitButton["state"] = "disabled"
                root.update()
                if buttonPressed == 3:
                    self.blackjack.playerHands.get(1).doubleDown()
                    break
        doubleButton["state"] = "disabled"
        splitButton["state"] = "disabled"
        standButton["state"] = "disabled"
        hitButton["state"] = "disabled"
        root.update()

        if not self.blackjack.playerHands.get(2) is None:
            self.value.set(0)
            self.blackjack.playerHands.get(2).setCard(self.blackjack.gameShoe.hit())
            card = self.blackjack.playerHands.get(2).cardsInHand.get(1)
            cardToShow = Image.open(card.image)
            cardToShow = cardToShow.resize((80, 120))  # card size for game
            cardToShow = ImageTk.PhotoImage(cardToShow)
            cardToShowLabelD = tk.Label(image=cardToShow)
            cardToShowLabelD.image = cardToShow
            cardToShowLabelD.grid(column=1, row=2)

            standButton = tk.Button(root, text="Stand", command=lambda: self.standButtonClicked(2))
            hitButton = tk.Button(root, text="Hit Hand", command=lambda: self.hitButtonClicked(2))
            doubleButton = tk.Button(root, text="Double Down", command=lambda: self.doubleButtonClicked(2, bet),
                                     state="disabled")
            splitButton = tk.Button(root, text="Split Hand", command=lambda: self.splitButtonClicked(root, 2, bet),
                                    state="disabled")
            standButton.grid(column=7, row=2)
            hitButton.grid(column=8, row=2)
            doubleButton.grid(column=9, row=2)
            splitButton.grid(column=10, row=2)
            root.update()
            time.sleep(.5)

            self.hitTicker = 0

            while not (self.value.get() == 1 or self.value.get() == 3):
                if self.blackjack.playerBustCheck(2):
                    self.value.set(1)
                    break
                enableDouble = self.blackjack.enableDouble(self.blackjack.playerHands.get(2))
                enableSplit = self.blackjack.enableSplit()
                if enableDouble and self.hitTicker == 0 and userMoney - (bet + self.totalBet) > 0:
                    doubleButton["state"] = "normal"
                if enableSplit and self.hitTicker == 0 and userMoney - (bet + self.totalBet) > 0:
                    splitButton["state"] = "normal"
                root.update()
                self.hitTicker += 1

                root.wait_variable(self.value)
                buttonPressed = self.value.get()
                if buttonPressed == 1:
                    break

                card = self.blackjack.playerHands.get(2).cardsInHand.get(1 + self.hitTicker)
                cardToShow = Image.open(card.image)
                cardToShow = cardToShow.resize((80, 120))  # card size for game
                cardToShow = ImageTk.PhotoImage(cardToShow)
                cardToShowLabel = tk.Label(image=cardToShow)
                cardToShowLabel.image = cardToShow
                cardToShowLabel.grid(column=1 + self.hitTicker, row=2)
                doubleButton["state"] = "disabled"
                splitButton["state"] = "disabled"
                root.update()
                if buttonPressed == 3:
                    self.blackjack.playerHands.get(2).doubleDown()
                    break
        doubleButton["state"] = "disabled"
        splitButton["state"] = "disabled"
        standButton["state"] = "disabled"
        hitButton["state"] = "disabled"
        root.update()

        if not self.blackjack.playerHands.get(3) is None:
            self.value.set(0)
            self.blackjack.playerHands.get(3).setCard(self.blackjack.gameShoe.hit())
            card = self.blackjack.playerHands.get(3).cardsInHand.get(1)
            cardToShow = Image.open(card.image)
            cardToShow = cardToShow.resize((80, 120))  # card size for game
            cardToShow = ImageTk.PhotoImage(cardToShow)
            cardToShowLabelD = tk.Label(image=cardToShow)
            cardToShowLabelD.image = cardToShow
            cardToShowLabelD.grid(column=1, row=3)

            standButton = tk.Button(root, text="Stand", command=lambda: self.standButtonClicked(3))
            hitButton = tk.Button(root, text="Hit Hand", command=lambda: self.hitButtonClicked(3))
            doubleButton = tk.Button(root, text="Double Down", command=lambda: self.doubleButtonClicked(3, bet),
                                     state="disabled")
            splitButton = tk.Button(root, text="Split Hand", command=lambda: self.splitButtonClicked(root, 3, bet),
                                    state="disabled")
            standButton.grid(column=7, row=3)
            hitButton.grid(column=8, row=3)
            doubleButton.grid(column=9, row=3)
            splitButton.grid(column=10, row=3)

            root.update()
            time.sleep(.5)

            self.hitTicker = 0

            while not (self.value.get() == 1 or self.value.get() == 3):
                if self.blackjack.playerBustCheck(3):
                    self.value.set(1)
                    break
                enableDouble = self.blackjack.enableDouble(self.blackjack.playerHands.get(3))
                if enableDouble and self.hitTicker == 0 and userMoney - (bet + self.totalBet) > 0:
                    doubleButton["state"] = "normal"
                splitButton["state"] = "disabled"
                root.update()
                self.hitTicker += 1

                root.wait_variable(self.value)
                buttonPressed = self.value.get()
                if buttonPressed == 1:
                    break

                card = self.blackjack.playerHands.get(3).cardsInHand.get(1 + self.hitTicker)
                cardToShow = Image.open(card.image)
                cardToShow = cardToShow.resize((80, 120))  # card size for game
                cardToShow = ImageTk.PhotoImage(cardToShow)
                cardToShowLabel = tk.Label(image=cardToShow)
                cardToShowLabel.image = cardToShow
                cardToShowLabel.grid(column=1 + self.hitTicker, row=3)

                root.update()
                if buttonPressed == 3:
                    self.blackjack.playerHands.get(3).doubleDown()
                    break
        doubleButton["state"] = "disabled"
        splitButton["state"] = "disabled"
        standButton["state"] = "disabled"
        hitButton["state"] = "disabled"
        root.update()

        # flip dealer card image and proceed to display dealer cards as it hits
        card = self.blackjack.dealerHand.cardsInHand.get(0)
        cardToShow = Image.open(card.image)
        cardToShow = cardToShow.resize((80, 120))  # card size for game
        cardToShow = ImageTk.PhotoImage(cardToShow)
        cardToShowLabelD = tk.Label(image=cardToShow)
        cardToShowLabelD.image = cardToShow
        cardToShowLabelD.grid(column=11, row=0)
        root.update()
        time.sleep(.5)

        hitTicker = 0
        while self.dealerHitChoice():
            hitTicker += 1
            card = self.blackjack.gameShoe.hit()
            self.blackjack.dealerHand.setCard(card)
            cardToShow = Image.open(card.image)
            cardToShow = cardToShow.resize((80, 120))  # card size for game
            cardToShow = ImageTk.PhotoImage(cardToShow)
            cardToShowLabel = tk.Label(image=cardToShow)
            cardToShowLabel.image = cardToShow
            cardToShowLabel.grid(column=11, row=1 + hitTicker)
            root.update()
            time.sleep(.5)

        index = 0
        self.playerBusted = 0
        self.vsLoss = 0
        self.vsPushes = 0
        self.vsWins = 0
        self.dealerBusted = 0
        self.blackjacks = 0
        winnings = 0
        for hand in self.blackjack.playerHands.values():
            result = self.winConditions(index)
            index += 1
            if result == 1:
                self.blackjacks += 1
                winnings += hand.bet * 1.5
            if result == 2:
                winnings += hand.bet
            if result == 3:
                winnings += hand.bet
            if result == 4:
                pass
            if result == 5:
                winnings -= hand.bet
            if result == 6:
                winnings -= hand.bet

        return winnings, self.blackjacks

