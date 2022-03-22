#import files from herd and fleet to start battle ground 
from dino import attack_methodd, choose_dino
from herd import Herd
from fleet import Fleet
from robot import attack_methodr, choose_robot

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()
      

def run_game(self): 
    self.greeting_dis()
    self.run_battleground
    
   
def greeting_dis(self): 
        print('Welcome to Robots vs Dinosours!')


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
    dino.herd_index = 0
    for dino in self.herd.dino:
        print(f" Press {dino.herd_index} for {dino.name}")
    dino.herd_index += 1 
     

def go_robo(self, robot): 
    robot_fleet_index = 0
    for robot in self.fleet.robot:
        print(f" Press {robot_fleet_index} for {robot.name}")
    robot.fleet_index += 1 
     

def the_winners(self): 
    print('And the winner is...')
    if len(self.fleet.robot) > 0:
            print('Robots Win!')
    else:
        print('Dinos Win!')