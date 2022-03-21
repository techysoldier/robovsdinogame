from unicodedata import name
from weapon import Weapon

class Dino: 
    def __init__(self,name,):
        self.name = name  
        self.health = '100'
        self.attack_power = Weapon('')
    pass
    def choose_name(self): 
        name = ['littlefoot', 'duckie', 'petree', 'spike']
        print(input('What is your dino name?'))
        if input != name: 
                print('Lame, try again')
        if input == 'sarah': 
            print(' No three horns allowed')
        pass
    def choose_weapon (attack_choiced): 
        attack_choiced = ['stomp', 'roar','headbut','charge']
        print(input('Choose your attack'))
        print('Initiating', attack_choiced)
    pass
    def health_meter(self, health):
        health == '100'
        print("Your health is currently:") 
        print(health)
    pass 


