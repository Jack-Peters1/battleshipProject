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

    def main(self):
        self.createGrids()
        while self.p1.stillHasShips() or self.cpu.stillHasShips():
            self.p1.takeTurn(self.cpu)
            self.cpu.takeTurn(self.p1)
            self.p1.printGrids()

        if( not self.p1.stillHasShips()):
            print("You Lose")
        else:
            print("You Win")


g1 = Game()
g1.main()


