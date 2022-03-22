#Model robot and pick name, weapon, healthmeter, random attack power

from unicodedata import name
from weapon import Weapon
class Robot:
    def __init__(self,name) -> None:
        self.robot = name
        self.health = '100'
        self.weapon = Weapon ('Blastergun','')
       
def choose_robot(self,name): 
    self.robot = name

def choose_weapon(self, name): 
    self.weapon = ('')
    print('Please select weapon for', name)
    
   
def health_meter(self): 
    self.health = '100'


def attack_methodr(self,dino): 
    dino.health -= self.weapon 
    print(f" {self.robot} attacked {self.dino}!")
    print(f" {self.dino} total health is now {dino.health}")


   