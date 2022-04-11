from TernaryTree import Trie
from bidict import bidict

class WordMatcher:
    def build_prefixes(self, graph, node, word_repository, valid_prefixes, visited_node):
        for neighbour in graph[node]:
            # If there aren't any prefixes just yet
            prefix = node[0] + neighbour[0] # sanitize (strip coordinates)
            # if it is a valid prefix and its neighbours aren't yet evaluated
            possible_prefix_key = node + '#' + neighbour
            if prefix in word_repository and prefix not in valid_prefixes.values():
                valid_prefixes[possible_prefix_key] = prefix
                visited_node.append(node)

    def build_words(self, valid_prefixes, graph, word_repository, visited_node, valid_words):
        for prefix in valid_prefixes.values():
            node_prefix_key = valid_prefixes.inverse[prefix].split('#')[1]
            for neighbour in graph[node_prefix_key]:
                possible_word = prefix + neighbour[0]
        
                if possible_word in word_repository and neighbour not in visited_node:
                    visited_node.append(neighbour)
                    stored_word_key = valid_prefixes.inverse[prefix] + '#' + neighbour

                    if stored_word_key not in valid_words:
                        valid_words[stored_word_key] = possible_word

    def check(self, graph, node):
        word_repository = Trie()
        valid_prefixes = bidict({})
        valid_words = {}
        visited_node = []
        visited_node.append(node)

        # If there aren't any prefixes just yet
        self.build_prefixes(graph, node, word_repository, valid_prefixes, visited_node)
        
        # Once prefixes are found, look for whole words starting from them
        self.build_words(valid_prefixes, graph, word_repository, visited_node, valid_words)

        return valid_words

    
    # def check_possible_words(self, possible_word, graph, prefix):
    #     if possible_word not in word_repository:
    #         return None
    #     else: