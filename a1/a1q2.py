#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 1 Question 2

from a1q1 import *
import fileinput
import queue as queue
import sys

class MathSearchNode:
    def  __init__(self, depth, action, parent, step_cost, state):
        """Node in the equation generating search TreeSearch

        state -- a MathProblemState object
        depth -- the depth of this node from the root
        action -- a string representing the action that caused this state
        parent -- the node responsible for creating this Node
        step_cost -- the cost of implementing this action
        """
        self.st = state
        self.d = depth
        self.act = action
        self.p = parent
        self.pc = step_cost

    def __str__(self):
        """Override print method for this class """
        prstr = ""
        prstr +="Depth: " + str(self.d) + "\tPath Cost: " + str(self.pc)
        prstr += "\nAction: " + self.act
        prstr += "\nState:\n"+format(self.st)

        return prstr

class MathSearchResult:
    def __init__(self, success, depth, state, cutoff=False):
        """Contains the results of a search.
        success -- True if solution found, false otherwise
        depth -- the distance from intial node to success node
        state -- the state at which success was met
        """
        self.st = state
        self.suc = success
        self.d = depth
        self.cut = cutoff

    def __str__(self):
        """Override print method to interpret class in printable format """
        if self.suc:
            prstr = "Solution found at depth " + str(self.d) + "\nState:\n"
        elif self.cut:
            prstr ="Limit reached before solution was found\n"
        else:
            prstr = "Failed to find a solution.\n"
        prstr += format(self.st)
        return prstr



class MathSolutionTreeSearch:
    def __init__(self):
        """Creates a Search class with an associated frontier """
        self.frontier = None

    def InitializeFrontier(self, problem):
        """ Initialize the Frontier with the problem provided

        problem -- A MathProblem class instance
        """
        for act in problem.actions(problem.init_state):
            rslt_st = problem.result(problem.init_state, act)
            self.frontier.put_nowait(MathSearchNode(1, act, None, 0, rslt_st))

    def IncreaseFrontier(self, problem, cur_node):
        """ Increase the Frontier with possible actions for cur_node

        problem -- A MathProblem class instance
        cur_node -- The node being expanded
        """
        for act in problem.actions(cur_node.st):
            child_state = problem.result(cur_node.st, act)
            child_node = MathSearchNode(cur_node.d+1, act, cur_node,
                                        cur_node.pc+1, child_state)
            self.frontier.put_nowait(child_node)

    def TreeSearch(self, problem):
        """Searches and expands a frontier to attempt to solve the problem
        Returns:
        A MathSearchResult object with True if solution found, false otherwise
        """
        #Check if init state is goal, because it *could* be
        if problem.is_goal(problem.init_state):
            return MathSearchResult(True, 0, problem.init_state)

        self.InitializeFrontier(problem)

        #Try everything in the frontier, in order decided by frontier type
        while not self.frontier.empty():
            cur_node = self.frontier.get_nowait()
            if problem.is_goal(cur_node.st):
                return MathSearchResult(True, cur_node.d, cur_node.st)
            else:
                self.IncreaseFrontier(problem, cur_node)
        return MathSearchResult(False, 0, problem.init_state)

    def BFS(self, problem):
        """Initiates a breadth first search of a problem class"""
        self.frontier = queue.Queue()
        return self.TreeSearch(problem)

    def DFS(self, problem):
        """Initiates a depth first search of a problem class"""
        self.frontier = queue.LifoQueue()
        return self.TreeSearch(problem)

    def DLTreeSearch(self, problem, limit):
        """Initiates a depth first search of a problem class with limited depth

        limit -- the maximum depth the search will descend to
        """
        #Check if init state is goal, because it *could* be
        if problem.is_goal(problem.init_state):
            return MathSearchResult(True, 0, problem.init_state)

        #Initialize the frontier
        self.frontier = queue.LifoQueue()
        self.InitializeFrontier(problem)

        #Try everything in the frontier, in order decided by frontier type
        cutoff = False
        while not self.frontier.empty():
            cur_node = self.frontier.get_nowait()
            if problem.is_goal(cur_node.st):
                return MathSearchResult(True, cur_node.d, cur_node.st)
            else:
                if cur_node.d < limit:
                    self.IncreaseFrontier(problem, cur_node)
                else:
                    cutoff = True
        return MathSearchResult(False, 0, problem.init_state, cutoff)

    def IDS(self, problem):
        """Initiates a depth first search with increasing depth of a problem"""
        self.frontier = queue.LifoQueue()

        limit = 0
        while True:
            result = self.DLTreeSearch(problem, limit)
            if result.suc:
                return result
            #If not success and cutoff not reached
            if not result.suc and not result.cut:
                 return result
            limit +=1
