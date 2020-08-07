#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 1 Question 2

from a1q1 import *
import fileinput

#This will read in lines and run each search on that line
for line in fileinput.input():
    nums=line.split()
    state = MathProblemState(0, nums[0], nums[1:])
    problem = MathProblem(state)
    search = MathSolutionTreeSearch()
    print(search.DFS(problem))
    print(search.BFS(problem))
    print(search.DLTreeSearch(problem))
    print(search.IDS(problem))
    print("\n")
