#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 3 Question 4

from A1Search import Search, SearchResult
import copy
import operator

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
    def __init__(self, coll, bl, size):
        self.collection = dict(coll)
        for key in coll.keys():
            self.collection[key] = Variable(coll[key].cur_val, list(coll[key].dom))
        self.blanks = []
        for b in bl:
            self.blanks.append((b[0],b[1]))
        self.sz = size
        self.is_consistant = True

    """Make a nice mess"""
    def __str__(self):
        prstr = ""
        for item in self.collection.values():
            prstr += format(item) + "\n"

        return prstr + "\nBlanks:" + format(self.blanks)


class Problem:
    """Represents a state with variables and blanks

    Keyword Arguments:
    size -- the length/width of the square
    square -- the square itself, as an array of arrays or 2d array
    """
    def __init__(self, initial_square):
        self.ini_sq = initial_square

    """Return an initial state for the problem, using stored square"""
    def initial_state(self):
        #Changes from a3q2 are in State __init__ function
        size = len(self.ini_sq)
        blanks = []
        collection = {}
        for c in range(0, size):
            #Determine the domain based on the column
            column_domain = list(map(str, range(1, size+1)))
            for r in range(0, size):
                if square[r][c] != "_":
                    column_domain.remove(square[r][c])

            for r in range(0, size):
                identifier = str(r)+"x"+str(c)

                if square[r][c] == "_":
                    domain = list(set(column_domain) - set(square[r]))

                    blanks.append((identifier,len(domain)))
                    collection[identifier]=Variable(None, domain)
        blanks.sort(key = operator.itemgetter(1))
        #print(blanks)
        return State(collection, blanks, size)

    """Determine if the state provided is consistent and complete"""
    def is_goal(self, state):
        if state.blanks:
            #A proper solution must be complete
            return False
        elif not state.is_consistant:
            #A proper solution must be consistent
            return False
        return True

    """Return possible actions for a blank cell in the state(if one exists)"""
    def actions(self, state):
        a = []
        if state.is_consistant:
            if state.blanks:
                id = state.blanks[0]
                v = state.collection[id[0]]
                for d in v.dom:
                    a.append((id[0], d))
        #print(state)
        #print(len(state.blanks))
        return a

    """Apply a provided action to a cell in the state

    action -- a pair of a location string and an integer from 1...N
    """
    def result(self, state, action):
        #print(action)
        #print(state.blanks)
        new_state = State(state.collection, state.blanks, size) #TODO: Change deepcopy to new implementation
        loc = action[0]
        if new_state.blanks:
            new_state.blanks.remove((loc, len(new_state.collection[loc].dom)))
            #[blank for blank in new_state.blanks if blank[0] != action[0]]
            new_state.collection[action[0]].assign(action[1])

            #Remove action from all cells in the same row/column
            r,c = action[0].split("x")
            changed = False
            #for bl in new_state.blanks:
            for index in range(1, size+1):
                row_id = str(r)+"x"+str(index)
                col_id = str(index)+"x"+str(c)

                #Edit blanks in same column/row
                for i in row_id, col_id:
                    try:
                        sz = len(new_state.collection[i].dom)
                        new_state.collection[i].dom.remove(str(action[1]))
                        new_state.blanks.remove((i, sz))
                        new_state.blanks.append((i, sz-1))
                        changed = True
                        #Check if variable's domain is now empty
                        if not new_state.collection[i].dom:
                            new_state.is_consistant = False
                            return new_state    #It's inconsistent, stop

                    except (ValueError, KeyError) as e:
                        pass
            if changed: new_state.blanks.sort(key = operator.itemgetter(1))

        return new_state

def my_copy(collection):
    return collection




num = int(input())
for i in range(0, num):
    square = []
    size = int(input())
    for j in range(0, size):
        line = input().split()
        square.append(line)
    #print(format(State(size, square)) + "\n")
    problem = Problem(square)
    search = Search(problem, 200)
    #Create search call here
    #print(problem.result(State(size, square), ("0x0",2)))
    #print("Actions: " + format(problem.actions(State(size, square))))
    result = search.DepthFirstSearch(problem.initial_state())
    print(result)

    try:
        input()
    except EOFError:
        #print("End of file reached")
        pass
