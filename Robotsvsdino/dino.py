from unicodedata import name
from weapon import Weapon

class Dino: 
    def __init__(self,name,):
        self.nameone = name  
        self.health = '100'
        self.attack_power = Weapon('')
    pass
    def choose_name(self,name): 
        self.choose_name = ['littlefoot', 'duckie', 'petree', 'spike']
        print(input('What is your dino name?'))
        if input != self.choose_name: 
                print('Lame, try again')
        if input == 'sarah': 
            print(' No three horns allowed')
        pass
    def choose_weapon (self,attack_choiced): 
        attack_choiced = ['stomp', 'roar','headbut','charge']
        self.choose_weapon = attack_choiced
        print(input('Choose your attack'))
        print('Initiating', self.choose_weapon)
    pass
    def health_meter(self):
        self.health_meter == '100'
        print("Your health is currently:") 
        print(self.health_meter)
    pass 
    def attackpower_amount (self): 
        attackpower = ['10', '20','50','2']
        self.attackpower_amount = attackpower
        print(self.attackpower_amount)
    pass 