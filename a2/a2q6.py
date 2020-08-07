#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 2 Question 6

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


def random_guessing(problem):
    """A solution finding function that guesses random states
    and stores the best one"""
    best_guess = problem.create_random_state()
    for i in range(0,1000):
        guess = problem.create_random_state()
        if problem.dift_from_T(guess) < problem.dift_from_T(best_guess):
            best_guess = guess
    return MachineProblemResult(best_guess,
                problem.machine_exec(best_guess.seq), problem.T )

def random_search(problem):
    """A solution finding function that creates a random successor state
    and moves to the new state if it is better than the current state"""
    best_guess = problem.create_random_state()
    for i in range(0,1000):  #Range used in place of a timer
        guess = problem.create_random_neighbour_state(best_guess)
        if problem.dift_from_T(guess) < problem.dift_from_T(best_guess):
            best_guess = guess
    return MachineProblemResult(best_guess,
                problem.machine_exec(best_guess.seq), problem.T )

def hill_climbing_search(problem, iterations=1000, max_si_stps=30):
    """A solution finding method which finds the best neighbour of a random
    state and progresses to that state if it is better than the current states
    If no state is better, it returns the current state.
    """
    best_guess = problem.create_random_state()
    side_steps = 0
    for i in range(0,iterations):  #Range used in place of a timer
        guess = problem.create_best_neighbour_state(best_guess)
        if problem.dift_from_T(guess) < problem.dift_from_T(best_guess):
            #neighbour is better than current best_guess
            best_guess = guess
            side_steps = 0
        elif problem.dift_from_T(guess) == problem.dift_from_T(best_guess):
            if side_steps < max_si_stps:
                #allow a small amount of plateau movement
                best_guess = guess
                side_steps += 1
            else:
                return MachineProblemResult(best_guess,
                            problem.machine_exec(best_guess.seq), problem.T )
    return MachineProblemResult(best_guess,
                problem.machine_exec(best_guess.seq), problem.T )

def random_restart_hill_climbing_search(problem, restarts=10, iterations=100):
    """A possible solution finding method uses the hill climbing search
    method, restarting a number of times and returning the best result.
    """
    result = hill_climbing_search(problem)
    for climb in range(0, restarts):
        new_result = hill_climbing_search(problem, iterations)
        if problem.dift_from_T(result.st) > problem.dift_from_T(new_result.st):
            result = new_result
    return result

def stochastic_hill_climbing_search(problem, iterations=1000, max_si_stps=30):
    """A solution finding method which finds a better neighbour of a random
    initial state and progresses to that state if it is better than the current
    states. If no state is better, it returns the current state.
    """
    best_guess = problem.create_random_state()

    for i in range(0,iterations):  #Range used in place of a timer
        guess = problem.create_improved_neighbour_state(best_guess)
        side_steps = 0
        if problem.dift_from_T(guess) < problem.dift_from_T(best_guess):
            #neighbour is better than current best_guess
            best_guess = guess
            side_steps = 0
        elif problem.dift_from_T(guess) == problem.dift_from_T(best_guess):
            if side_steps < max_si_stps:
                #allow a small amount of plateau movement
                best_guess = guess
                side_steps += 1
            else:
                return MachineProblemResult(best_guess,
                            problem.machine_exec(best_guess.seq), problem.T )
    return MachineProblemResult(best_guess,
                problem.machine_exec(best_guess.seq), problem.T )

def calc_error(problem, state):
    return (problem.dift_from_T(state)/problem.T)

def root_mean_square_error(error_vals):
    count = 0
    sum = 0
    for err in error_vals:
        count +=1
        sum += (err * err)
    return math.sqrt(sum/count)

import fileinput
rand_guess_results = []
rand_search_results = []
hill_climbing_results = []
stochastic_hc_results = []
restart_hc_results_50_by_20 = []
restart_hc_results_10_by_100 = []
rg_time = 0
rs_time = 0
hc_time = 0
shc_time = 0
rhc50by20_time = 0
rhc10by100_time = 0

count = 0
for line in fileinput.input():
    count += 1
    nums=line.split()
    print(count)
    problem = MachineProblemClass( nums[1:], nums[0])

    start = time.time()
    result = random_guessing(problem)
    rand_guess_results.append(calc_error(problem, result.st))
    end = time.time()
    rg_time += (end - start)

    start = time.time()
    result = random_search(problem)
    rand_search_results.append(calc_error(problem, result.st))
    end = time.time()
    rs_time += (end - start)

    start = time.time()
    result = hill_climbing_search(problem)
    hill_climbing_results.append(calc_error(problem, result.st))
    end = time.time()
    hc_time += (end - start)

    start = time.time()
    result = stochastic_hill_climbing_search(problem)
    stochastic_hc_results.append(calc_error(problem, result.st))
    end = time.time()
    shc_time += (end - start)

    start = time.time()
    result = random_restart_hill_climbing_search(problem, 50, 20)
    restart_hc_results_50_by_20.append(calc_error(problem, result.st))
    end = time.time()
    rhc50by20_time += (end - start)

    start = time.time()
    result = random_restart_hill_climbing_search(problem, 10, 100)
    restart_hc_results_10_by_100.append(calc_error(problem, result.st))
    end = time.time()
    rhc10by100_time += (end - start)

print("Random Guess:" + str(root_mean_square_error(rand_guess_results))+"\t"+str(rg_time/count))

print("Random Search:" + str(root_mean_square_error(rand_search_results))+"\t"+str(rs_time/count))

print("Hill Climbing:" + str(root_mean_square_error(hill_climbing_results)) + "\t"+ str(rs_time/count))

print("Stochastic Hill-climbing:" + str(root_mean_square_error(stochastic_hc_results)) + "\t"+ str(rs_time/count))

print("Random-Restart Hill-climbing (50 × 20):" + str(root_mean_square_error(restart_hc_results_50_by_20)) + "\t" +  str(rs_time/count))

print("Random-Restart Hill-climbing (10 × 100):" + str(root_mean_square_error(restart_hc_results_10_by_100)) + "\t" + str(rs_time/count))
