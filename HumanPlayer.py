from Player import *

class HumanPlayer(Player):

    def __init__(self):
        super().__init__()

    def checkOverlapping(self, size, vOrH, rowStart, colStart):
        if vOrH == "V" or vOrH == "v":
            for i in range(size):
                if not self.gridShips.isSpaceWater(i, colStart - 1):
                    return False
        elif vOrH == "H" or vOrH == "h":
            for k in range(size):
                if not self.gridShips.isSpaceWater(rowStart-1, k):
                    return False
        return True


    def placeShip(self , ship , size):
        count = 1
        while count>0:
            vOrH = str(input("Do you want ship " + ship + " vertically or horizontally? Enter V or H."))
            colStart = int(input("What column do you want ship " + ship + " to start in? 1-10."))
            rowStart = int(input("What row do you want ship " + ship + " to start in? 1-10."))

            if 10 >= colStart >= 1 and 10 >= rowStart >= 1 and self.gridShips.isSpaceWater(rowStart - 1, colStart - 1):
                if vOrH == "V" or vOrH == "v":
                    if rowStart-1 + size <= 9 and self.checkOverlapping(size, vOrH, rowStart, colStart):
                        self.gridShips.changeCol(colStart-1, ship, rowStart-1, size)
                        self.printGrids()
                    else:
                        print("Your ship goes out of bounds or is overlapping - please try again")
                        count += 1
                elif vOrH == "H" or vOrH == "h":
                    if colStart-1 + size <= 9 and self.checkOverlapping(size, vOrH, rowStart, colStart):
                        self.gridShips.changeRow(rowStart-1, ship, colStart-1, size)
                        self.printGrids()
                    else:
                        print("Your ship goes out of bounds or is overlapping - please try again")
                        count += 1
                else:
                    print("Illegal value entered - try again.")
                    count += 1
            else:
                print("Placement illegal, please try again")
                count += 1
            count -= 1


    def takeTurn(self, playerGrid):
        count = 1
        if not self.stillHasShips():
            print("Sorry! all your ships have sunk and the game is over.")
            pass
        if not playerGrid.stillHasShips():
            print("You have won and sunk all opponent ships!")
            pass

        while count >0:
            colStart = int(input("What column do you want to take your shot in? 1-10."))
            rowStart = int(input("What row do you want to take your shot in? 1-10."))
            if colStart > 10 or rowStart > 10 or colStart < 1 or rowStart < 1:
                print("Illegal coordinates - Try again")
                count += 1

            if playerGrid.gridShips.isSpaceWater(rowStart - 1, colStart - 1):
                self.gridShots.changeSingleSpace(self, rowStart-1, colStart-1, "0")
                print("Sorry! Your shot missed and landed in the water.")
            else:
                self.gridShots.changeSingleSpace(self, rowStart-1, colStart-1, "X")
                print("You got a hit!")
                ship = playerGrid.gridShips.returnLocation(rowStart-1, colStart-1)
                playerGrid.gridShips.changeSingleSpace(self, rowStart-1, colStart-1, "X")
                count = 0
                for i in range(10):
                    for j in range(10):
                        if playerGrid.gridShips.returnLocation(i, j) == ship:
                            count+=1
                if count == 0:
                    if ship == "A" or ship == "a":
                        print("You sunk the enemies Aircraft Carrier!")
                    elif ship == "B" or ship == "b":
                        print("You sunk the enemies Battleship!")
                    elif ship == "C" or ship == "c":
                        print("You sunk the enemies Cruiser!")
                    elif ship == "D" or ship == "d":
                        print("You sunk the enemies Destroyer!")
                    elif ship == "S" or ship == "s":
                        print("You sunk the enemies Submarine!")
            count-=1



    # this method will determine if the Player's ship grid still
    # has ships or not
    # If they have no ships left, the other player wins
    # This method returns true if they still have ships
    # This method returns false if they don't have ships
    def stillHasShips(self):
        for j in range(10):
            for k in range(10):
                if not self.gridShips.returnLocation(j, k) == "~" or not self.gridShips.returnLocation(j, k) == "X":
                    return True
        return False





    def createShipGrid(self):
        self.placeShip( "A" , 5 )
        self.placeShip( "B", 4 )
        self.placeShip( "C", 3 )
        self.placeShip( "S", 3 )
        self.placeShip( "D", 2 )

player = HumanPlayer()
player.createShipGrid()