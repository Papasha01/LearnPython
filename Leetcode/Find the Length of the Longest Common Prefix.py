class Node():
    def __init__(self, parents:dict, ch:str) -> None:
        self.parents = parents
        self.ch = ch
        
    
class Tree():
    def __init__(self):
        self.parents = {}

    def add(self, string:str):
        for ch in string:
            if ch not in self.parents:
                self.parents[ch] = Node({}, ch)
                self = self.parents[ch]
            else:
                self = self.parents[ch]
    
    def search_prefix(self, word:str) -> int:
        length = 0
        for ch in word:
            if ch not in self.parents:
                break
            else:
                self = self.parents[ch]
                length +=1
        return length

class Solution:
    def longestCommonPrefix(self, arr1: list, arr2: list) -> int:
        Tr = Tree()
        max_pref = 0
        for element in arr1:
            Tr.add(str(element))
        for element in arr2:
            prefix = Tr.search_prefix(str(element))
            if max_pref<prefix:max_pref=prefix
        return max_pref
        

        
Sol = Solution()
print(Sol.longestCommonPrefix([6,32],[8,36]))