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
                preffix = self.sanitize(s) + self.sanitize(neighbour)

                if preffix in word_repository and neighbour not in visited_node:
                    visited_node.append(neighbour)
                    search_queue.append(neighbour)
            
    def sanitize(self, string):
        return string[0]