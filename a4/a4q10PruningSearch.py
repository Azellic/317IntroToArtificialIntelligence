#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 4 Search Code

import sys
import math
import time as time
from a4q10common import *

class GameSearch(object):
    """Methods for performing a Alpha-Beta pruning version of MinMax search,
    with optional cutoff
    game: the game class provided for search
    """
    def __init__(self, game, cutoff=math.inf):
        self._game = game
        self._cutoff = cutoff

    """Determines the maximum utility for a particular state, stops searching
    if values don't meet the standards of Alpha-beta pruning"""
    def Max_Value(self, state, maxs_best, mins_best, depth):
        if self._game.is_terminal(state):
            best_here = self._game.utility(state)
        elif self._game.cutoff_test(state, depth, self._cutoff):
            best_here = self._game.eval(state)
        else:
            best_here = - math.inf
            if self._cutoff > 0:           #Check we are using cutoff search
                depth = depth + 1
            for act in self._game.actions(state):
                res = self._game.result(state, act)
                val = self.Min_Value(res, maxs_best, mins_best, depth)
                if val > best_here:
                    best_here = val

                if best_here >= mins_best:
                    return best_here

                maxs_best = max(maxs_best, best_here)
        return best_here

    """Determines the minimum utility for a particular state, stops searching
    if values don't meet the standards of Alpha-beta pruning"""
    def Min_Value(self, state, maxs_best, mins_best, depth):
        if self._game.is_terminal(state):
            best_here = self._game.utility(state)
        elif self._game.cutoff_test(state, depth, self._cutoff):
            best_here = self._game.eval(state)
        else:
            best_here = math.inf
            if self._cutoff > 0:           #Check we are using cutoff search
                depth = depth + 1
            for act in self._game.actions(state):
                res = self._game.result(state, act)
                val = self.Max_Value(res, maxs_best, mins_best, depth)
                if val < best_here:
                    best_here = val

                if best_here <= maxs_best:
                    return best_here

                mins_best = min(mins_best, best_here)
        return best_here

    """Determines the best action available to player 1 at any given state,
     returns the utility and the action"""
    def Max_Decision(self, state, depth):
        maxs_best = - math.inf
        mins_best = math.inf

        best_here = - math.inf
        best_action = None

        for act in self._game.actions(state):
            res = self._game.result(state, act)
            val = self.Min_Value(res, maxs_best, mins_best, depth)

            if val > best_here:
                best_here = val
                best_action = act

            maxs_best = max(maxs_best, best_here)

        return best_here, best_action

    """Determines the best action available to player 2 at any given state,
     returns the utility and the action"""
    def Min_Decision(self, state, depth):
        maxs_best = - math.inf
        mins_best = math.inf

        best_here = math.inf
        best_action = None

        for act in self._game.actions(state):
            res = self._game.result(state, act)
            val = self.Max_Value(res, maxs_best, mins_best, depth)

            if val < best_here:
                best_here = val
                best_action = act

            mins_best = min(mins_best, best_here)

        return best_here, best_action

    """The entry point for MinMax_Search, determines which player's turn it
    is, and calls the corrent functions, returning what they return"""
    def Minimax_Value(self, state, depth=0):
        if self._game.is_maxs_turn(state):
            return self.Max_Decision(state, depth)
        else:
            return self.Min_Decision(state, depth)

    """Alpha-beta pruning MinMax search. Determines the best action and
    utility of that action, returning a MinMaxSearchResult object"""
    def MinMax_Search(self, state):
        start_time = time.time()
        val, act = self.Minimax_Value(state)
        now = time.time()
        return MinMaxSearchResult(size=self._game._sz, utility=val,
                                  start_action=act, time=now-start_time)

    """Alpha-beta pruning MinMax search with a cutoff. Cutoff is determined by
    the Game class. Determines the best action and utility of that action,
    returning a MinMaxSearchResult object"""
    def MinMax_Cutoff_Search(self, state):
        start_time = time.time()
        val, act = self.Minimax_Value(state, 1)
        now = time.time()
        return MinMaxSearchResult(size=self._game._sz, utility=val,
                                  start_action=act, time=now-start_time)
