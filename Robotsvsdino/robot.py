from unicodedata import name
from weapon import Weapon
import random
class Robot:
    def __init__(self,name) -> None:
        self.robot == name
        self.health == '100'
        Weapon == Weapon
  

    def robo_name(self, name):
        name = ['terminator', 'R2D2', "R5D4", 'AXL']
        self.robo_name == name
        print(name)



    def choose_weapon (self,attack_choicer): 
        attack_choicer = ['blaster', 'rocket launcher','muay thai kick','overload']
        self.choose_weapon = attack_choicer
        print(input('Choose your attack'))
        if input == 'blaster':
            print('Initiating', input)
        elif input == 'rocketlauncher':
            print('Initiating', input)
        elif input == 'muay thai kick':
            print('Initiating', input)
        else: 
            print('Initiating, Overload!!')


    def health_meter(self):
        self.health_meter == '100'
        print("Your health is currently:") 
        print(self.health_meter)
    pass 

    def attackpower_amount (self): 
        attackpower = ['10', '20','50','2']
        self.attackpower_amount = attackpower
        print(random.choice(self.attackpower_amount))
        return self.attackpower_amount
pass 

