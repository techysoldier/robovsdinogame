#import files from herd and fleet to start battle ground 
from dino import attack_methodd, choose_dino
from herd import Herd
from fleet import Fleet
import random

from robot import attack_methodr, choose_robot

class Battlefield:
    def __init__(self):
        self.herd = Herd
        self.fleet = Fleet
        pass

def greeting(self): 
  print('Welcome to Robots vs Dinosours!')

  def run_battlefield_fight(self): 
    self.greeting()
    self.run_battleground
    pass 
   

def run_batleground(self):
    print(" Battle Royal Ready")
    self.go_dino()
    choose_dino = int("Which dino will battle first?")

    self.go_robo()
    choose_robot = int('Which Robot will activate?')
    
def start_battle(self): 
    go = [self.dino_go, self.robo_go]
    game_start = True 
    while game_start == True:
        if len(self.fleet.robot) <= len(self.herd.dino):
         self.go_robo()
        if len(self.herd.dino) <=  len(self.fleet.robot):
            self.go_dino
    
def dino_turn(self): 
    attack_methodd()
    if self.herd.dino[choose_dino].health <= 0: 
        print(f' Dino Extinct')
   

def robo_turn(self):
     attack_methodr()
     if self.fleet.robot[choose_robot].health <= 0: 
         print(f'Robot Eliminated')
    

def go_dino(self,dino): 
    dino_index = 0
    for dino in self.herd.dino:
        print(f" Press {dino.index} for {dino.name}")
    dino.index += 1 
    pass  

def go_robo(self, robot): 
    robo_index = 0
    for robot in self.fleet.robot:
        print(f" Press {robo_index} for {robot.name}")
    robot.index += 1 
    pass  

def the_winners(self): 
    print('And the winner is...')
    if len(self.fleet.robots) > 0:
            print('Robots Win!')
    else:
        print('Dinos Win!')