

class PlayerCharacter:

    def __init__(self,startXP=0):
        self._charStartingXP = startXP
        self._charXP = self._charStartingXP
        self._charLevel = self.calcLevel()

    def __str__(self):
        return "object is a level " + str(self._charLevel)

    def calcLevel(self):
        totalXP = self._charXP
        levelResult = 1
        for number in range(20):
            if totalXP >= ( ( number + 1 ) * 1000 ):
                print(number)
                levelResult = number
        return levelResult        

    
        
