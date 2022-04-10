from TernaryTree import Trie

class BFS:
    def check(self, graph, node):
        word_repository = Trie()
        visited_node = [] 
        search_queue = []  
        visited_node.append(node)
        search_queue.append(node)

        while search_queue:
            s = search_queue.pop(0) 
            print (s, end = " ") 

            for neighbour in graph[s]:
                if neighbour not in visited_node:
                    visited_node.append(neighbour)
                    search_queue.append(neighbour)
            
            print()