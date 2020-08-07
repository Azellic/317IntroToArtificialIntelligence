#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 4 Variation 1b

from random import getrandbits, randint
from a4q10common import *

class Game:
    """The game class, provides methods for working with and modifying a
    state representing a board of size N which can have N queens

    Variables:
    size: the size of the game (chess) board
    """
    def __init__(self, size):
        self._sz = size
        self.start_state = State()

    """Returns true if there are no actions available from given state"""
    def is_terminal(self, state):
        if self.actions(state):
            return False
        return True

    """The utility of a terminal node, depending on who's turn it is"""
    def utility(self, state):
        if self.is_mins_turn(state):
            return len(state.Q)
        else:
            return - len(state.Q)

    """Returns true if depth is greater than the cutoff point, false
    otherwise"""
    def cutoff_test(self, state, depth, cutoff):  #Only used in cutoff search
        if depth > cutoff:
            return True
        return False

    """Calculates an estimated utility for non-terminal node at cutoff depth."""
    def eval(self, state):          #Only used in cutoff search
        val = len(state.Q) + (len(self.actions(state)) / 2.5 )
        if round(val) % 2 == 0:
            return val
        else:
            return -val

    """Returns playable index for the left-most empty column in list form."""
    def actions(self, state):
        posibilities = [p for p in range(0, self._sz)]
        for i in range(0, len(state.Q)):
            if state.Q[i] in posibilities: posibilities.remove(state.Q[i])
            dif = len(state.Q) - i
            diag_d = state.Q[i]+ dif
            diag_u = state.Q[i]- dif
            if diag_d in posibilities: posibilities.remove(diag_d)
            if diag_u in posibilities: posibilities.remove(diag_u)
        return posibilities

    """Applys the action to the state and returns a new state"""
    def result(self, state, action):
        new_state = State(list(state.Q), action)
        new_state.Q.append(action)
        return new_state

    """If the number of queens on the board is even, it is Max's turn"""
    def is_maxs_turn(self, state):
        #Implementation optional
        return len(state.Q) % 2 == 0

    """If the number of queens on the board is odd, it is Min's turn"""
    def is_mins_turn(self, state):
        return not len(state.Q) % 2 == 0
