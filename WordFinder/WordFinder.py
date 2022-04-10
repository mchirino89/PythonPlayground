import numpy as np
import time
from Graph import Handler
from BreadFirstSearch import BFS 

board = [["M", "A", "R", "T"],
         ["S", "P", "E", "F"],
         ["I", "B", "U", "M"],
         ["P", "T", "O", "R"]]

def print_board(board):
    matrix = np.array(board)
    for i in matrix:
        for j in i:
            print(j, " ", end="")
        print()
    print()

handler = Handler()
print_board(board)
# print(board[0][0], " -> ", handler.find_neighbors(board, 0, 0))
# print(board[0][3], " -> ", handler.find_neighbors(board, 0, 3))
# print(board[3][3], " -> ", handler.find_neighbors(board, 3, 3))
# print(board[3][0], " -> ", handler.find_neighbors(board, 3, 0))
# print(board[0][1], " -> ", handler.find_neighbors(board, 0, 1))
# print(board[3][1], " -> ", handler.find_neighbors(board, 3, 1))
# print(board[2][0], " -> ", handler.find_neighbors(board, 2, 0))
# print(board[2][3], " -> ", handler.find_neighbors(board, 2, 3))
# print(board[1][1], " -> ", handler.find_neighbors(board, 1, 1))

assembled_graph = handler.build_graph(board)

# for key in assembled_graph:
#     print(key, " -> ", assembled_graph[key])
# print()
bfs = BFS()
bfs.check(assembled_graph, list(assembled_graph.keys())[0])

# start_time = time.time()
# print("Is 'ma' a valid prefix? -> ",'ma' in word_repository)
# print("--- Evaluates prefix in %s seconds ---" % (time.time() - start_time))

# start_time = time.time()
# print("Give me all possible suggestions for 'the'")
# print(word_repository.autocomplete("the"))
# print("--- Produces autocomplete suggestions in %s seconds ---" % (time.time() - start_time))