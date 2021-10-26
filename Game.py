from HumanPlayer import *
from smartComputerPlayer import *

p1 = HumanPlayer()
cpu = smartComputerPlayer()

def createGrids():
    cpu.createShipGrid()
    p1.createShipGrid()

def main():
    createGrids()
    while p1.stillHasShips() and cpu.stillHasShips(): #Continue the game until someone has lost
        p1.takeTurn(cpu)
        cpu.takeTurn(p1)
        p1.printGrids()

    if not p1.stillHasShips(): #If the player is out of ships, he loses
        print("You Lose")
        pass
    else: #Otherwise, he wins
        print("You Win")
        pass

main()