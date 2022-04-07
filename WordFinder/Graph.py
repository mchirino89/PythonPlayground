class Handler:
    def build_graph(self, board):
        grap = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                key = self.format_key(board[i][j], i, j)
                grap[key] = self.find_neighbors(board, i, j)

        return grap

    def format_key(self, key, i, j):
        return "{key}_({i},{j})".format(key=key, i=i, j=j) 
    
    def find_neighbors(self, board, i, j):
        neighbors = []
        # corners
        if i == 0 and j == 0: # top left corner
            neighbors.append(self.format_key(board[i][j + 1], i, j + 1))
            neighbors.append(self.format_key(board[i + 1][j + 1], i + 1, j + 1))
            neighbors.append(self.format_key(board[i + 1][j], i + 1, j))
        elif i == len(board) - 1 and j == 0: # bottom left corner
            neighbors.append(self.format_key(board[i - 1][j], i - 1, j))
            neighbors.append(self.format_key(board[i - 1][j + 1], i - 1, j + 1))
            neighbors.append(self.format_key(board[i][j + 1], i, j + 1))
        elif i == 0 and j == len(board) - 1: # top right corner
            neighbors.append(self.format_key(board[i + 1][j], i + 1, j))
            neighbors.append(self.format_key(board[i + 1][j - 1], i + 1, j - 1))
            neighbors.append(self.format_key(board[i][j - 1], i, j - 1))
        elif i == len(board) - 1 and j == len(board) - 1: # bottom right corner
            neighbors.append(self.format_key(board[i][j - 1], i, j - 1))
            neighbors.append(self.format_key(board[i - 1][j - 1], i - 1, j - 1))
            neighbors.append(self.format_key(board[i - 1][j], i - 1, j))

        # rows
        elif j > 0 and j < len(board) - 1 and i == 0: # top row
            neighbors.append(self.format_key(board[i][j + 1], i, j + 1))
            neighbors.append(self.format_key(board[i + 1][j + 1], i + 1, j + 1))
            neighbors.append(self.format_key(board[i + 1][j], i + 1, j))
            neighbors.append(self.format_key(board[i + 1][j - 1], i + 1, j - 1))
            neighbors.append(self.format_key(board[i][j - 1], i, j - 1))
        elif j > 0 and j < len(board) - 1 and i == len(board) - 1: # bottom row
            neighbors.append(self.format_key(board[i][j - 1], i, j - 1))
            neighbors.append(self.format_key(board[i - 1][j - 1], i - 1, j - 1))
            neighbors.append(self.format_key(board[i - 1][j], i - 1, j))
            neighbors.append(self.format_key(board[i - 1][j + 1], i - 1, j + 1))
            neighbors.append(self.format_key(board[i][j + 1], i, j + 1))

        # columns
        elif i > 0 and i < len(board) - 1 and j == 0: # left column
            neighbors.append(self.format_key(board[i - 1][j], i - 1, j))
            neighbors.append(self.format_key(board[i - 1][j + 1], i - 1, j + 1))
            neighbors.append(self.format_key(board[i][j + 1], i, j + 1))
            neighbors.append(self.format_key(board[i + 1][j + 1], i + 1, j + 1))
            neighbors.append(self.format_key(board[i + 1][j], i + 1, j))
        elif i > 0 and i < len(board) - 1 and j == len(board) - 1: # right column
            neighbors.append(self.format_key(board[i + 1][j], i + 1, j))
            neighbors.append(self.format_key(board[i + 1][j - 1], i + 1, j - 1))
            neighbors.append(self.format_key(board[i][j - 1], i, j - 1))
            neighbors.append(self.format_key(board[i - 1][j - 1], i - 1, j - 1))
            neighbors.append(self.format_key(board[i - 1][j], i - 1, j))

        # middle tiles
        else:
            neighbors.append(self.format_key(board[i - 1][j], i - 1, j))
            neighbors.append(self.format_key(board[i - 1][j + 1], i - 1, j + 1))
            neighbors.append(self.format_key(board[i][j + 1], i, j + 1))
            neighbors.append(self.format_key(board[i + 1][j + 1], i + 1, j + 1))
            neighbors.append(self.format_key(board[i + 1][j], i + 1, j))
            neighbors.append(self.format_key(board[i + 1][j - 1], i + 1, j - 1))
            neighbors.append(self.format_key(board[i][j - 1], i, j - 1))
            neighbors.append(self.format_key(board[i - 1][j - 1], i - 1, j - 1))

        print(neighbors)
        return neighbors
