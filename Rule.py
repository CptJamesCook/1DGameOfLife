"""The rule for whether a cell lives or dies."""

class Rule(object):
    """The rule for whether a cell lives or dies."""

    def __init__(self, num):
        """Initialize self."""
        self.situationState = {}
        self.setRules(num)

    def __str__(self):
        """The string method for the class."""
        classStr = "\n"
        for key, val in self.situationState.items():
            classStr += "situation: " + key + "\n" \
                      + "Next state: " + val + "\n\n"
        return classStr

    def setRules(self, num):
        """
        Set the rules of the game based on the number passed in.

        Each bit of a number corresponds to the outcome of one of 8 situations.
        The next state of each cell depends on both the current state of the
        cell and the current state of each neighbor, meaning there is 2**3, 8,
        possible situations.
        """
        situations = ['111', '110', '101', '100', '011', '010', '001', '000']
        binNum = bin(num)[2:]
        while (len(binNum) < 8):
            binNum = '0' + binNum
        for i in range(0, 8):
            self.situationState[situations[i]] = binNum[i]

    def nextState(self, cell):
        """Choose the next state of the cellular automaton."""
        return self.situationState[cell.lneighbor.state
                                 + cell.state
                                 + cell.rneighbor.state]
