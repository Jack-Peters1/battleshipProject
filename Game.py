from HumanPlayer import *
from smartComputerPlayer import *

p1 = HumanPlayer()
cpu = smartComputerPlayer()

def createGrids():
    cpu.createShipGrid()
    p1.createShipGrid()

def main():
    createGrids()
    while p1.stillHasShips() and cpu.stillHasShips():
        p1.takeTurn(cpu)
        cpu.takeTurn(p1)
        p1.printGrids()

    if not p1.stillHasShips():
        print("You Lose")
        pass
    else:
        print("You Win")
        pass

main()