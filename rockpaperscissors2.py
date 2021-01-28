import random
from Game4 import Game

aChoices=["rock","paper","scissors"]

class rockpaperscissors2(Game):
    def __init__(self):
        Game.__init__(self)
        self.__nCurrent=-1
    def computerChoose(self):
        global aChoices
        nChoice=random.randint(0,2)
        return aChoices[nChoice]
    def takeTurn(self,sInput):
        global aChoices
        if(self.__nCurrent == -1):
            self.__nCurrent=0
            self.sAI=random.choice(['rock','paper','scissors'])
            return["Welcome to a game of rock, paper, scissors!",
            "Choose rock, paper, or scissors!"
            ]
        
        else:
            sComputer=self.computerChoose()

            if sInput not in aChoices:
                return["Please enter rock, paper, or scissors"]
            elif sInput == "rock" and sComputer == "paper":
                return["Computer wins! Paper beats rock"]
            elif sInput == "rock" and sComputer == "rock":
                return["Nobody wins! You both chose rock!"]
            elif sInput == "paper" and sComputer == "scissors":
                return["Computer wins! Scissors beat paper"]
            elif sInput == "papers" and sComputer == "paper":
                sInput["Nobody wins! You both chose paper"]
            elif sInput == "scissors" and sComputer == "rock":
                return["computer wins! Rock beats scissors"]
            elif sInput == "scissors" and sComputer == "scissors":
                return["Nobody wins! You both chose scissors"]
            return["You win! You chose "+sInput,"The computer chose "+sComputer]