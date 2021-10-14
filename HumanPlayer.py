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
            if self.isPlacementLegal(self.gridShips.grid, rowStart - 1, colStart - 1):
                if vOrH == "V" or vOrH == "v":
                    self.gridShips.changeCol(colStart-1, ship, rowStart-1, size)
                elif vOrH == "H" or vOrH == "h":
                    self.gridShips.changeRow(rowStart-1, ship, colStart-1, size)
            else:
                print("Placement illegal, please try again")
                count+=1
            self.printGrids()
            count-=1

    def takeTurn(self):
        colStart = int(input("What column do you want to take your shot in?"))
        rowStart = int(input("What row do you want to take your shot in?"))
        self.gridShots.changeSingleSpace(self, rowStart, colStart, "X")

        pass

    def createShipGrid(self):
        self.placeShip( "A" , 5 )
        self.placeShip( "B", 4 )
        self.placeShip( "C", 3 )
        self.placeShip( "S", 3 )
        self.placeShip( "D", 2 )

player = HumanPlayer()
player.createShipGrid()