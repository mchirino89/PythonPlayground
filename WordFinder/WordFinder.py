import numpy as np
import time
from Graph import Handler
from WordEngine import WordMatcher 
from english_words import english_words_lower_alpha_set

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
start_time = time.time()
word_builder = WordMatcher()

letters = list(assembled_graph.keys())
word_candidates = set()

for letter in letters:
    words_found = word_builder.check(assembled_graph, letter)
    for word in words_found.values():
        word_candidates.add(word.lower())

# print()
valid_words = english_words_lower_alpha_set.intersection(word_candidates)
print("Total 3 letter words = {total}".format(total=len(valid_words)))
print("--- Word assembled from board took %s seconds ---" % (time.time() - start_time))

for word in valid_words:
    print(word.upper())

# start_time = time.time()
# print("Is 'ma' a valid prefix? -> ",'ma' in word_repository)
# print("--- Evaluates prefix in %s seconds ---" % (time.time() - start_time))

# start_time = time.time()
# print("Give me all possible suggestions for 'the'")
# print(word_repository.autocomplete("the"))
# print("--- Produces autocomplete suggestions in %s seconds ---" % (time.time() - start_time))