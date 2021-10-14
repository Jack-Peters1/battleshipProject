from Player import *

class HumanPlayer(Player):

    def __init__(self):
        super().__init__()

    def placeShip(self, ship, size):
        count = 1
        while count>0:
            vOrH = str(input("Do you want ship " + ship + " vertically or horizontally? Enter V or H."))
            colStart = int(input("What column do you want ship " + ship + " to start in? 1-10."))
            rowStart = int(input("What row do you want ship " + ship + " to start in? 1-10."))

            if 10 >= colStart >= 1 and 10 >= rowStart >= 1:
                if self.gridShips.isSpaceWater(rowStart - 1, colStart - 1):
                    if vOrH == "V" or vOrH == "v":
                        if rowStart-1 + size <= 9:
                            self.gridShips.changeCol(colStart-1, ship, rowStart-1, size)
                        else:
                            print("Your ship goes out of bounds - please try again")
                            count+=1
                    elif vOrH == "H" or vOrH == "h":
                        if colStart-1 + size <= 9:
                            self.gridShips.changeRow(rowStart-1, ship, colStart-1, size)
                        else:
                            print("Your ship goes out of bounds - please try again")
                            count+=1
                    else:
                        print("Illegal value entered - try again.")
                        count+=1
                else:
                    print("Placement illegal, please try again")
                    count+=1
            else:
                print("Placement illegal, please try again")
                count+=1
            self.printGrids()
            count-=1



    def takeTurn(self, playerGrid):
        count = 1
        while count >0:
            colStart = int(input("What column do you want to take your shot in? 1-10."))
            rowStart = int(input("What row do you want to take your shot in? 1-10."))
            if colStart > 10 or rowStart > 10 or colStart < 1 or rowStart < 1:
                print("Illegal coordinates - Try again")
                count+=1
            elif playerGrid.gridShips.isSpaceWater(rowStart - 1, colStart - 1):
                self.gridShots.changeSingleSpace(self, rowStart-1, colStart-1, "0")
                print("Sorry! Your shot missed and landed in the water.")
            else:
                self.gridShots.changeSingleSpace(self, rowStart-1, colStart-1, "X")
                print("You got a hit!")
        count-=1
        pass

    def createShipGrid(self):
        self.placeShip( "A" , 5 )
        self.placeShip( "B", 4 )
        self.placeShip( "C", 3 )
        self.placeShip( "S", 3 )
        self.placeShip( "D", 2 )

player = HumanPlayer()
player.createShipGrid()