from HumanPlayer import *
from computerPlayer import *
from Player import *

class Game:
    def __init__(self):
        self.p1 = HumanPlayer()
        self.cpu = ComputerPlayer()

    def createGrids(self):
        self.cpu.createShipGrid()
        self.p1.createShipGrid()



