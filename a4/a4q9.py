#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 4 Question 9

import a4q10game1a as a4game1a
import a4q10game1b as a4game1b
import a4q10search as a4search
import a4q10PruningSearch as a4PruningSearch

data = [["N", "Cut-off P1", "Cut-off P2", "Win/Loss P1"]]
col_width = max(len(word) for row in data for word in row)+2  # padding

for max in [10, 20]:
    #This is cutoff 4, 4 and basic cutoff search for both
    wins=[0,0]
    for size in range(1, max+1):
        game = a4game1a.Game(size)
        p1search = a4search.GameSearch(game, 4)
        p2search = a4search.GameSearch(game, 4)
        cur_state = game.start_state
        while not game.is_terminal(cur_state):
            if game.is_maxs_turn(cur_state):
                #print(len(cur_state.Q))
                result = p1search.MinMax_Cutoff_Search(cur_state)
                #print(result.st_act)
            else:
                #print(len(cur_state.Q))
                result = p2search.MinMax_Cutoff_Search(cur_state)
                #print(result.st_act)
            cur_state = game.result(cur_state, result.st_act)
        #print(str(result.val))
        #print(str(cur_state.Q) + "\n")
        if result.val > 0:
            wins[0] = wins[0] + 1
        else:
            wins[1] = wins[1] + 1
    data.append([str(max), "4", "4", str(wins)])




    wins=[0,0]
    for size in range(1, max+1):
        game = a4game1a.Game(size)
        p1search = a4search.GameSearch(game, 5)
        p2search = a4search.GameSearch(game, 5)
        cur_state = game.start_state
        while not game.is_terminal(cur_state):
            if game.is_maxs_turn(cur_state):
                result = p1search.MinMax_Cutoff_Search(cur_state)
            else:
                result = p2search.MinMax_Cutoff_Search(cur_state)
            cur_state = game.result(cur_state, result.st_act)
        if result.val > 0:
            wins[0] = wins[0] + 1
        else:
            wins[1] = wins[1] + 1
    data.append([str(max), "5", "5", str(wins)])




    wins=[0,0]
    for size in range(1, max+1):
        game = a4game1a.Game(size)
        p1search = a4search.GameSearch(game, 5)
        p2search = a4search.GameSearch(game, 3)
        cur_state = game.start_state
        while not game.is_terminal(cur_state):
            if game.is_maxs_turn(cur_state):
                #print(len(cur_state.Q))
                result = p1search.MinMax_Cutoff_Search(cur_state)
                #print(result.st_act)
            else:
                #print(len(cur_state.Q))
                result = p2search.MinMax_Cutoff_Search(cur_state)
                #print(result.st_act)
            cur_state = game.result(cur_state, result.st_act)
        #print(str(result.val))
        #print(str(cur_state.Q) + "\n")
        if result.val > 0:
            wins[0] = wins[0] + 1
        else:
            wins[1] = wins[1] + 1
    data.append([str(max), "5", "3", str(wins)])




    wins=[0,0]
    for size in range(1, max+1):
        game = a4game1a.Game(size)
        p1search = a4search.GameSearch(game, 3)
        p2search = a4search.GameSearch(game, 5)
        cur_state = game.start_state
        while not game.is_terminal(cur_state):
            if game.is_maxs_turn(cur_state):
                #print(len(cur_state.Q))
                result = p1search.MinMax_Cutoff_Search(cur_state)
                #print(result.st_act)
            else:
                #print(len(cur_state.Q))
                result = p2search.MinMax_Cutoff_Search(cur_state)
                #print(result.st_act)
            cur_state = game.result(cur_state, result.st_act)
        #print(str(result.val))
        #print(str(cur_state.Q) + "\n")
        if result.val > 0:
            wins[0] = wins[0] + 1
        else:
            wins[1] = wins[1] + 1
    data.append([str(max), "5", "3", str(wins)])


for row in data:
    print("".join(word.ljust(col_width) for word in row))
