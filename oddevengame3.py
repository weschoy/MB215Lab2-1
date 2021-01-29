import random
from Game4 import Game

aChoices=["odd","even"]
class oddevengame3(Game):
    def __init__(self):
        Game.__init__(self)
        self.__nCurrent = -1
    def takeTurn(self, sInput):
        if(self.__nCurrent == -1):
            self.__nCurrent = 0
            return["Welcome to Odds and Even",
                   "Choose odd or even"]
                
        if sInput=="even":
            self.__nCurrent=1
            return["Computer is odd, please choose a number from 1 to 3"]

        elif sInput=="odd":
            self.__nCurrent=2
            return["Computer is even, please choose a number from 1 to 3"]
       
        elif(self.__nCurrent==1):
            self.Computer=random.randint(1,4)
            self.nAddition=int(sInput)+self.Computer
            if int(sInput)<1 or int(sInput)>3:
                return["Invalid input"]
            elif self.nAddition%2==0:
                self.__nCurrent=-1
                return["Computer chose: "+str(self.Computer),
                "Total is "+str(self.nAddition),
                "Therefore, you win!"
                ]
            else:
                self.__nCurrent=-1
                return["Computer chose: "+str(self.Computer),
                "Total is "+str(self.nAddition),
                "Therefore, you lose!"
                ]

        elif(self.__nCurrent==2):
            self.Computer=random.randint(1,4)
            self.nAddition=int(sInput)+self.Computer
            if int(sInput)<1 or int(sInput)>3:
                return["Invalid input"]
            elif self.nAddition%2==0:
                self.__nCurrent=-1
                return["Computer chose: "+str(self.Computer),
                "Total is "+str(self.nAddition),
                "Therefore, you lose!"
                ]
            else:
                self.__nCurrent=-1
                return["Computer chose: "+str(self.Computer),
                "Total is "+str(self.nAddition),
                "Therefore, you win!"
                ]

        else:
            return["Please choose even or odd"]

            
      
            

               