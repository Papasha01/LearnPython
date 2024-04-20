from collections import deque

class Node:
    def __init__(self, parents:dict, char:str, is_leaf:bool = False):
        self.parents = parents
        self.char = char
        self.is_leaf = is_leaf

class Trie:
    def __init__(self):
        self.parents = {}

    def add(self, word:str):
        for ch in word:
            if ch not in self.parents:
                self.parents [ch] = Node({}, ch, True if ch == word [-1] else False)
                self = self.parents[ch] 
            else:
                self = self.parents[ch]
                if ch == word[-1]:
                    self.is_leaf = True

    def search(self, word:str) -> str:
        result = ""
        
        for ch in word:
            if ch in self.parents:
                self = self.parents[ch]
                result += ch
            else:
                result = "None"
                break
        return result

    def bfs(self, root:Node = None):
        if not root:
                root = self
        q = deque()
        q += list(root.parents.values())
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                print(list(node.char), end=" ")
                q += node.parents.values()    
 
    def dfs(self, root:Node = None):
        if root is None:
            root = self
        if root.parents.keys():
            print(list(root.parents.keys()), end=" ") 
        for child in root.parents.values():
            self.dfs(child)

Tr = Trie()
Tr.add("ABD")
Tr.add("ABE")
Tr.add("ACF")
Tr.add("ACG")
Tr.dfs()
print("")
Tr.bfs()
