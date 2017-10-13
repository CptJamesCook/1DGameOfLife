"""Run a sample game."""
from Rule import Rule
from CellularAutomaton import CellularAutomaton
from Game import Game

if __name__ == "__main__":
    rule = Rule(30)
    game = Game(rule, numLoops=12)
