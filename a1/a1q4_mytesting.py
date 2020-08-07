#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 1 Question 2

from a1q2 import *
from a1q4 import *


test_state = MathProblemState("0", "4", ["10", "7", "5", "8", "2"])
test_problem = MathProblem(test_state)
search = MathProblemInformedSearch()
print(search.UCS(test_problem))
print(search.GBFS(test_problem))
print(search.AStarSearch(test_problem))
test_state2 = MathProblemState("0", "852", ["372", "31", "71", "2"])
test_problem = MathProblem(test_state2)
print(search.UCS(test_problem))
print(search.GBFS(test_problem))
print(search.AStarSearch(test_problem))
