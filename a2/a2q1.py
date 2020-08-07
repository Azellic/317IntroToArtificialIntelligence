#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 2 Question 1

from a2q6 import *

def random_guessing(problem):
    """A solution finding function that guesses random states
    and stores the best one"""
    best_guess = problem.create_random_state()
    for i in range(0,300):
        guess = problem.create_random_state()
        if problem.dift_from_T(guess) < problem.dift_from_T(best_guess):
            best_guess = guess
    return MachineProblemResult(best_guess,
                problem.machine_exec(best_guess.seq), problem.T )
