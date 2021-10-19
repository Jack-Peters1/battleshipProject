from Player import Player
import random

class ComputerPlayer(Player):

    def __init__(self):
        super().__init__()
    def takeTurn(self, otherPlayer):

        startx = random.randrange(0, 10) #Randomly generate coordinates to shoot at
        starty = random.randrange(0, 10)

        if not self.gridShots.isSpaceWater(startx, starty): #If the spot has already been shot at, try again
            self.takeTurn(otherPlayer)

        if not otherPlayer.gridShips.isSpaceWater(startx, starty) and not otherPlayer.gridShips.returnLocation(startx, starty) == "O": #If the spot chosen to shoot at is a hit, mark it a hit on both boards
            self.gridShots.changeSingleSpace(startx, starty, "X")
            otherPlayer.gridShips.changeSingleSpace(startx, starty, "X")

        else: #Otherwise if it is a miss, mark it a miss on both boards
            self.gridShots.changeSingleSpace(startx, starty, "O")
            otherPlayer.gridShips.changeSingleSpace(startx, starty, "O")

    def checkOverlapping(self, size, vOrH, rowStart, colStart):
        if vOrH == 0: #If the ship is going vertical, check for vertical overlap
            for i in range(size):
                if not self.gridShips.isSpaceWater(i, colStart - 1): #If there is overlap, return false
                    return False
        elif vOrH == 1: #If the ship is going horizantal, check for horizantal overlap
            for k in range(size):
                if not self.gridShips.isSpaceWater(rowStart - 1, k): #If there is overlap, return false
                    return False
        return True #If no overlap is found, return True; the ship placement is valid

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

            if self.gridShips.isSpaceWater(rowStart - 1, colStart - 1): #Make sure you're shooting at water
                if vOrH == 0: #For vertical Ships
                    if rowStart - 1 + size <= 9 and self.checkOverlapping(size, vOrH, rowStart, colStart): #Make sure the ship is not overlapping or out of bounds
                        self.gridShips.changeCol(colStart - 1, ship, rowStart - 1, size)
                        self.printGrids()
                    else: #If the placement is invalid, the while loop does not stop and instead runs again
                        count += 1
                elif vOrH == 1: #For horizantal ships
                    if colStart - 1 + size <= 9 and self.checkOverlapping(size, vOrH, rowStart, colStart): #Make sure the ship is not overlapping or out of bounds
                        self.gridShips.changeRow(rowStart - 1, ship, colStart - 1, size)
                        self.printGrids()
                    else: #If the placement is invalid, the while loop does not stop and instead runs again
                        count += 1
            else: #If the shot location is invalid, the while loop does not stop and instead runs again
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
                if not self.gridShips.returnLocation(j, k) == "~" or not self.gridShips.returnLocation(j, k) == "X" or not self.gridShips.returnLocation(j, k) == "O": #If there are no letters left indicating another ship, end the code
                    return True
        return False

cpu = ComputerPlayer()
cpu.printGrids()
cpu.createShipGrid()
cpu.printGrids()

for i in range(100):
    cpu.takeTurn(cpu)
    cpu.printGrids()