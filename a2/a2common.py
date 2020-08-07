import random
import copy
import math
import time

class MachineProblemState:
    def __init__(self, numbers, operators):
        """Represents a state in the calculation machine

        Keyword Arguments:
        numbers -- List of constant number used
        operators -- The operations associated with each number
        target -- The number the equation is trying to create

        """
        self.N = numbers
        self.OPS = operators
        self.seq = list(zip(operators, numbers))

    def __str__(self):
        """An override method for nicely printing the state. """
        return "Sequence: " + str(self.seq)


class MachineProblemClass:
    OPERATORS=["ADD", "SUB", "MUL", "DIV", "NOP"]

    def __init__(self, numbers, target):
        self.T = float(target)
        self.NUMS = numbers

    def machine_exec(self, seq):
        """Return the resulting register value after applying operations in seq.

        seq -- A list of tuples containing an operator and operand
        """
        register = 0
        for instruction in seq:
            operator = instruction [0]
            operand = float(instruction [1])
            if operator == "ADD":
                register += operand
            elif operator == "SUB":
                register -= operand
            elif operator == "MUL":
                register *= operand
            elif operator == "DIV":
                register = register / operand
            elif operator == "NOP":
                pass
            else:
                print("unknown operator", operator)
        return register

    def dift_from_T(self, state):
        """The distance from the target as determined by f(s, t)=|t − m(s)|"""
        return abs(self.T - self.machine_exec(state.seq))

    def create_random_state(self):
        """Return a new completely random state."""
        operators = []
        for num in self.NUMS:
            operators.append(random.choice(self.OPERATORS))
        return MachineProblemState(self.NUMS, operators)

    def create_random_neighbour_state(self, state):
        """Return a new random neightbour to the given state."""
        index = random.randint(0, len(self.NUMS)-1)
        new_operators = copy.deepcopy(state.OPS)
        new_operators[index] = random.choice(self.OPERATORS)
        return MachineProblemState(self.NUMS, new_operators)

    def create_best_neighbour_state(self, state):
        """Return the best neighbour of the given state."""
        return_state = state    #If no neighbour is better, return original
        for index in range(0, len(self.NUMS)):
            new_operators = copy.deepcopy(state.OPS)
            for op in self.OPERATORS:
                new_operators[index] = op
                new_state = MachineProblemState(self.NUMS, new_operators)
                if self.dift_from_T(new_state) < self.dift_from_T(return_state):
                    return_state = copy.deepcopy(new_state)
        return return_state

    def create_improved_neighbour_state(self, state):
        """Return a random better neighbour of the given state."""
        better_states=[]
        for index in range(0, len(self.NUMS)):
            new_operators = copy.deepcopy(state.OPS)
            for op in self.OPERATORS:
                new_operators[index] = op
                new_state = MachineProblemState(self.NUMS, new_operators)
                if self.dift_from_T(new_state) < self.dift_from_T(state):
                    better_states.append(copy.deepcopy(new_state))
        if better_states:
            return random.choice(better_states)
        else:
            return state

class MachineProblemResult:
    def __init__(self, state, total, target):
        self.st = state
        self.tot = total
        self.tar = target

    def __str__(self):
        prstr = "Target: " + str(self.tar)
        prstr += "\nCalculated total: " + str(self.tot)
        prstr += "\n" + format(self.st)
        return prstr
