from Player import Player
import random

class ComputerPlayer(Player):

    def __init__(self):
        super().__init__()
    def takeTurn(self, otherPlayer):
        startx = random.randrange(0, 10)
        starty = random.randrange(0, 10)

        if not self.gridShots.isSpaceWater(startx, starty):
            self.takeTurn(otherPlayer)
        if not otherPlayer.gridShips.isSpaceWater(startx, starty):
            self.gridShots.changeSingleSpace(startx, starty, "X")
        else:
            self.gridShots.changeSingleSpace(startx, starty, "O")

    def createShipGrid(self):
        self.placeShip("A", 5)
        self.placeShip("B", 4)
        self.placeShip("C", 3)
        self.placeShip("S", 3)
        self.placeShip("D", 2)

    def placeShip(self, ship, size):
        rotate = random.randint(0, 1)
        startx = random.randrange(0, 10)
        starty = random.randrange(0, 10)

        if rotate == 0:
            for i in range(0, size):
                if (startx + i >= 9):
                    self.placeShip(ship, size)
                    return
                if not self.gridShips.isSpaceWater(startx + i, starty):
                    self.placeShip(ship, size)
                    return

            self.gridShips.changeRow(starty, ship, startx, size)

        if rotate == 1:
            for i in range(0, size):
                if (starty + i >= 9):
                    self.placeShip(ship, size)
                    return
                if not self.gridShips.isSpaceWater(startx, starty + i):
                    self.placeShip(ship, size)
                    return

            self.gridShips.changeCol(startx, ship, starty, size)

cpu = ComputerPlayer()
cpu.printGrids()
cpu.createShipGrid()
cpu.printGrids()

for i in range(100):
    cpu.takeTurn(cpu)
    cpu.printGrids()