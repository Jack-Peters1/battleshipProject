from Player import Player
import random

class ComputerPlayer(Player):

    def __init__(self):
        print("sus")

        super().__init__()

    def createShipGrid(self):
        self.placeShip( "A", 5)
        self.placeShip( "B", 4 )
        self.placeShip( "C", 3 )
        self.placeShip( "S", 3 )
        self.placeShip( "D", 2 )

    def placeShip(self, ship, size):
        rotate = random.randint(0, 1)
        startx = random.randrange(1, 10)
        starty = random.randrange(1, 10)

        if rotate == 0:
            for i in range(0, size):
                if (startx + i >= 9):
                    self.placeShip(ship, size)
                    return
                if self.isPlacementLegal(self.gridShips.grid, startx + i, starty) == False:
                    self.placeShip(ship, size)
                    return

            for i in range(0, size):
                self.gridShips.changeSingleSpace(startx + i, starty, ship)

        if rotate == 1:
            for i in range(0, size):
                if (starty + i >= 9):
                    self.placeShip(ship, size)
                    return
                if self.isPlacementLegal(self.gridShips.grid, startx, starty + i) == False:
                    self.placeShip(ship, size)
                    return

            for i in range(0, size):
                self.gridShips.changeSingleSpace(startx, starty + i, ship)

cpu = ComputerPlayer()
cpu.printGrids()
cpu.createShipGrid()
cpu.printGrids()