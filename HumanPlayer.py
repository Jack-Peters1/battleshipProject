from Player import *

class HumanPlayer(Player):

    def __init__(self):
        super().__init__()

    # this helper method checks if there are any overlaps when placing a ship
    #takes the size of ship, orientation, row and column start
    def checkOverlapping(self, size, vOrH, rowStart, colStart):
        if vOrH == "V" or vOrH == "v": #if vertical, check veritcaly for overlaps
            for i in range(size): #traverse grid based on ship size
                if not self.gridShips.isSpaceWater(i + rowStart -1, colStart - 1): # if there is an overlap, return false
                    return False
        elif vOrH == "H" or vOrH == "h": #if horozontal, check for overlaps.
            for k in range(size): # traverse grid based on ship size
                if not self.gridShips.isSpaceWater(rowStart-1, k + colStart - 1): # if there is an overlap return false
                    return False
        return True

    #places a ship, asks user where they want to place it and everything
    #gets type of ship and size
    def placeShip(self , ship , size):
        count = 1
        if ship == "A" or ship == "a": # just sets variable to the actual ship name
            shipName = "Aircraft Carrier"
        elif ship == "B" or ship == "b":
            shipName = "Battleship"
        elif ship == "C" or ship == "c":
            shipName = "Cruiser"
        elif ship == "D" or ship == "d":
            shipName = "Destroyer"
        elif ship == "S" or ship == "s":
            shipName = "Submarine"

        while count > 0: #main while loop for placing ships
            vOrH = str(input("Do you want your " + shipName + " vertically or horizontally? Enter V or H."))
            colStart = int(input("What column do you want your " + shipName + " to start in? 1-10."))
            rowStart = int(input("What row do you want your " + shipName + " to start in? 1-10."))

            #first checks if input is valid
            if 10 >= colStart >= 1 and 10 >= rowStart >= 1 and self.gridShips.isSpaceWater(rowStart - 1, colStart - 1):
                if vOrH == "V" or vOrH == "v": #if input is valid, check if vertical is wanted
                    if rowStart-1 + size <= 9 and self.checkOverlapping(size, vOrH, rowStart, colStart): #check if it goes out of bounds and is not overlapping
                        self.gridShips.changeCol(colStart-1, ship, rowStart-1, size)
                        self.printGrids()
                    else: #prompt user to restart, add 1 to count
                        print("Your ship goes out of bounds or is overlapping - please try again")
                        count += 1
                elif vOrH == "H" or vOrH == "h": # if horozontal
                    if colStart-1 + size <= 9 and self.checkOverlapping(size, vOrH, rowStart, colStart): # check if out of bounds or overlapping
                        self.gridShips.changeRow(rowStart-1, ship, colStart-1, size)
                        self.printGrids()
                    else: #if invalid, prompt to restart this ship and add 1 to count
                        print("Your ship goes out of bounds or is overlapping - please try again")
                        count += 1
                else: # if user entered something besides V v H or h
                    print("Illegal value entered - try again.")
                    count += 1
            else: # if a invalid location was entered
                print("Placement illegal, please try again")
                count += 1
            count -= 1

    # asks the player where they want to shoot
    def takeTurn(self, playerGrid):
        count = 1
        if not self.stillHasShips(): # checks if game is over
            print("Sorry! all your ships have sunk and the game is over.")
            pass
        if not playerGrid.stillHasShips(): # checks if game is over
            print("You have won and sunk all opponent ships!")
            pass

        while count >0: # main while loop to ask where they want to shoot
            colStart = int(input("What column do you want to take your shot in? 1-10."))
            rowStart = int(input("What row do you want to take your shot in? 1-10."))
            if colStart > 10 or rowStart > 10 or colStart < 1 or rowStart < 1: # check for legal coordinates
                print("Illegal coordinates - Try again")
                count += 1
            elif playerGrid.gridShips.isSpaceWater(rowStart - 1, colStart - 1): # checks if the player missed and sets values
                self.gridShots.changeSingleSpace(self, rowStart-1, colStart-1, "O")
                playerGrid.gridShips.changeSingleSpace(self, rowStart-1, colStart-1, "O")
                print("Sorry! Your shot missed and landed in the water.")
            else: # if player got a hit, change values and then check if it was sunk
                self.gridShots.changeSingleSpace(self, rowStart-1, colStart-1, "X")
                print("You got a hit!")
                shipTemp = playerGrid.gridShips.returnLocation(rowStart-1, colStart-1)
                playerGrid.gridShips.changeSingleSpace(self, rowStart-1, colStart-1, "X")
                count2 = 0
                for i in range(10): # traverse opponent ship grid and check if a ship was sunk
                    for j in range(10):
                        if playerGrid.gridShips.returnLocation(i, j) == shipTemp:
                            count2 += 1
                if count2 == 0: # if something was sunk
                    if shipTemp == "A" or shipTemp == "a": # see which ship was sunk
                        print("You sunk the enemies Aircraft Carrier!")
                    elif shipTemp == "B" or shipTemp == "b":
                        print("You sunk the enemies Battleship!")
                    elif shipTemp == "C" or shipTemp == "c":
                        print("You sunk the enemies Cruiser!")
                    elif shipTemp == "D" or shipTemp == "d":
                        print("You sunk the enemies Destroyer!")
                    elif shipTemp == "S" or shipTemp == "s":
                        print("You sunk the enemies Submarine!")
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
