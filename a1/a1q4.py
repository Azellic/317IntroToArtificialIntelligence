#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 1 Question 4

from a1q2 import *
from heapq import heapify, heappush, heappop


class ComparableMathSearchNode(MathSearchNode):
    """Identical to MathSearchNode, but with implemented comparison methods
    """
    def __init__(self, depth, action, parent, step_cost, state):
        MathSearchNode.__init__(self, depth, action, parent, step_cost, state)

    def __cmp__(self, other):
        return cmp(self.pc, other.pc)

    def __lt__(self, other):
        return self.pc < other.pc

    def __eq__(self, other):
        return eval(self.st.eqn) == eval(other.st.eqn)


class MathProblemInformedSearch:
    def __init__(self):
        """Creates an Informed Search class with an associated frontier """
        self.frontier = None
        self.explored = None

    def UCS(self, problem):
        """Uses a priority queue to expand the search frontier looking for a
        solution. Next node to be expanded decided by lowest path cost.
        """
        first_node = ComparableMathSearchNode(0,"", None, 0, problem.init_state)
        self.frontier = []
        heappush(self.frontier, first_node)
        self.explored = []
        while self.frontier:
            node = heappop(self.frontier)
            if problem.is_goal(node.st):
                return MathSearchResult(True, node.d, node.st)
            self.explored.append(node)
            for act in problem.actions(node.st):
                child_state = problem.result(node.st, act)
                child_node = ComparableMathSearchNode(node.d + 1, act, node,
                                            node.pc + child_state.pc,
                                            child_state)
                if not child_node in self.frontier and not child_node in self.explored:
                    heappush(self.frontier, child_node)
                elif child_node in self.frontier:
                    index = self.frontier.index(child_node)
                    if child_node < self.frontier[index]:
                        self.frontier[index] = child_node

        return MathSearchResult(False, 0, problem.init_state)

    def DetermineHeuristicPathCost(self, state, act, depth):
        """Heuristic Method for determining the heuristic path cost of expanding a node.
        """
        opt_dict = {"+":"-", "-":"+", "//":"*", "*":"//"}
        operator, num = act.split()
        val = eval(state.eqn)
        if val == 0:    #To prevent division by 0
            val = 1
        if val == state.g:
            return 0

        if state.g > val:
            heuristic = abs(eval(str(state.g)+ str(operator) + str(val)))
        else:
            heuristic = abs(eval(str(val)+ opt_dict.get(operator) + str(state.g)))

        if heuristic == 0:          #this would only happen from //
            heuristic = 1

        return heuristic * depth

    def GBFS(self, problem):
        """Uses a priority queue to expand the search frontier looking for a
        solution. Next node to be expanded decided by heuristic algorithm.
        """
        first_node = ComparableMathSearchNode(0,"", None, 0, problem.init_state)
        self.frontier = []
        heappush(self.frontier, first_node)
        self.explored = []
        while self.frontier:
            node = heappop(self.frontier)
            if problem.is_goal(node.st):
                return MathSearchResult(True, node.d, node.st)
            self.explored.append(node)
            for act in problem.actions(node.st):
                child_state = problem.result(node.st, act)
                pc = self.DetermineHeuristicPathCost(child_state, act, node.d+1)
                child_node = ComparableMathSearchNode(node.d + 1, act, node,
                                    pc, child_state)
                if not child_node in self.frontier and not child_node in self.explored:
                    heappush(self.frontier, child_node)
                elif child_node in self.frontier:
                    index = self.frontier.index(child_node)
                    if child_node < self.frontier[index]:
                        self.frontier[index] = child_node
        return MathSearchResult(False, 0, problem.init_state)

    def AStarSearch(self, problem):
        """Uses a priority queue to expand the search frontier looking for a
        solution. Next node to be expanded decided by value ofheuristic
        the algorithm + the lowest path cost.
        """
        first_node = ComparableMathSearchNode(0,"", None, 0, problem.init_state)
        self.frontier = []
        heappush(self.frontier, first_node)
        self.explored = []
        while self.frontier:
            node = heappop(self.frontier)
            if problem.is_goal(node.st):
                return MathSearchResult(True, node.d, node.st)
            self.explored.append(node)
            for act in problem.actions(node.st):
                child_state = problem.result(node.st, act)
                pc = node.pc + child_state.pc + self.DetermineHeuristicPathCost(child_state, act, node.d+1)
                child_node = ComparableMathSearchNode(node.d + 1, act, node,
                                            node.pc + child_state.pc,
                                            child_state)
                if not child_node in self.frontier and not child_node in self.explored:
                    heappush(self.frontier, child_node)
                elif child_node in self.frontier:
                    index = self.frontier.index(child_node)
                    if child_node < self.frontier[index]:
                        self.frontier[index] = child_node

        return MathSearchResult(False, 0, problem.init_state)
