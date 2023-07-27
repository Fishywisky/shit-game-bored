import player


n = 1

def main():
    print('start the game'+'\n'+'enter the name of your caractere'+'\n')
    name =  input()
    print('Select your class betwen : Assassin, Mage, Clerf, Barbarian')
    Class = input()
    while Class not in ['Assassin', 'Mage', 'Clerf', 'Barbarian']:
        print('Please type your Class:  Assassin, Mage, Clerf, Barbarian')
        Class = input()
    Player1 = player.Player(name,Class)

    choise1 = player.action.DuoChoise('do you want to go lef?','Or do you prefer to stay in position?')
    choise1.displayChoises()
    choise1.actionReactionChoise(Player1.position.sety(-10),None)
    Player1.position.displayPosition()
    
if __name__ == '__main__':
    main()