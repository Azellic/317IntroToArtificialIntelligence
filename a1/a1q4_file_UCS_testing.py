#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 1 Question 4

import multiprocessing
import time
from a1q1 import *
from a1q2 import *
from a1q4 import *
import fileinput


def run(line):
    state = MathProblemState(0, nums[0], nums[1:])
    problem = MathProblem(state)
    search = MathProblemInformedSearch()
    print(search.UCS(problem))
    print("\n")

if __name__ == '__main__':
    for line in fileinput.input():
        nums=line.split()
        # Start bar as a process
        p = multiprocessing.Process(target=run, args=(nums,))
        p.start()

        # Wait for 10 seconds or until process finishes
        p.join(60)

        # If thread is still active
        if p.is_alive():
            print ("Timeout reached")

            # Terminate
            p.terminate()
            p.join()
