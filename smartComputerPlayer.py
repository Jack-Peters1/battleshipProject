from Player import Player
import random

class ComputerPlayer(Player):

    def __init__(self):
        super().__init__()
        self.firstHit = False
    def findFirstX(self):
        while True and self.firstHit:
            col = random.randint(0, 9)
            row = random.randint(0, 9)
            if(self.gridShots.returnLocation(row, col) == "X"):
                return [row, col]
        return [-1, -1]
    def takeTurn(self, otherPlayer):
        direction = random.randint(1, 4)
        startx = -1
        starty = -1

        smartShotInvalid = False

        if not self.firstHit:
            startx = random.randrange(0, 10)
            starty = random.randrange(0, 10)
        else:
            target = self.findFirstX()

            try:
                self.gridShots.isSpaceWater(target[0], target[1] - 1)
                self.gridShots.isSpaceWater(target[0], target[1] + 1)
                self.gridShots.isSpaceWater(target[0] - 1, target[1])
                self.gridShots.isSpaceWater(target[0] + 1, target[1])
            except:
                smartShotInvalid = True

            if smartShotInvalid or (self.gridShots.isSpaceWater(target[0], target[1] - 1) == False) and (self.gridShots.isSpaceWater(target[0], target[1] + 1) == False) and (self.gridShots.isSpaceWater(target[0] - 1, target[1]) == False) and (self.gridShots.isSpaceWater(target[0] + 1, target[1])  == False):
                startx = random.randrange(0, 10)
                starty = random.randrange(0, 10)
            elif(direction == 1): #up
                startx = target[0]
                starty = target[1] - 1
            elif (direction == 2):  # down
                startx = target[0]
                starty = target[1] + 1
            elif (direction == 3):  # left
                startx = target[0] - 1
                starty = target[1]
            elif (direction == 4):  # right
                startx = target[0] + 1
                starty = target[1]

        if not self.gridShots.isSpaceWater(startx, starty) or 0 > startx > 9 or 0 > starty > 9:
            self.takeTurn(otherPlayer)
        if not otherPlayer.gridShips.isSpaceWater(startx, starty):
            self.gridShots.changeSingleSpace(startx, starty, "X")
            self.firstHit = True
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
    print("Grid after turn ", i)