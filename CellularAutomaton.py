"""A cell that lives or dies based on the neighborhood conditions."""

class CellularAutomaton(object):
    """A cell that lives or dies based on neighborhood conditions."""

    def __init__(self, rule, state='0', nextState='0',
                             lneighbor='0', rneighbor='0'):
        """Initialize self."""
        self.rule = rule
        self.state = state
        self.nextState = nextState
        self.lneighbor = lneighbor
        self.rneighbor = rneighbor

    def __str__(self):
        """The string method of the class."""
        return "Left neighbor: " + str(self.lneighbor) + "\n"   \
             + "Right neighbor: " + str(self.rneighbor) + "\n"  \
             + "Current state: " + str(self.state)

    def chooseNextState(self):
        """Choose the next state of the automaton."""
        self.nextState = self.rule.nextState(self)

    def update(self):
        """Update the current state of the cell."""
        self.state = self.nextState
