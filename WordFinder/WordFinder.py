import numpy as np
from Graph import Handler

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

print_board(board)
# print(board[0][0], " -> ", find_neighbors(board, 0, 0))
# print(board[0][3], " -> ", find_neighbors(board, 0, 3))
# print(board[3][3], " -> ", find_neighbors(board, 3, 3))
# print(board[3][0], " -> ", find_neighbors(board, 3, 0))
# print(board[0][1], " -> ", find_neighbors(board, 0, 1))
# print(board[3][1], " -> ", find_neighbors(board, 3, 1))
# print(board[2][0], " -> ", find_neighbors(board, 2, 0))
# print(board[2][3], " -> ", find_neighbors(board, 2, 3))
# print(board[1][1], " -> ", find_neighbors(board, 1, 1))

handler = Handler()
assembled_graph = handler.build_graph(board)

for key in assembled_graph:
    print(key, assembled_graph[key])