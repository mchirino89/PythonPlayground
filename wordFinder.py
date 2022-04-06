import numpy as np

board = [["M", "A", "R", "T"],
         ["S", "P", "E", "F"],
         ["I", "B", "U", "M"],
         ["P", "T", "O", "R"]]

def print_board(board):
    grap = {}
    matrix = np.array(board)
    for i in matrix:
        for j in i:
            print(j, " ", end="")
        print()
    print()

def find_neighbors(board, i, j):
    neighbors = []
    if i == 0 and j == 0: # top left corner
        neighbors.append(board[i][j + 1])
        neighbors.append(board[i + 1][j + 1])
        neighbors.append(board[i + 1][j])
    if i == len(board) - 1 and j == 0: # bottom left corner
        neighbors.append(board[i - 1][j])
        neighbors.append(board[i - 1][j + 1])
        neighbors.append(board[i][j + 1])
    if i == 0 and j == len(board) - 1: # top right corner
        neighbors.append(board[i + 1][j])
        neighbors.append(board[i + 1][j - 1])
        neighbors.append(board[i][j - 1])
    if i == len(board) - 1 and j == len(board) - 1: # bottom right corner
        neighbors.append(board[i][j - 1])
        neighbors.append(board[i - 1][j - 1])
        neighbors.append(board[i - 1][j])

    return neighbors

print_board(board)
print(board[0][0], " -> ", find_neighbors(board, 0, 0))
print(board[0][3], " -> ", find_neighbors(board, 0, 3))
print(board[3][3], " -> ", find_neighbors(board, 3, 3))
print(board[3][0], " -> ", find_neighbors(board, 3, 0))