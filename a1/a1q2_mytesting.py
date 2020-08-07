#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 1 Question 2

from a1q2 import *

def basic_testing():
    """Initial testing for a1q2 non search classes """
    test_state = MathProblemState("0", "5", ["2","3",])
    test_problem = MathProblem(test_state)
    search_node = MathSearchNode(0, "+ 1", None, 0, test_state)
    print(search_node)
    goal_state = MathProblemState("5", "5", ["0"])
    result = MathSearchResult(True, 3, goal_state)
    print(result)

def BFS_and_DFS_testing():
    """A few test examples for BreadthFS and DepthFS """
    #Should be a success
    test_state = MathProblemState("0", "5", ["1", "7", "3", "8", "2"])
    test_problem = MathProblem(test_state)
    search = MathSolutionTreeSearch()
    print(search.BFS(test_problem))
    print ("\n")
    print(search.DFS(test_problem))
    print ("\n")
    #should fail
    test_state = MathProblemState("0", "10", ["99", "7", "2"])
    test_problem = MathProblem(test_state)
    print(search.BFS(test_problem))
    print ("\n")
    print(search.DFS(test_problem))
    print ("\n")
    test_state = MathProblemState("0", "7", ["3", "-4", "2"])
    test_problem = MathProblem(test_state)
    print(search.BFS(test_problem))
    print ("\n")
    print(search.DFS(test_problem))
    print ("\n")
    test_state = MathProblemState("0", "-7", ["3", "-4", "2"])
    test_problem = MathProblem(test_state)
    print(search.BFS(test_problem))
    print ("\n")
    print(search.DFS(test_problem))
    print ("\n")

def DLS_testing():
    """Some simple testing for Depth Limited Search """
    test_state = MathProblemState("0", "5", ["1", "7", "3", "8", "2"])
    test_problem = MathProblem(test_state)
    search = MathSolutionTreeSearch()
    print(search.DLTreeSearch(test_problem, 10))
    print ("\n")
    test_state = MathProblemState("0", "5", ["100", "700", "300", "400", "550"])
    test_problem = MathProblem(test_state)
    print(search.DLTreeSearch(test_problem, 3))
    print ("\n")

def IDS_testing():
    """Some simple testing for Iterative Depth Limited Search """
    test_state = MathProblemState("0", "5", ["1", "7", "3", "8", "2"])
    test_problem = MathProblem(test_state)
    search = MathSolutionTreeSearch()
    print(search.IDS(test_problem))
    print ("\n")
    test_state = MathProblemState("0", "5", ["100", "700", "300", "400", "550"])
    test_problem = MathProblem(test_state)
    print(search.IDS(test_problem))
    print ("\n")


basic_testing()
BFS_and_DFS_testing()
DLS_testing()
IDS_testing()
