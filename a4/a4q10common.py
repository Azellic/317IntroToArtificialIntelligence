#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 4 Shared Classes Code

class MinMaxSearchResult(object):
    """Class used to return the results of a MinMax search.

    Variables:
    size - size of the gameboard
    utility - utility of the starting move
    start_action - the first move returned by the MinMax search
    time - time it took to finish the search
    """
    def __init__(self, size, utility, start_action, time):
        self.sz = size
        self.val = utility
        self.st_act = start_action
        self.t = time

    def __str__(self):
        """Make a nice mess"""
        prstr = ""
        prstr += str(self.sz) + "\t" + str(self.val) + "\t" + str(self.st_act) + "\t" + str(self.t)
        return prstr

class State:
    """A class representing the state of the board of queens at any point.

    Variables:
    queens: an array of numbers, representing the row of each queen in the
        column corresponding to the index
    action: the action which created this state.
    """
    def __init__(self, queens=[], action=None):
        self.Q = queens
        self.prev_act = action
        
