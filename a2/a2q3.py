#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 2 Question 3

from a2q6 import *


def hill_climbing_search(problem, iterations=200, max_side_steps=30):
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
            if side_steps < max_side_steps:
                #allow a small amount of plateau movement
                best_guess = guess
                side_steps += 1
            else:
                return MachineProblemResult(best_guess,
                            problem.machine_exec(best_guess.seq), problem.T )
    return MachineProblemResult(best_guess,
                problem.machine_exec(best_guess.seq), problem.T )
