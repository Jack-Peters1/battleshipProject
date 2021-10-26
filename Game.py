from HumanPlayer import *
from smartComputerPlayer import *

class Game:
    def __init__(self):
        self.p1 = HumanPlayer()
        self.cpu = smartComputerPlayer()

    def createGrids(self):
        self.cpu.createShipGrid()
        self.p1.createShipGrid()

    def main(self):
        self.createGrids()
        while self.p1.stillHasShips() and self.cpu.stillHasShips():
            self.p1.takeTurn(self.cpu)
            self.cpu.takeTurn(self.p1)
            self.p1.printGrids()

        if not self.p1.stillHasShips():
            print("You Lose")
            pass
        else:
            print("You Win")
            pass


g1 = Game()
g1.main()
