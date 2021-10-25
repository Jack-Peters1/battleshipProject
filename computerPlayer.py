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

        if not otherPlayer.gridShips.isSpaceWater(startx, starty) and not otherPlayer.gridShips.returnLocation(startx, starty) == "O":
            self.gridShots.changeSingleSpace(startx, starty, "X")
            otherPlayer.gridShips.changeSingleSpace(startx, starty, "X")

        else:
            self.gridShots.changeSingleSpace(startx, starty, "O")
            otherPlayer.gridShips.changeSingleSpace(startx, starty, "O")

    def checkOverlapping(self, size, vOrH, rowStart, colStart):
        if vOrH == 0:
            for i in range(size):
                if not self.gridShips.isSpaceWater(i, colStart - 1):
                    return False
        elif vOrH == 1:
            for k in range(size):
                if not self.gridShips.isSpaceWater(rowStart-1, k):
                    return False
        return True

    def createShipGrid(self):
        self.placeShip("A", 5)
        self.placeShip("B", 4)
        self.placeShip("C", 3)
        self.placeShip("S", 3)
        self.placeShip("D", 2)

    def placeShip(self, ship, size):
        count = 1
        while count > 0:
            vOrH = random.randint(0, 1)
            colStart = random.randint(1, 10)
            rowStart = random.randint(1, 10)

            if 10 >= colStart >= 1 and 10 >= rowStart >= 1 and self.gridShips.isSpaceWater(rowStart - 1, colStart - 1):
                if vOrH == 0:
                    if rowStart - 1 + size <= 9 and self.checkOverlapping(size, vOrH, rowStart, colStart):
                        self.gridShips.changeCol(colStart - 1, ship, rowStart - 1, size)
                    else:
                        count += 1
                elif vOrH == 1:
                    if colStart - 1 + size <= 9 and self.checkOverlapping(size, vOrH, rowStart, colStart):
                        self.gridShips.changeRow(rowStart - 1, ship, colStart - 1, size)
                    else:
                        count += 1
                else:
                    count += 1
            else:
                count += 1
            count -= 1

        # this method will determine if the Player's ship grid still
        # has ships or not
        # If they have no ships left, the other player wins
        # This method returns true if they still have ships
        # This method returns false if they don't have ships
    def stillHasShips(self):
        for j in range(10):
            for k in range(10):
                if not self.gridShips.returnLocation(j, k) == "~" and not self.gridShips.returnLocation(j, k) == "X" and not self.gridShips.returnLocation(j, k) == "O":
                    return True
        return False

cpu = ComputerPlayer()
cpu.printGrids()
cpu.createShipGrid()
cpu.printGrids()

