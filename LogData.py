import os.path


class LogData:
    def __init__(self):
        self.userMoney = 0
        self.userResets = 0
        self.userBlackjacks = 0

    def getUserData(self, userName):

        if os.path.exists("BlackjackProfiles/" + userName + ".txt"):
            userFile = open("BlackjackProfiles/" + userName + ".txt", "r")
            index = 0
            for line in userFile.readlines():
                if index == 0:
                    self.userMoney = int(line.strip())
                if index == 1:
                    self.userBlackjacks = int(line.strip())
                if index == 2:
                    self.userResets = int(line.strip())
                index += 1
            userFile.close()
            return self.userMoney
        else:
            userFile = open("BlackjackProfiles/" + userName + ".txt", "w")
            self.userMoney = 1000
            self.userBlackjacks = 0
            self.userResets = 0
            userFile.writelines(str(self.userMoney) + "\n")
            userFile.writelines(str(self.userBlackjacks) + "\n")
            userFile.writelines(str(self.userResets) + "\n")
            userFile.close()
            return self.userMoney

    def setUserData(self, userName, money, blackjacks):
        self.userMoney += money
        self.userBlackjacks += blackjacks
        if self.userMoney <= 0:
            self.userMoney = 1000
            self.userBlackjacks = 0
            self.userResets += 1
        userFile = open("BlackjackProfiles/" + userName + ".txt", "w")
        userFile.writelines(str(self.userMoney) + "\n")
        userFile.writelines(str(self.userBlackjacks) + "\n")
        userFile.writelines(str(self.userResets) + "\n")
        userFile.close()
