from Player import *

class HumanPlayer(Player):

    def __init__(self):
        super().__init__()

    def placeShip(self):
        count = 5
        while count>0:
            ship = str(input("What type of ship would you like to place (Only one per type)? A(5), B(4), C(3), D(2), or S(3)?"))
            vOrH = str(input("Do you want your ship vertically or horizontally? Enter V or H."))
            colStart = int(input("What column do you want your ship to start in? 1-10."))
            rowStart = int(input("What row dop you want your ship to start in? 1-10."))
            if ship == "A" or ship == "a":
                size = 5
            elif ship == "B" or ship == "b":
                size = 4
            elif ship == "S" or ship == "C" or ship == "s" or ship == "c":
                size = 3
            elif ship == "D" or ship == "d":
                size = 2

            if self.isPlacementLegal(self.gridShips.grid, rowStart - 1, colStart - 1):
                if vOrH == "V" or vOrH == "v":
                    self.gridShips.changeCol(colStart-1, ship, rowStart-1, size)
                elif vOrH == "H" or vOrH == "h":
                    self.gridShips.changeRow(rowStart-1, ship, colStart-1, size)
            else:
                print("Placement illegal, please try again")
                count+=1
            count-=1

player = HumanPlayer()
player.placeShip()