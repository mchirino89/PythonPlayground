import numpy as np
import time
from Graph import Handler
from BreadFirstSearch import BFS 
from english_words import english_words_lower_alpha_set
from TernaryTree import Trie

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

start_time = time.time()
assembled_graph = handler.build_graph(board)
print("--- Build graph -> %s seconds ---" % (time.time() - start_time))

for key in assembled_graph:
    print(key, " -> ", assembled_graph[key])

# bfs = BFS()
# bfs.check(assembled_graph,"M")

dictionary = {}
start_time = time.time()
for word in english_words_lower_alpha_set:
    if len(word) > 2 and len(word) < 9:
        dictionary[word] = 1

words = list(dictionary.keys())
words.sort()
print("--- Feed dictiory %s seconds ---" % (time.time() - start_time))
start_time = time.time()
word_repository = Trie('')

for word in words:
    word_repository.append(word)
    # print(word)

print("--- Build autocomplete repo %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print('ma'.upper() in word_repository)
print("--- Evaluate prefix %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(word_repository.autocomplete("the"))
print("THE" in word_repository)
print("--- Evaluate prefix %s seconds ---" % (time.time() - start_time))