import action

class Player:

    def __init__(self,name,Class):
        self.name = name
        self.Class = Class
        self.position = action.Move()  
        if self.Class == 'Mage':
            self.MP = 150
            self.HP = 750
            self.Atk = 200
        elif self.Class == 'Assassin':
            self.MP = 75
            self.HP = 1000
            self.Atk = 250
        elif self.Class == 'Clerf':
            self.MP = 100
            self.HP = 1750
            self.Atk = 100
        elif self.Class == 'Barbarian':
            self.MP = 25
            self.HP = 2500
            self.Atk = 150


# _________________________Accesseur Accesseur__________________________

    def getClass(self):
        return self.Class

    def getMP(self):
        return self.MP

    def getHP(self):
        return self.HP  
    
    def getAtk(self):
        return self.Atk

    def getName(self):
        return self.name
    
    def getPOsition(self):
        return self.position
    
    
# _________________________Accesseur Mutateur__________________________
    
    def setClass(self,new):
        self.Class = new

    def setMP(self,new):
        self.MP = new

    def setHP(self,new):
        self.HP = new
    
    def setAtk(self,new):
        self.Atk = new

    def setName(self,new):
        self.name = new
