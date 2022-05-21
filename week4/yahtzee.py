import random 

class dice:
    sides = ['🎲', '⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

    def __init__(self, sides= 6):
        self.sideNumber = sides
        self.firstFace = 1
        
    def roll(self):
        self.firstFace = random.randint(1, self.sideNumber)
        return self.sideNumber

    def getCurrentFaceValue(self):
        return self.firstFace

    def showDiceFace(self):
        print(f'{dice.sides[self.getCurrentFaceValue()]} {self.getCurrentFaceValue()}', end= "")

def gamePlay():
    myDice = [dice(), dice(), dice(), dice(), dice()]
    
    for die in myDice:
       die.roll()
       die.showDiceFace()
        

    yahtzee = all(die.getCurrentFaceValue() == myDice[0].getCurrentFaceValue() for die in myDice)
    
    
    if yahtzee:
        print('YAHTZEE')

gamePlay()
