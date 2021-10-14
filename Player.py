from Grid import Grid

class Player:

    def __init__(self):
        self.gridShips = Grid()
        self.gridShots = Grid()

    def takeTurn(self, otherPlayer ):
        # over write in the HumanPlayer and ComputerPlayer subclasses
        # you need access to the otherPlayer (who is the computer or human)
        # this way you can access their grids to determine if you hit their ship
        pass

    def placeShip(self, ship , size ):
        # over write in the HumanPlayer and ComputerPlayer subclasses
        pass


    def createShipGrid(self):
        placeShip( "A" , 5 )
        placeShip( "B", 4 )
        placeShip( "C", 3 )
        placeShip( "S", 3 )
        placeShip( "D", 2 )

    def printGrids(self):
        print("Ship Grid")
        self.gridShips.printGrid()
        print("Shot Grid")
        self.gridShots.printGrid()
