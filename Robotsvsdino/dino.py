from unicodedata import name
from weapon import Weapon
import random

class Dino: 
    def __init__(self,name,):
        self.nameone = name  
        self.health = '100'
        self.attack_power = Weapon('')

def choose_name(self,name): 
    self.choose_name = ['littlefoot', 'duckie', 'petree', 'spike']
    print(input('What is your dino name?'))
    if input == self.choose_name:
        print (random.choice(self.choose_name))
    elif input == 'sarah': 
        print(' No three horns allowed')
    else:
        print('Lame, try again')
    return self.choose_name


def chooseweapon (self,attack_choiced): 
    attack_choiced = ['stomp', 'roar','headbut','charge']
    self.chooseweapon = attack_choiced
    print(input('Choose your attack'))
    print('Initiating')
    print(random.choice (self.chooseweapon))
    return self.chooseweapon

def health_meter(self):
    self.health_meter == '100'
    print("Your health is currently:") 
    print(self.health_meter)
    return self.health_meter

def attackpower_amount (self): 
    attackpower = ['10', '20','50','2']
    self.attackpower_amount = attackpower
    print(random.choice(self.attackpower_amount))
    return self.attack_power
pass 

def dino_attack(self): 
    if self.chooseweapon == 'stomp':
        print(self.choose_name,'Stomp Stomp Stomp')
    elif self.chooseweapon == 'roar':
        print ('what a raoar')
    elif self.chooseweapon == 'headbut': 
        print(' Ouch what a hit')
    else: 
        print('CHARRRRGGGGGEEEE!!!!!')
    return self.chooseweapon