#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 4 Question 7

import a4q10game1a as a4game1a
import a4q10game1b as a4game1b
import a4q10PruningSearch as a4PruningSearch

print("Variation 1a")
data=[["Size", "Minimax Value", "Best Opening Move", "Time in Seconds"]]
col_width = max(len(word) for row in data for word in row)+2  # padding
for size in range(1, 21):
    game = a4game1a.Game(size)
    search = a4PruningSearch.GameSearch(game, 4)
    result = search.MinMax_Cutoff_Search(game.start_state)
    data.append([str(result.sz), str(result.val), str(result.st_act), str(result.t)])

for row in data:
    print("".join(word.ljust(col_width) for word in row))
print("Variation 1b")
data=[["Size", "Minimax Value", "Best Opening Move", "Time in Seconds"]]
for size in range(1, 21):
    game = a4game1b.Game(size)
    search = a4PruningSearch.GameSearch(game, 4)
    result = search.MinMax_Cutoff_Search(game.start_state)
    data.append([str(result.sz), str(result.val), str(result.st_act), str(result.t)])

for row in data:
    print("".join(word.ljust(col_width) for word in row))
print("\n")
