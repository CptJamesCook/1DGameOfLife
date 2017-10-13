"""The game entity."""
from CellularAutomaton import CellularAutomaton
import time

class Game(object):
    """Controls the number of cell automaton and what's printed to screen."""

    def __init__(self, rule, numLoops=12, initCond='0000000100000000', numCells=16):
        """Initialize self."""
        self.numLoops = numLoops
        if len(initCond) != numCells:
            # should raise error
            print("Warning: length of initial conditions not equal to "
                  "length of the number of cells.")
        self.cellList = []
        for x in range(0, numCells):
            cell = CellularAutomaton(rule)
            self.cellList.append(cell)
        for x in range(0, numCells):
            if (x == 0):
                self.cellList[0].lneighbor = self.cellList[numCells - 1]
                self.cellList[0].rneighbor = self.cellList[1]
            elif (x == numCells-1):
                self.cellList[numCells-1].lneighbor = self.cellList[numCells-2]
                self.cellList[numCells-1].rneighbor = self.cellList[0]
            else:
                self.cellList[x].lneighbor = self.cellList[x-1]
                self.cellList[x].rneighbor = self.cellList[x+1]
        for x in range(0, numCells):
            self.cellList[x].state = initCond[x]
        self.gameLoop()

    def gameLoop(self):
        """The game loop."""
        # print the starting case
        display = ''
        for cell in self.cellList:
            display += cell.state
        hstr = '%0*X' % ((len(display) + 3) // 4, int(display, 2))
        display += "\tHex Representation: " + hstr
        print(display)

        # print the rest of the simulation
        for x in range(0, self.numLoops-1):
            for cell in self.cellList:
                cell.chooseNextState()
            display = ''
            for cell in self.cellList:
                cell.update()
                display += cell.state
            hstr = '%0*X' % ((len(display) + 3) // 4, int(display, 2))
            display += "\tHex Representation: " + hstr
            print(display)
