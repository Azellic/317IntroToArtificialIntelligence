#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 2 Bonus 1

from a2common import *
import copy
import random
import time
import math


def SimAnneal(problem , schedule, t=1000):
    current = problem.create_random_state()
    start = time.time()
    while t > 0:
        next = problem.create_random_state()
        deltaE = problem.dift_from_T(next) - problem.dift_from_T(current)
        if deltaE > 0:
            current = copy.deepcopy(next)
        else:
            r = math.exp(deltaE/t)
            p = random.uniform(0,1)
            if r < p:
                current = copy.deepcopy(next)
        t = t - schedule #t - (time.time() - start)
    return MachineProblemResult(current,
                problem.machine_exec(current.seq), problem.T )

import fileinput
for line in fileinput.input():
    nums=line.split()
    print(SimAnneal(MachineProblemClass(nums[1:], nums[0]), 70) )
