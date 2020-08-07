#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 3 Question 2

from A1Search import Search, SearchResult
import copy

class Variable(object):
    """A variable for representing a single cell in the Latin Square

    Keyword Arguments:
    val -- The value of the cell, if assigned
    domain -- The possible values for a variable, empty if assigned
    """
    def __init__(self, val=None, domain=[]):
        self.cur_val = val
        self.dom = domain

    """Assign a value to a variable, emptying its domain"""
    def assign(self, val):
        self.cur_val = val
        self.dom = []

    """Make a nice mess"""
    def __str__(self):
        prstr="Value:" + str(self.cur_val) + "    \tDomain:" + str(self.dom)
        return prstr

class State:
    """Represents a state with variables and blanks

    Keyword Arguments:
    size -- the length/width of the square
    square -- the square itself, as an array of arrays or 2d array
    """
    def __init__(self, size, square):
        self.collection = {}
        self.blanks = []
        self.sz = size
        for r in range(0, size):
            for c in range(0, size):
                identifier = str(r)+"x"+str(c)

                if square[r][c] == "_":
                    self.blanks.append(identifier)
                    domain = list(range(1, size+1))
                    self.collection[identifier]=Variable(None, domain)
                else:
                    self.collection[identifier]=Variable(square[r][c],[])

    """Make a nice mess"""
    def __str__(self):
        prstr = ""
        for item in self.collection.values():
            prstr += format(item) + "\n"

        return prstr + "\nBlanks:" + format(self.blanks)


class Problem:
    """The problem class with methods for handling the states

    Keyword Arguments:
    initial_state -- an array representing the latin square
    """
    def __init__(self, initial_square):
        self.ini_sq = initial_square

    """Return an initial state for the problem, using stored square"""
    def initial_state(self):
        return State(len(self.ini_sq), self.ini_sq)

    """Determine if the state provided is correctly solved & complete"""
    def is_goal(self, state):
        if state.blanks:
            return False

        for r in range(0, state.sz):
            column = []
            row = []
            for c in range(0, state.sz):
                identifier_row = str(r)+"x"+str(c)
                identifier_col = str(c)+"x"+str(r)
                #Check if the items in the row are unique
                row.append(state.collection[identifier_row])
                #Build a column
                column.append(state.collection[identifier_row])
            #Check that all values in the column are unique
            if len(set(column)) != len(column):
                return False
            if len(set(row)) != len(row):
                return False

        return True

    """Return possible actions for the first blank cell in the state"""
    def actions(self, state):
        a = []
        if state.blanks:
            id = state.blanks[0]
            v = state.collection[id]
            for d in v.dom:
                a.append((id, d))
        return a

    """Apply a provided action to a cell in the state

    action -- a pair of a location string and an integer from 1...N
    """
    def result(self, state, action):
        new_state = copy.deepcopy(state)
        if new_state.blanks:
            new_state.blanks.remove(action[0])
        new_state.collection[action[0]].assign(action[1])
        return new_state



num = int(input())
for i in range(0, num):
    square = []
    size = int(input())
    for j in range(0, size):
        line = input().split()
        square.append(line)
    problem = Problem(square)
    search = Search(problem)
    #Create search call here
    result = search.DepthFirstSearch(problem.initial_state())
    print(result)

    try:
        input()
    except EOFError:
        pass
