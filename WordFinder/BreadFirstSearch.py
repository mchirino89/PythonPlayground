class BFS:
    def check(self, graph, node):
        visited = []  # List to keep track of visited nodes.
        queue = []  # Initialize a queue
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0) 
            print (s, end = " ") 

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)