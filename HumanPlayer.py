from Player import *

class HumanPlayer(Player):

    def __init__(self):
        self.gridShips = Grid()
        self.gridShots = Grid()

    def placeShip(self, ship , size, vOrH, rowStart, colStart):
        if self.isPlacementLegal(self.gridShips, rowStart, colStart):
            if vOrH == "V":
                self.changeColumn(self, colStart, ship, rowStart, size)
            elif vOrH == "H":
                self.changeColumn(self, rowStart, ship, colStart, size)
        elif self.isPlacementLegal(self.gridShips, rowStart, colStart):
            pass

    def takeTurn(self):
        thing = 5



    count = 5
    while count>0:
        ship = str(input("What type of ship would you like to place first? A, B, C, D, or S?"))
        size = int(input("What size is that ship? 2, 3, 4, or 5?"))
        vOrH = str(input("Do you want your ship vertically or horizontally? Enter V or H."))
        rowStart = str(input("What row do you want your ship to start in? 1-10."))
        colStart = str(input("What column dop you want your ship to start in? 1-10."))
        placeShip(ship, size, vOrH, rowStart, colStart)
        count-=1


