#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 3 Question 1

from A1Search import Search, SearchResult
import copy

class State:
    """Represents a state with an array of numbers

    Keyword Arguments:
    size -- the length/width of the square
    square -- the square itself, as an array of arrays or 2d array
    """
    def __init__(self, size, square):
        self.sq = square
        self.blanks = []
        self.sz = size
        for r in range(0, size):
            for c in range(0, size):
                if self.sq[r][c] == "_":
                    self.blanks.append((r,c))


    def __str__(self):
        return format(self.sq) + "\n" + format(self.blanks)

"""The problem class with methods for handling the states"""
class Problem:
    """Determine if the state provided is correctly solved & complete"""
    def is_goal(self, state):
        if state.blanks:
            return False
        else:
            for r in range(0, state.sz):
                column = []
                #Check if length or unique items is same as row length
                if len(set(state.sq[r])) != len(state.sq[r]):
                    return False
                for c in range(0, state.sz):
                    #Build a column
                    column.append(state.sq[c][r])
                #Check that all values in the column are unique
                if len(set(column)) != len(column):\
                    return False
        return True

    """Return possible actions for each blank cell in the state"""
    def actions(self, state):
        a = []
        for b in state.blanks:
            x, y = b
            acts = list(set(map(str, range(1, state.sz+1))) - set(state.sq[x]))
            for act in acts:
                a.append((b, act))
        return a

    """Apply a provided action to a cell in the state

    action -- a pair consisting of coordinates and a value
    """
    def result(self, state, action):
        new_state = copy.deepcopy(state)
        x, y = action[0]
        new_state.sq[x][y] = action[1]
        return State(new_state.sz, new_state.sq)

num = int(input())
problem = Problem()
search = Search(problem)
for i in range(0, num):
    square = []
    size = int(input())
    for j in range(0, size):
        line = input().split()
        square.append(line)
    #Create search call here
    result = search.DepthFirstSearch(State(size, square))
    print(result)


    try:
        input()
    except EOFError:
        pass
