#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 4 Search Code

import sys
import math
import time as time
from a4q10common import *

class GameSearch(object):
    """Methods for performing a basic MinMax search, with optional cutoff
    game: the game class provided for search
    """
    def __init__(self, game, cutoff=math.inf):
        self._game = game
        self._cutoff = cutoff

    """Player 1's turn, determines best value for all possible actions, and
    therfor the utility of this particular non-root node. If cutoff reached,
    returns an estimated utility

    Variables:
    state: the state of the gameboard
    depth: Depth of search from initial action
    """
    def Max_Value(self, state, depth):
        if self._game.is_terminal(state):
            best = self._game.utility(state)
        elif self._game.cutoff_test(state, depth, self._cutoff):
            best = self._game.eval(state)
        else:
            best = - math.inf
            depth = depth + 1
            for act in self._game.actions(state):
                val = self.Min_Value(self._game.result(state, act), depth)
                if val > best:
                    best = val
        return best

    """Player 2's turn, determines best value for all possible actions, and
    therfor the utility of this particular non-root node. If cutoff reached,
    returns an estimated utility

    Variables:
    state: the state of the gameboard
    depth: Depth of search from initial action
    """
    def Min_Value(self, state, depth):
        if self._game.is_terminal(state):
            best = self._game.utility(state)
        elif self._game.cutoff_test(state, depth, self._cutoff):
            best = self._game.eval(state)
        else:
            best = math.inf
            depth = depth + 1
            for act in self._game.actions(state):
                val = self.Max_Value(self._game.result(state, act), depth)
                if val < best:
                    best = val
        return best

    """Determine's the best move for a player on their turn based on the utility
    of an action."""
    def minimax_decision(self, state, depth=0):
        best_action = None
        if self._game.is_maxs_turn(state):
            best = - math.inf
            for act in self._game.actions(state):
                val = self.Min_Value(self._game.result(state, act), depth)
                if val > best:
                    best = val
                    best_action = act
        else:
            best = math.inf
            for act in self._game.actions(state):
                val = self.Max_Value(self._game.result(state, act), depth)
                if val < best:
                    best = val
                    best_action = act
        return best, best_action

    """The basic MinMax search. Determines the best action and utility of that
    action, returning a MinMaxSearchResult object"""
    def MinMax_Search(self, state):
        start_time = time.time()
        val, act = self.minimax_decision(state)
        now = time.time()
        return MinMaxSearchResult(size=self._game._sz, utility=val,
                                  start_action=act, time=now-start_time)

    """The basic MinMax search with a cutoff. Cutoff is determined by the Game
    class. Determines the best action and utility of that action, returning a
    MinMaxSearchResult object

    *A note, I restructured some stuff later on and this is basically the
    same as non-cutoff except the depth is passed from here. Cutoff set in init"""
    def MinMax_Cutoff_Search(self, state):
        start_time = time.time()
        val, act = self.minimax_decision(state, 1)
        now = time.time()
        return MinMaxSearchResult(size=self._game._sz, utility=val,
                                  start_action=act, time=now-start_time)
