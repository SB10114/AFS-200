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

    def showDieFace(self):
        print(f'{dice.sides[self.getCurrentFaceValue()]} {self.getCurrentFaceValue()}', end= "")

def gamePlay():
    myDie = [dice(), dice(), dice(), dice(), dice()]
    
    for die in myDie:
        die.roll()
        die.showDieFace()
        

    # yahtzee = all(die.getCurrentFaceValue() == myDie[0].getCurrentFaceValue() for die in myDie)
    # return yahtzee
    
    # if yahtzee:
    #     print('YAHTZEE')

gamePlay()
