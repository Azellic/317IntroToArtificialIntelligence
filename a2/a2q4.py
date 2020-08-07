#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 2 Question 4

from a2q6 import *
from a2q3 import hill_climbing_search

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
