
import item


class Move:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.distance = self.get_distance()

    def get_distance(self):
        return self.x + self.y

    def displayPosition(self):
        print('x:'+str(self.getx()) , 'y:'+str(self.gety()))

# _________________________Accesseur Accesseur__________________________

    def getx(self):
        return self.x

    def gety(self):
        return  self.y
    
    def getDistance(self):
        return self.distance
    
# _________________________Accesseur Mutateur__________________________
    
    def setx(self,new):
        self.x = self.x + new

    def sety(self,new):
        self.y = self.y + new

    
    def setDistance(self,new):
        self.distance = new



class DuoChoise:
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
        self.choise1 = False
        self.choise2 = False

    def displayChoises(self):
        while(1):
            print(self.number1+'\n'+self.number2+'\n'+'select choise 1 by entering 1 and choise number 2 by entering 2')
            choiseSelected = input()
            if choiseSelected == '1':
                self.choise1 = True
                return self.choise1
            elif choiseSelected == '2':
                self.choise2 = True
                return self.choise2
    
    def actionReactionChoise(self,do1,do2):
        if self.choise1 == True:
            do1
        elif self.choise2 == True:
            do2
        else:
            return None



# _________________________Accesseur Accesseur__________________________

    def getNumber1(self):
        return self.number1
    
    def getNumber2(self):
        return self.number2
    
# _________________________Accesseur Mutateur__________________________
    
    def setNumber1(self,new):
        self.number1 = new

    
    def setNumber2(self,new):
        self.number2 = new

        