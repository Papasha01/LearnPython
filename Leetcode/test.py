from collections import deque

class Node:
    def __init__(self, char: str, is_leaf: bool = False):
        self.char = char
        self.is_leaf = is_leaf
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node('')

    def add(self, word: str):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node(ch, False)
            current = current.children[ch]
        current.is_leaf = True

    def traverse_bfs(self):
        if not self.root:
            return
        
        queue = deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            print(current.char, end=" ")

            for child in current.children.values():
                queue.append(child)

# Пример использования
trie = Trie()
trie.add("apple")
trie.add("banana")
trie.add("orange")

trie.traverse_bfs()
