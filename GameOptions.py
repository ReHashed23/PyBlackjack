import tkinter as tk
from tkinter import *
import GameControl
from PIL import Image, ImageTk


class GameOptions:
    def __init__(self):
        self.winnings = 0
        self.blackjacks = 0

    def startGame(self, root, gameDeckCount, gameBet, cardBackings, userMoney):
        for ele in root.winfo_children():
            ele.destroy()
        self.game = GameControl.GameControl(gameDeckCount, cardBackings)
        self.winnings, self.blackjacks = self.game.game(root, gameBet, userMoney)
        self.gameControl.set(0)

    def defineConstraints(self, root, userMoney):
        for ele in root.winfo_children():
            ele.destroy()

        cardToShow1 = Image.open("PlayingCards/4/0.png")
        cardToShow1 = cardToShow1.resize((80, 120))  # card size for game
        cardToShow1 = ImageTk.PhotoImage(cardToShow1)
        cardToShowLabel1 = tk.Label(image=cardToShow1)
        cardToShowLabel1.grid(row=0, column=0)
        cardToShow2 = Image.open("PlayingCards/4/1.png")
        cardToShow2 = cardToShow2.resize((80, 120))  # card size for game
        cardToShow2 = ImageTk.PhotoImage(cardToShow2)
        cardToShowLabel2 = tk.Label(image=cardToShow2)
        cardToShowLabel2.grid(row=0, column=1)
        cardToShow3 = Image.open("PlayingCards/4/2.png")
        cardToShow3 = cardToShow3.resize((80, 120))  # card size for game
        cardToShow3 = ImageTk.PhotoImage(cardToShow3)
        cardToShowLabel3 = tk.Label(image=cardToShow3)
        cardToShowLabel3.grid(row=0, column=2)

        choice = IntVar()
        self.gameControl = IntVar()
        r1 = Radiobutton(root, text="Normal", variable=choice, value=0, state="active")
        r1.grid(row=1, column=0)
        r2 = Radiobutton(root, text="Vegeta and Goku", variable=choice, value=1)
        r2.grid(row=1, column=1)
        r3 = Radiobutton(root, text="Gogeta", variable=choice, value=2)
        r3.grid(row=1, column=2)

        betLabel = Label(text="Please input a number for your bet. You have $" + str(userMoney))
        betLabel.grid(row=2, column=1)
        betField = Entry()
        betField.grid(row=3, column=1)
        decksLabel = Label(text="Please input the number of decks in play.")
        decksLabel.grid(row=4, column=1)
        decksField = Entry()
        decksField.grid(row=5, column=1)
        self.confirmButton = tk.Button(root, text="Confirm Entries", command=lambda: self.startGame(root,
            int(decksField.get()), int(betField.get()), int(choice.get()), userMoney))
        self.confirmButton.grid(row=6, column=1)
        root.update()
        root.wait_variable(self.gameControl)
