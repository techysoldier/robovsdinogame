#import robot file to create fleet 
from robot import Robot


class Fleet:
    def __init__(self) :
        self.fleet = []
        self.create_fleet()

def create_fleet(self): 
    terminator = Robot('terminator', 30)
    self.robot.append(terminator)
    r2d2 = Robot('R2D2', 50)
    self.robot.append(r2d2)
    r5d4 =  Robot('R5D4', 22)
    self.robot.append(r5d4)
    axl = Robot('AXL', 100)
    self.robot.append(axl)
    pass