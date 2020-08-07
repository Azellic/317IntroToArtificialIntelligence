#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 2 Question 2

from a2q6 import *

def random_search(problem):
    """A solution finding function that creates a random successor state
    and moves to the new state if it is better than the current state"""
    best_guess = problem.create_random_state()
    for i in range(0,300):  #Range used in place of a timer
        guess = problem.create_random_neighbour_state(best_guess)
        if problem.dift_from_T(guess) < problem.dift_from_T(best_guess):
            best_guess = guess
    return MachineProblemResult(best_guess,
                problem.machine_exec(best_guess.seq), problem.T )
