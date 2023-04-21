import LogData
import GameOptions
from tkinter import *


class Program:
    def __init__(self):
        self.game = GameOptions.GameOptions()
        self.log = LogData.LogData()
        self.root = Tk(className=" Kyle's Blackjack Simulator")

    def accountCheck(self):
        self.root.update()
        userName = self.userNameEntry.get("1.0", "end-1c")
        userMoney = self.log.getUserData(userName)
        self.game.defineConstraints(self.root, userMoney)
        self.log.setUserData(userName, self.game.winnings, self.game.blackjacks)

    def gatherUserData(self):
        checkComplete = IntVar()
        checkComplete.set(0)
        userNamePrompt = Label(text="Please enter your User Name below")
        userNamePrompt.grid()
        self.userNameEntry = Text(self.root, height=1, width=20)
        self.userNameEntry.grid()
        enterButton = Button(self.root, text="Confirm Entries", command=lambda: self.accountCheck())
        enterButton.grid()
        self.root.mainloop()
